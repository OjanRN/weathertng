from flask import Flask,jsonify
import requests

def get_api():
    URL = "https://api.openweathermap.org/data/2.5/weather?q=Tangerang&appid=67364aa4b9ee77a66fc7a32db03cdd84"
    raw_data = requests.get(URL)
    json_data = raw_data.json()
    return json_data['main']['temp']

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1 style='font-family: monospace;'>Example URL: /api</h1>"

@app.route('/api')
def apireturn():
    degree = get_api()
    result_dict = {"WEATHER":degree}
    return jsonify(result_dict)
    
if __name__ == "__main__":
    app.run()
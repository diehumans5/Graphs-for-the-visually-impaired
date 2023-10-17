from flask import Flask, request, jsonify,render_template
from nlpop import nlp
from nlpop import nlpdes
import os
import pyttsx3
import pyautogui
from graph1 import run;
send_data = ""
app = Flask(__name__)

process_data = ""

male = 0

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[male].id)

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()
    print(data['input_data']['key1'])
    try:
        processed_data = nlp(data['input_data']['key1'])
        print(processed_data)
        ok_data = nlpdes(processed_data)
        engine.say(ok_data)
        engine.runAndWait()
        print(ok_data)
        run(processed_data)
        return jsonify({'output_data': processed_data})
    except :
        return jsonify({'output_data':"please enter again"})

    
if __name__ == '__main__':
    app.run(debug=True)

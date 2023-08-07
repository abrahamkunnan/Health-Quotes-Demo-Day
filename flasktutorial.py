from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def route():
    return "Hello world"

@app.route('/bruh')
def bruh():
    return "bruh"
app.run(debug=True, port=8002, host='0.0.0.0')

import asyncio
from tkinter import Variable

from flask import Flask, render_template
from ble import discover

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/exhibition')
def exhibition():
    return render_template('exhibition.html')

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/current_location')
def current_location():
    uuid = discover()
    return render_template('current_location.html', uuid = uuid )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
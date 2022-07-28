import asyncio

from flask import Flask, render_template
# from ble import discover
from new_ble import discover

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

## beacon
@app.route('/current_location')
def current_location():
    # uuid = discover()
    uuid = 1
    return render_template('current_location.html', uuid = uuid )

@app.route('/preview')
def preview():
    return render_template('preview.html')

## beacon + API
@app.route('/preview/exhibition')
def preview_exhibition():
    uuid = asyncio.run(discover())
    print(uuid)
    return render_template('preview02.html', uuid = uuid)

@app.route('/event')
def event():
    return render_template('event.html')

@app.route('/mission')
def mission():
    return render_template('mission.html')

@app.route('/event/detail')
def event_detail():
    return render_template('event02.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
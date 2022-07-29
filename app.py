import asyncio

from flask import Flask, render_template, request
from ble import BLEGetter
from util import get_token, get_fsm_token, mac_for_ip
# from new_ble import discover

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
    token = get_fsm_token()
    return render_template('exhibition.html', token = token)

@app.route('/location')
def location():
    return render_template('location.html')

## beacon
@app.route('/current_location')
def current_location():
    getter = BLEGetter()
    asyncio.run(getter.discover())
    uuid = getter.uuid
    token = get_token()
    return render_template('current_location.html', uuid = uuid, token = token )

@app.route('/preview')
def preview():
    return render_template('preview.html')

## beacon + API
@app.route('/preview/exhibition')
def preview_exhibition():
    getter = BLEGetter()
    asyncio.run(getter.discover())
    uuid = getter.uuid
    token = get_token()
    ip = request.remote_addr
    mac_address = mac_for_ip(ip)
    return render_template('preview02.html', uuid = uuid, token = token, mac_address = mac_address)

@app.route('/event')
def event():
    token = get_fsm_token()
    return render_template('event.html', token=token)

@app.route('/mission')
def mission():
    token = get_fsm_token()
    return render_template('mission.html', token=token)

@app.route('/event/detail')
def event_detail():
    token = get_fsm_token()
    return render_template('event02.html', token = token)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
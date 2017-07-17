from flask import Flask, jsonify
import sys
import bluetooth
from threading import Thread
from gattlib import BeaconService

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "running"})

@app.route('/simple-scan', methods=['GET'])
def simple_scan():
    return jsonify(bluetooth.discover_devices())

@app.route('/scan-for/<string:device_address>', methods=['GET'])
def scan_for_device(device_address):
    if(not(bluetooth.is_valid_address(device_address))):
        return jsonify({"is_present": False})

    name = bluetooth.lookup_name(device_address, timeout=4)
    if(name is None):
        return jsonify({"is_present": False})
    else:
        return jsonify({"is_present": True})

@app.route('/start-beacon', methods=['POST'])
def begin_beacon():
    device_id = request.args.get('device_id')
    major = request.args.get('major') 
    minor = request.args.get('minor')
    uuid = request.args.get('uuid')
    tx_power = request.args.get('tx_power')
    interval = request.args.get('interval')

    service = BeaconService(device_id)

    try:
        thread = Thread(target = service.start_advertising, args = (uuid, major, minor, tx_power, interval))
        thread.start()

        return jsonify({"is_started": True})
    except:
        return jsonify({"is_started": False})

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Invalid number of arguments!")
        sys.exit(1)

    host = sys.argv[1]
    port = sys.argv[2]
        
    app.run(host=host, port=port)

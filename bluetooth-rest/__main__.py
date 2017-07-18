from flask import Flask, jsonify, request
import sys
import bt
import beacon

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"is_running": True})

@app.route('/scan-for/any', methods=['GET'])
def simple_scan():
    return jsonify(bt.simple_scan())

@app.route('/scan-for/<string:device_address>', methods=['GET'])
def scan_for_device(device_address):
    timeout = 4

    try:
        timeout = int(request.args.get('timeout'))
    except:
        pass
        
    return jsonify({
        "is_present": bt.is_device_present(device_address, timeout)
    })

@app.route('/beacon/status', methods=['GET'])
def get_beacon_status():
    return jsonify({
        "is_running": beacon.is_running()
    })

@app.route('/beacon/stop', methods=['POST'])
def stop_beacon():
    try:
        device_name = request.args.get('device_name')
        if(device_name is None):
            raise Exception()
        else:
            device_name = str(device_name)
    except:
        return jsonify({
            "is_stopped": False
        })
    
    stopped_successfully = beacon.stop(device_name)
    return jsonify({
        "is_stopped": stopped_successfully
    })
    
@app.route('/beacon/start', methods=['POST'])
def start_beacon():

    try:
        beacon_params = {
            "device_id": str(request.args.get('device_id')),
            "major": int(request.args.get('major')),
            "minor": int(request.args.get('minor')),
            "uuid": str(request.args.get('uuid')),
            "tx_power": int(request.args.get('tx_power')),
            "interval": int(request.args.get('interval')),
        }
    except:
        return jsonify({
            "is_started": False
        })

    started_successfully = beacon.start(beacon_params);

    return jsonify({
        "is_started": started_successfully
    })

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Invalid number of arguments!")
        sys.exit(1)

    host = sys.argv[1]
    port = sys.argv[2]
        
    app.run(host=host, port=port)

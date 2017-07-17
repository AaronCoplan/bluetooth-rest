from flask import Flask, jsonify
import bluetooth

app = Flask(__name__)

@app.route('/simple-scan', methods=['GET'])
def simple_scan():
    return jsonify(bluetooth.discover_devices())

if __name__ == "__main__":
    app.run()

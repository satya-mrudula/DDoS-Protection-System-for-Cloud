from flask import Flask, request, jsonify
from detector import analyze_request
from mitigation import Mitigation

app = Flask(__name__)
mitigator = Mitigation()

@app.route("/traffic", methods=["POST"])
def traffic():
    data = request.get_json()
    ip = data.get("ip", "unknown")

    result = analyze_request(ip)
    if result["attack"]:
        mitigator.block_ip(ip)
        return jsonify({"status": "blocked", "ip": ip}), 403

    return jsonify({"status": "allowed", "ip": ip}), 200

@app.route("/status")
def status():
    return jsonify({"blocked_ips": list(mitigator.blocked_ips)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

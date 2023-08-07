import os
from flask import Flask, jsonify
from datetime import datetime
from threading import Thread

from collector import send_data

app = Flask(__name__)


@app.get("/metrics")
def metrics_get():
    pass


@app.get("/metrics/last")
def metrics_last_get():
    data = [datetime.strptime(p.removesuffix(".json"), "%Y-%m-%dT%H:%M:%S") for p in os.listdir("data")]
    data = sorted(data, reverse=True)

    return jsonify(list(data))


if __name__ == "__main__":
    t = Thread(target=send_data, daemon=True)
    t.start()
    app.run("0.0.0.0", port=5000)
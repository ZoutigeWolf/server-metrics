import json
import os
from flask import Flask, jsonify
from datetime import datetime
from threading import Thread

from collector import send_data

app = Flask(__name__)


def load_json(p: str):
    with open(p) as f:
        return json.load(f)


@app.get("/metrics")
def metrics_get():
    pass


@app.get("/metrics/last")
def metrics_last_get():
    files = [datetime.strptime(p.removesuffix(".json"), "%Y-%m-%dT%H:%M:%S") for p in os.listdir("data")]
    file_name = sorted(files, reverse=True)[0].strftime("%Y-%m-%dT%H:%M:%S") + ".json"

    data = load_json("data/" + file_name)

    return jsonify(data)


if __name__ == "__main__":
    t = Thread(target=send_data, daemon=True)
    t.start()
    app.run("0.0.0.0", port=5000)
import os
from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.get("/metrics")
def metrics_get():
    pass


@app.get("/metrics/last")
def metrics_last_get():
    data = [datetime.strptime(p.removesuffix(".json"), "%Y-%m-%dT%H:%M:%S") for p in os.listdir("data")]
    data = sorted(data, reverse=True)
    print(data)

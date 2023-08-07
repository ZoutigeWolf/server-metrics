import subprocess
from datetime import datetime
import json


def send_data():
    p = subprocess.Popen(["jsonperfmon", "-A", "1"], stdout=subprocess.PIPE)

    for c in iter(p.stdout.readline, ""):
        data = json.loads(c)
        with open(datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + ".json", "w") as f:
            json.dump(data, f, indent=4)


if __name__ == "__main__":
    send_data()
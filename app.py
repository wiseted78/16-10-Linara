
import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent

    return jsonify({
        "message": "Cloud microservice is working!",
        "CPU_Usage_Percent": cpu_usage,
        "RAM_Usage_Percent": ram_usage
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

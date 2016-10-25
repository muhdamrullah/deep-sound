import os
import subprocess

from flask import Flask, redirect

app = Flask(__name__)

@app.route("/")
def hello():
    subprocess.call('python listen_to_my_request.py', shell=True)
    return redirect("http://192.168.1.145:8888/current_anotated.jpg")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6007))
    app.run(host='0.0.0.0', port=port)

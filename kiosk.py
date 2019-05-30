import socket
from flask import Flask, request, redirect, render_template

app = Flask(__name__, static_url_path="")
app.url_map.strict_slashes = False

destination = "https://www.google.com/"

@app.route("/config", methods=['GET', 'POST'])
def config():
    global destination
    if request.method == "POST":
        destination = request.form["URL"]
    return render_template("config.html", destination=destination)

@app.route("/display")
def display():
    return redirect(destination)

if __name__ == "__main__":
    host_ip = ([(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
    app.run(host=host_ip, port=4321)

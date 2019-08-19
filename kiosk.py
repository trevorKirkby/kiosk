import socket
from flask import Flask, request, redirect, render_template
from selenium import webdriver

PORT = 4321

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options = chrome_options)

app = Flask(__name__, static_url_path="")
app.url_map.strict_slashes = False

destination = "https://www.google.com/"

@app.route("/config", methods=['GET', 'POST'])
def config():
    global destination
    if request.method == "POST":
        destination = request.form["URL"]
        driver.get(destination)
    return render_template("config.html", destination=destination)

@app.route("/display")
def display():
    return redirect(destination)

if __name__ == "__main__":
    try:
        host_ip = ([(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
        driver.get(destination)
        driver.fullscreen_window()
        app.run(host=host_ip, port=PORT)
    finally:
        driver.quit()

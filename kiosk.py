import socket
from flask import Flask, request, redirect, render_template, url_for
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PORT = 4321
host_ip = ([(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', chrome_options = chrome_options)
action = ActionChains(driver)

app = Flask(__name__, static_url_path="")
app.url_map.strict_slashes = False

destination = "http://www.google.com"

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
        driver.get(destination)
        driver.fullscreen_window()
        search_box = driver.find_element_by_name('q')
        search_box.send_keys("{}:{}/config".format(host_ip, PORT))
        app.run(host=host_ip, port=PORT)
    finally:
        driver.quit()

# kiosk
simple web-server for displaying a web page from a raspberry pi

# Setup
0. If installing Raspbian, install Raspbian Desktop with recommended software.
1. Install the latest versions of Chromium Browser and the Unclutter package: `sudo apt-get install chromium-browser unclutter`
2. Set up Selenium for use with chromium within python according to [this guide](https://www.reddit.com/r/selenium/comments/7341wt/success_how_to_run_selenium_chrome_webdriver_on/).
3. Install the flask library for python: `pip install flask`
4. Add the following lines to make kiosk and unclutter run on startup: `sudo nano /etc/profile`
```
unclutter &
python /home/pi/kiosk/kiosk.py &
```

# Usage
Reboot to start kiosk mode. Visit the page `[IP address]:[port]/config` to change what URL is being displayed.
Kiosk will initially display the correct IP address after booting.
Will run on port 4321 by default. Port may be configured as a constant in kiosk.py.

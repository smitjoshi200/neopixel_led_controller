from flask import Flask
import subprocess
import os

app = Flask(__name__)
p = 0

@app.before_request
def before_request():
    global p
    try:
        p.terminate()
    except:
        pass
    os.system("sudo python3 exit.py")

@app.route('/')
def index():
    return "Hello from Flask!"

@app.route('/led_on')
def turn_on():
    p = subprocess.Popen(["sudo", "python3", "main.py"])
    return "LEDS Turned On", 200

@app.route('/led_off')
def turn_off():
    try:
        p.terminate()
    except:
        pass
    subprocess.run(["sudo", "python3", "exit.py"])
    return "LEDS Turned Off", 200

@app.route('/effects/<effect>')
def effects(effect):
    if effect == "rainbow":
        p = subprocess.Popen(["sudo", "python3", "rainbow.py"])
        return "Started Rainbow Effect", 200
    elif effect == "warm":
        p = subprocess.Popen(["sudo", "python3", "warm.py"])
        return "Started Warm Effect", 200
    else:
        return "Effect Not Found", 404
    
    

if __name__ == "__main__":
    app.run(debug=True)
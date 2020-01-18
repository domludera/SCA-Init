from flask import Flask
import serial
app = Flask(__name__)

ser = serial.Serial('/dev/ttyACM0')

@app.route("/")
def greeting():
    return "<h2 style='color:green'>LED 9000</h1><a href=\"on\">Turn ON</a><br><a href=\"off\">Turn OFF</a>"

@app.route("/on")
def on():
    ser.write(b'1')
    return "<h1 style='color:green'>LED 9000</h1><a href=\"on\">Turn ON</a><br><a href=\"off\">Turn OFF</a>"

@app.route("/off")
def off():
    ser.write(b'0')
    return "<h1 style='color:green'>LED 9000</h1><a href=\"on\">Turn ON</a><br><a href=\"off\">Turn OFF</a>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
from energenie import switch_on, switch_off

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/on1/')
def on1():
    switch_on(1)
    return render_template('index.html')

@app.route('/on2/')
def on2():
    switch_on(2)
    return render_template('index.html')

@app.route('/on3/')
def on3():
    switch_on(3)
    return render_template('index.html')

@app.route('/on4/')
def on4():
    switch_on(4)
    return render_template('index.html')


@app.route('/off1/')
def off1():
    switch_off(1)
    return render_template('index.html')

@app.route('/off2/')
def off2():
    switch_off(2)
    return render_template('index.html')

@app.route('/off3/')
def off3():
    switch_off(3)
    return render_template('index.html')

@app.route('/off4/')
def off4():
    switch_off(4)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') #, port=int("5001"))


from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime
import threading
import time

app = Flask(__name__)
app.secret_key = 'secret_key'

# Global variables for alarm
alarm_time = None
alarm_triggered = False

# Function to check and trigger the alarm
def alarm_checker():
    global alarm_time, alarm_triggered
    while True:
        if alarm_time and datetime.now() >= alarm_time:
            alarm_triggered = True
            alarm_time = None  # Reset alarm after triggering
        time.sleep(1)  # Check every second

# Background thread to run the alarm checker
threading.Thread(target=alarm_checker, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html', alarm_time=alarm_time, alarm_triggered=alarm_triggered)

@app.route('/set_alarm', methods=['POST'])
def set_alarm():
    global alarm_time, alarm_triggered
    alarm_triggered = False  # Reset alarm status
    alarm_input = request.form.get('alarm_time')
    if alarm_input:
        try:
            alarm_time = datetime.strptime(alarm_input, '%Y-%m-%dT%H:%M')
            if alarm_time < datetime.now():
                flash("Alarm time must be in the future!", "danger")
            else:
                flash(f"Alarm set for {alarm_time.strftime('%Y-%m-%d %H:%M:%S')}!", "success")
        except ValueError:
            flash("Invalid date-time format!", "danger")
    return redirect(url_for('index'))

@app.route('/clear_alarm', methods=['POST'])
def clear_alarm():
    global alarm_time, alarm_triggered
    alarm_time = None
    alarm_triggered = False
    flash("Alarm cleared!", "success")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib

app = Flask(__name__)
CORS(app)

# 🔥 Temporary storage (no database)
latest_data = {
    "temperature": 0,
    "humidity": 0,
    "air": 0,
    "time": "No data yet"
}

# 📩 EMAIL ALERT (AQI > 200)
def send_email_alert(value):
    try:
        sender = "your_email@gmail.com"
        password = "your_app_password"
        receiver = "receiver_email@gmail.com"

        message = f"Subject: AQI Alert\n\n⚠️ Air Quality crossed limit! AQI = {value}"

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        server.quit()

        print("Email sent!")

    except Exception as e:
        print("Email error:", e)


# 🟢 HOME ROUTE
@app.route('/')
def home():
    return "Smart Classroom API Running"


# 📥 RECEIVE DATA (POST)
@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data

    try:
        data = request.get_json()

        temp = data.get("temperature")
        hum = data.get("humidity")
        air = data.get("air")

        print("Received:", temp, hum, air)

        # store latest values
        latest_data = {
            "temperature": temp,
            "humidity": hum,
            "air": air,
            "time": "just now"
        }

        # 🚨 ALERT
        if air is not None and air > 200:
            send_email_alert(air)

        return jsonify({"status": "stored"})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


# 📊 GET DATA
@app.route('/get-data')
def get_data():
    return jsonify(latest_data)


# 🚀 RUN SERVER
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
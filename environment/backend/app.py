from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time
import os
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# 🌐 MONGODB CONNECTION
MONGO_URI = "mongodb+srv://Dhruv155_db_user:7h5E9fFzffF9V8Yf@iot-env.0ofnd6w.mongodb.net/iot_db?retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)
db = client["iot_db"]
collection = db["readings"]

# ⏱️ Email cooldown
last_email_time = 0
EMAIL_COOLDOWN = 60


# 📩 EMAIL ALERT (MAILERSEND)
def send_email_alert(value):
    try:
        api_key = "mlsn.623eaa2a9f35028ab9fb4f3b8df1a8910a86f1ae89024941019121b8735acb24"

        url = "https://api.mailersend.com/v1/email"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        data = {
            "from": {
                "email": "iot@test-eqvygm07mx8l0p7w.mlsender.net"
            },
            "to": [
                {
                    "email": "vergilwiz155@gmail.com"
                }
            ],
            "subject": "🚨 Smart Classroom Alert",
            "text": f"BAD AIR QUALITY!!!!!\nAQI Value: {value}\nFan and buzzer activated."
        }

        response = requests.post(url, headers=headers, json=data)

        print("📧 MailerSend response:", response.status_code)
        print(response.text)

    except Exception as e:
        print("❌ MailerSend error:", e)


# 🟢 HOME
@app.route('/')
def home():
    return "Smart Classroom API Running 🚀"


# 📥 RECEIVE DATA
@app.route('/data', methods=['POST'])
def receive_data():
    global last_email_time

    try:
        data = request.get_json()

        temp = data.get("temperature")
        hum = data.get("humidity")
        air = data.get("air")

        print("📥 Received:", temp, hum, air)

        current_time_str = time.strftime("%H:%M:%S")

        # 💾 SAVE TO MONGODB
        collection.insert_one({
            "temperature": temp,
            "humidity": hum,
            "air": air,
            "time": current_time_str
        })

        # 🚨 ALERT
        current_time = time.time()

        if air is not None and air > 200:
            print("🚨 ALERT CONDITION TRUE")

            if current_time - last_email_time > EMAIL_COOLDOWN:
                send_email_alert(air)
                last_email_time = current_time
                print("🚨 Alert triggered")

        return jsonify({"status": "stored"})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": str(e)}), 500


# 📊 GET DATA (LATEST ENTRY)
@app.route('/get-data')
def get_data():
    try:
        latest = collection.find_one(sort=[("_id", -1)])

        if latest:
            return jsonify({
                "temperature": latest.get("temperature", 0),
                "humidity": latest.get("humidity", 0),
                "air": latest.get("air", 0),
                "time": latest.get("time", "No data")
            })
        else:
            return jsonify({
                "temperature": 0,
                "humidity": 0,
                "air": 0,
                "time": "No data yet"
            })

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({
            "temperature": 0,
            "humidity": 0,
            "air": 0,
            "time": "Error"
        })


# 🚀 RUN
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

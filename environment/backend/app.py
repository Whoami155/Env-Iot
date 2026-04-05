from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time
import sqlite3

app = Flask(__name__)
CORS(app)

# 🗄️ INIT DATABASE
def init_db():
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS readings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperature REAL,
        humidity REAL,
        air REAL,
        time TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# 🔥 Temporary storage (will sync with DB)
latest_data = {
    "temperature": 0,
    "humidity": 0,
    "air": 0,
    "time": "No data yet"
}

# ⏱️ Email cooldown
last_email_time = 0
EMAIL_COOLDOWN = 60


# 📩 EMAIL ALERT (MAILERSEND)
def send_email_alert(value):
    try:
        api_key = "mlsn.2842d15d53b855149336042013df026bdf3c225e74b7072168c198995935f1de"

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
    global latest_data, last_email_time

    try:
        data = request.get_json()

        temp = data.get("temperature")
        hum = data.get("humidity")
        air = data.get("air")

        print("📥 Received:", temp, hum, air)

        current_time_str = time.strftime("%H:%M:%S")

        # 💾 SAVE TO DB
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO readings (temperature, humidity, air, time)
            VALUES (?, ?, ?, ?)
        """, (temp, hum, air, current_time_str))

        conn.commit()
        conn.close()

        # 🔄 UPDATE LATEST
        latest_data = {
            "temperature": temp,
            "humidity": hum,
            "air": air,
            "time": current_time_str
        }

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


# 📊 GET DATA (FROM DB LAST ENTRY)
@app.route('/get-data')
def get_data():
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()

        cursor.execute("""
            SELECT temperature, humidity, air, time
            FROM readings
            ORDER BY id DESC
            LIMIT 1
        """)

        row = cursor.fetchone()
        conn.close()

        if row:
            return jsonify({
                "temperature": row[0],
                "humidity": row[1],
                "air": row[2],
                "time": row[3]
            })
        else:
            return jsonify(latest_data)

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify(latest_data)


# 🚀 RUN
if __name__ == '__main__':
    import os
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))

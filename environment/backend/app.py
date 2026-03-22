from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os
import smtplib

app = Flask(__name__)
CORS(app)

# 🔗 DATABASE CONNECTION
def get_connection():
    return psycopg2.connect(os.getenv("DATABASE_URL"))

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
    except Exception as e:
        print("Email error:", e)


# 📥 RECEIVE DATA FROM NODEMCU
@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json

    temp = data.get("temperature")
    hum = data.get("humidity")
    air = data.get("air")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO readings (temperature, humidity, air) VALUES (%s, %s, %s)",
        (temp, hum, air)
    )

    conn.commit()
    cur.close()
    conn.close()

    # 🚨 ALERT
    if air is not None and air > 200:
        send_email_alert(air)

    return jsonify({"status": "stored"})


# 📊 GET LATEST DATA (OFFLINE SAFE)
@app.route('/get-data')
def get_data():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT temperature, humidity, air, timestamp
        FROM readings
        ORDER BY id DESC LIMIT 1
    """)

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return jsonify({
            "temperature": row[0],
            "humidity": row[1],
            "air": row[2],
            "time": row[3].strftime("%Y-%m-%d %H:%M:%S")
        })
    else:
        return jsonify({
            "temperature": 0,
            "humidity": 0,
            "air": 0,
            "time": "No data yet"
        })


# 📈 HISTORY (DAY / WEEK)
@app.route('/history')
def history():
    period = request.args.get("period", "day")

    conn = get_connection()
    cur = conn.cursor()

    if period == "week":
        query = """
            SELECT temperature, humidity, air, timestamp
            FROM readings
            WHERE timestamp >= NOW() - INTERVAL '7 days'
            ORDER BY timestamp
        """
    else:
        query = """
            SELECT temperature, humidity, air, timestamp
            FROM readings
            WHERE timestamp >= NOW() - INTERVAL '1 day'
            ORDER BY timestamp
        """

    cur.execute(query)
    rows = cur.fetchall()

    cur.close()
    conn.close()

    data = []
    for r in rows:
        data.append({
            "temperature": r[0],
            "humidity": r[1],
            "air": r[2],
            "time": r[3].strftime("%H:%M:%S")
        })

    return jsonify(data)


# 🟢 HEALTH CHECK (OPTIONAL BUT GOOD)
@app.route('/')
def home():
    return "Smart Classroom API Running"


# 🚀 RUN
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
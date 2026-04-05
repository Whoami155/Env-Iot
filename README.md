# 🌿 Smart Classroom Environment Monitoring System

## 📌 Overview

The **Smart Classroom Environment Monitoring System** is an IoT-based solution designed to monitor environmental conditions in real-time and display them through a live web dashboard.

This system collects sensor data using an **Arduino UNO**, transmits it via **NodeMCU (ESP8266)** to a **cloud-based backend**, and visualizes it on a deployed frontend dashboard. It also includes automation and alert mechanisms to improve safety and comfort.

---

## 🚀 System Architecture

```
Sensors → Arduino UNO → Serial Communication → NodeMCU → WiFi → Cloud Backend → Web Dashboard
```

### 🔄 Data Flow

1. Sensors collect environmental data
2. Arduino processes readings
3. Data sent via Serial to NodeMCU
4. NodeMCU sends data to cloud backend (Render)
5. Backend stores data (SQLite)
6. Frontend fetches and displays live data

---

## 🧰 Hardware Components

* Arduino UNO
* NodeMCU (ESP8266)
* DHT11 Temperature & Humidity Sensor
* MQ Air Quality Sensor
* Passive Buzzer 🔔
* Relay Module ⚡
* DC Fan (for ventilation)
* Breadboard
* Jumper Wires
* USB Cables

---

## 💻 Software & Technologies

* Arduino IDE
* Embedded C / Arduino Programming
* Flask (Python Backend)
* SQLite Database
* HTML, CSS, JavaScript (Frontend)
* Chart.js (Data Visualization)
* MailerSend API (Email Alerts)
* Render (Backend Deployment)
* Netlify / GitHub Pages (Frontend Deployment)

---

## ✨ Features Implemented

### 📊 Real-Time Monitoring

* Temperature tracking
* Humidity monitoring
* Air quality measurement (MQ sensor)

### 🌐 Live Dashboard

* Real-time data visualization
* Graphs and gauges
* Responsive UI

### 🔔 Alert System

* **Passive buzzer** activates when AQI exceeds threshold
* **Email alerts** sent using MailerSend API

### ⚙️ Automation

* **Relay-controlled fan** turns ON automatically when air quality is poor

### ☁️ Cloud Integration

* Backend deployed on cloud
* Data accessible globally via API

### 💾 Persistent Storage

* SQLite database stores latest readings
* Data retained even after server restart

---

## 🔔 Alert Logic

```
If Air Quality > Threshold:
    → Buzzer ON
    → Fan ON
    → Email Alert Sent
Else:
    → Buzzer OFF
    → Fan OFF
```

---

## 📦 API Endpoints

### 🔹 GET Data

```
/get-data
```

Returns latest sensor readings in JSON format.

### 🔹 POST Data

```
/data
```

Receives sensor data from NodeMCU.

---

## 📊 Example Data Format

```
temperature,humidity,airQuality
```

Example:

```
26,58,210
```

---

## 🌐 Deployment

* **Backend:** Render (Flask API)
* **Frontend:** Netlify / GitHub Pages

---

## 🎯 Project Purpose

This project demonstrates how IoT, cloud computing, and web technologies can be combined to create a **smart monitoring and automation system** for real-world environments like classrooms.

It improves:

* Comfort
* Safety
* Energy efficiency

---

## 🚀 Future Enhancements

* Noise monitoring using sound sensor
* Occupancy detection (PIR sensor)
* Smart energy saving automation
* Historical data analytics
* AI-based environment optimization
* Mobile app integration

---

## 💡 Key Highlights

* Full-stack IoT system
* Real-time cloud communication
* Automation + alerts
* Persistent data storage
* Fully deployed project

---

## 📜 License

This project is open-source and intended for educational purposes.

---

## 👨‍💻 Author

Developed by **Dhruv**
K.R. Mangalam University


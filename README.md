Smart Classroom Environment Monitoring System
Overview

The Smart Classroom Environment Monitoring System is an IoT-based project designed to monitor environmental conditions inside a classroom and display them in real time through a cloud dashboard.

The system collects sensor data using an Arduino UNO, sends the data to a NodeMCU (ESP8266), and publishes it to the Blynk IoT cloud, where it can be viewed from a web dashboard or mobile device.

The goal of the project is to improve classroom comfort, safety, and energy efficiency by monitoring key environmental parameters such as temperature, humidity, air quality, noise levels, and occupancy.

System Architecture

Sensors collect environmental data and send it to the Arduino. The Arduino processes the sensor readings and sends them through serial communication to the NodeMCU. The NodeMCU connects to WiFi and transmits the data to the Blynk cloud platform. The Blynk dashboard displays the values in real time.

Flow:

Sensors → Arduino UNO → Serial Communication → NodeMCU (ESP8266) → WiFi → Blynk Cloud → Dashboard
Hardware Components
Arduino UNO
NodeMCU (ESP8266 WiFi Module)
DHT11 Temperature and Humidity Sensor
MQ Air Quality Sensor
Breadboard
Jumper Wires
USB Cables (Arduino + NodeMCU)
Passive Buzzer (Alert System) ✅ (Implemented)
Future Hardware Additions
Relay Module
12V Fan (automatic ventilation control)
PIR Motion Sensor
Sound Sensor Module
Software & Technologies
Arduino IDE
Embedded C / Arduino Programming
Blynk IoT Platform
ESP8266 WiFi Library
DHT Sensor Library
Features Implemented
Real-time temperature monitoring
Real-time humidity monitoring
Air quality measurement
IoT dashboard using Blynk Cloud
WiFi connectivity via NodeMCU
Serial communication between Arduino and NodeMCU
Live data visualization using gauges and labels
Air Quality Alert System using Passive Buzzer 🔔
🔔 Alert System (Buzzer Integration)

A passive buzzer is integrated with the Arduino to provide real-time audible alerts when environmental conditions exceed safe limits.

The system continuously monitors air quality using an MQ sensor.
If the air quality value crosses a predefined threshold, the buzzer is activated using a frequency signal (tone() function).
When conditions return to normal, the buzzer automatically stops (noTone()).

Logic:

If Air Quality > Threshold → Buzzer ON (Alert)
Else → Buzzer OFF

This ensures immediate attention to poor air conditions without relying only on the dashboard.

Features Planned

The following features will be implemented to enhance the system:

Noise Monitoring

A sound sensor will detect classroom noise levels and display them on the dashboard.

Occupancy Detection

A PIR motion sensor will detect whether people are present in the classroom.

Automatic Ventilation

A relay-controlled fan will automatically turn ON when air quality becomes poor.

Smart Energy Saving

If no motion is detected in the classroom for a period of time, the system will automatically turn off connected devices.

Data Flow
Sensors measure environmental conditions.
Arduino reads the sensor values.
Arduino sends formatted data through Serial communication.
NodeMCU receives the data.
NodeMCU uploads the data to the Blynk cloud using WiFi.
The Blynk dashboard displays real-time values.
Example Data Format

Arduino sends sensor values in the following format:

temperature,humidity,airQuality

Example:

26,58,210

NodeMCU parses this data and sends it to Blynk Virtual Pins.

Dashboard

The Blynk dashboard includes:

Temperature gauge
Humidity gauge
Air quality indicator
Alert indication via buzzer (physical feedback)
Additional widgets for noise and motion detection

The dashboard allows users to monitor classroom conditions remotely.

Project Purpose

This project demonstrates how IoT can be used to create a smart monitoring system for educational environments, helping improve comfort, health, and energy efficiency.

Future Improvements

Possible future upgrades include:

Mobile notifications when air quality is poor
Historical data logging
Automatic fan speed control using relay module
AI-based classroom comfort analysis
Integration with smart building systems
License

This project is open-source and intended for educational purposes.

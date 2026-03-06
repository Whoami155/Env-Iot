Smart Classroom Environment Monitoring System (Current Progress)

Overview

This project is a Smart Classroom Environment Monitoring System built using Arduino UNO and multiple sensors. The system monitors environmental conditions inside a classroom such as temperature, humidity, and air quality, and provides alerts when certain thresholds are crossed. It is designed as the foundation for a larger IoT-based automation system.

Features Implemented So Far

- Reading temperature and humidity using the DHT11 sensor
- Monitoring air quality levels using an MQ gas sensor
- Displaying sensor readings through the Arduino serial monitor
- Alert system using a buzzer when sensor values exceed thresholds
- Initial testing and setup of sensors using Arduino

Hardware Used

- Arduino UNO
- DHT11 Temperature and Humidity Sensor
- MQ Air Quality Sensor
- Breadboard
- Jumper Wires
- Buzzer

Working

The sensors are connected to the Arduino UNO. The Arduino reads environmental data from the sensors and processes the values. If certain values exceed predefined thresholds, the system can trigger alerts such as activating a buzzer. The sensor readings are currently displayed through the Arduino serial monitor.

Current Status

The basic sensor monitoring system is functioning correctly. Temperature, humidity, and air quality readings can be obtained and used for basic alert logic.

Next Steps

- Add PIR motion sensor for occupancy detection
- Add sound sensor to monitor classroom noise levels
- Integrate a relay module and fan for automatic ventilation control
- Connect NodeMCU ESP8266 for WiFi-based monitoring
- Build a mobile app dashboard to display real-time classroom data

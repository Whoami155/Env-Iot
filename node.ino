#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <WiFiClientSecure.h>

//  WIFI
const char* ssid = "WIFI_NAME";
const char* password = "WIFI_PASSWORD";

// BACKEND URL 
String serverURL = "https://env-iot.onrender.com/data";

void setup() {
  Serial.begin(9600);
  delay(1000);

  WiFi.begin(ssid, password);
  Serial.print("Connecting");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConnected!");
  Serial.println(WiFi.localIP());
}

void loop() {

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Reconnecting...");
    WiFi.begin(ssid, password);
    delay(2000);
    return;
  }

  if (Serial.available()) {

    String data = Serial.readStringUntil('\n');
    data.trim();

    Serial.print("Received: ");
    Serial.println(data);

    float temperature, humidity, air;

    int parsed = sscanf(data.c_str(), "%f,%f,%f",
                        &temperature, &humidity, &air);

    if (parsed == 3) {

      bool alert = false;

      if (air > 200) {   // match backend threshold
        alert = true;
      }

      //  HTTPS FIX
      WiFiClientSecure client;
      client.setInsecure();

      HTTPClient http;
      http.begin(client, serverURL);
      http.addHeader("Content-Type", "application/json");

      // JSON data
      String json = "{";
      json += "\"temperature\":" + String(temperature) + ",";
      json += "\"humidity\":" + String(humidity) + ",";
      json += "\"air\":" + String(air) + ",";
      json += "\"alert\":" + String(alert ? "true" : "false");
      json += "}";

      Serial.print("Sending: ");
      Serial.println(json);

      int code = http.POST(json);

      Serial.print("Response: ");
      Serial.println(code);

      http.end();

    } else {
      Serial.println("Invalid data format");
    }
  }
}

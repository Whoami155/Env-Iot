#define BLYNK_TEMPLATE_ID "TMPL3q519xQ8X"
#define BLYNK_TEMPLATE_NAME "CLASSROOM ENVIRONMENT"
#define BLYNK_AUTH_TOKEN "************"

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char ssid[] = "AndroidAP_2853";
char pass[] = "qxq12346";

void setup()
{
  Serial.begin(9600);
  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);
}

void loop()
{
  Blynk.run();

  if (Serial.available())
  {
    String data = Serial.readStringUntil('\n');

    int temp, hum, air;
    sscanf(data.c_str(), "%d,%d,%d", &temp, &hum, &air);

    Blynk.virtualWrite(V0, temp);
    Blynk.virtualWrite(V1, hum);
    Blynk.virtualWrite(V2, air);
  }
}
#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>

// 🔐 WIFI
const char* ssid = "AndroidAP_2853";
const char* password = "qxq12346";

// 🌐 BACKEND
String serverURL = "http://10.65.191.195:5000/data";

void setup() {
  Serial.begin(9600);
  delay(1000);

  Serial.println("\nStarting NodeMCU...");

  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi Connected!");
}

void loop() {

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("Reconnecting WiFi...");
    WiFi.begin(ssid, password);
    delay(2000);
    return;
  }

  if (Serial.available()) {

    String data = Serial.readStringUntil('\n');
    data.trim();

    Serial.print("Raw Data: ");
    Serial.println(data);

    float temperature, humidity, air;

    int parsed = sscanf(data.c_str(), "%f,%f,%f", &temperature, &humidity, &air);

    if (parsed == 3) {

      WiFiClient client;
      HTTPClient http;

      http.begin(client, serverURL);
      http.addHeader("Content-Type", "application/json");

      String json = "{";
      json += "\"temperature\":" + String(temperature) + ",";
      json += "\"humidity\":" + String(humidity) + ",";
      json += "\"air\":" + String(air);
      json += "}";

      int httpResponseCode = http.POST(json);

      Serial.print("Response: ");
      Serial.println(httpResponseCode);

      http.end();

    } else {
      Serial.println("Invalid Data Format!");
    }
  }
}

#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

#define BUZZER 8
#define MQ_PIN A0

float AIR_THRESHOLD = 200;  // adjust after testing

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  pinMode(BUZZER, OUTPUT);
  dht.begin();
}

void loop() {

  // 🌡️ Read temperature & humidity
  int temperature = dht.readTemperature();
  int humidity = dht.readHumidity();

  // 🌫️ Read air quality (MQ sensor)
  int airRaw = analogRead(MQ_PIN);


  int air = airRaw;

  // ❗ Check if DHT failed
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("0,0,0");  // safe fallback
    return;
  }

  // 📡 Send clean data to NodeMCU
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.println(air);

  // 🔔 BUZZER LOGIC
  if (air > AIR_THRESHOLD) {
    tone(BUZZER, 1000);
  } else {
    noTone(BUZZER);
  }

  delay(2000);
}

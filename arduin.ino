#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

#define BUZZER 8
#define RELAY 7
#define MQ_PIN A0

int AIR_THRESHOLD = 300;   // adjust if needed

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);

  pinMode(BUZZER, OUTPUT);
  pinMode(RELAY, OUTPUT);

  digitalWrite(RELAY, HIGH); // relay OFF initially

  dht.begin();
}

void loop() {

  int temperature = dht.readTemperature();
  int humidity = dht.readHumidity();
  int air = analogRead(MQ_PIN);

  // Safety check
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("0,0,0");
    return;
  }

  // 📡 Send data to NodeMCU
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.println(air);

  //  CONTROL LOGIC
  if (air > AIR_THRESHOLD) {

    //  Buzzer ON
    tone(BUZZER, 1000);

    //  Fan ON
    digitalWrite(RELAY, LOW);

    Serial.println("ALERT: FAN ON");

  } else {

    //  Buzzer OFF
    noTone(BUZZER);

    //  Fan OFF
    digitalWrite(RELAY, HIGH);

    Serial.println("NORMAL");
  }

  delay(2000);
}

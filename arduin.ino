#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11

int airPin = A0;

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {

  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  int airQuality = analogRead(airPin);

  // send values to NodeMCU
  Serial.print((int)temperature);
  Serial.print(",");
  Serial.print((int)humidity);
  Serial.print(",");
  Serial.println(airQuality);

  delay(2000);
}

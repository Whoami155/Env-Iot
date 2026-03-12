#include <DHT.h>

// Pin Definitions
#define DHTPIN 2        // DHT11 data pin connected to Arduino pin 2
#define DHTTYPE DHT11
#define MQ135_PIN A0    // MQ135 connected to analog pin A0

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
}

void loop() {

  // Read temperature and humidity
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  // Read air quality value
  int airQuality = analogRead(MQ135_PIN);

  // Check if DHT sensor reading failed
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Print temperature
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  // Print humidity
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");

  // Print air quality
  Serial.print("Air Quality Value: ");
  Serial.println(airQuality);

  Serial.println("---------------------------");

  delay(2000); // wait 2 seconds
}
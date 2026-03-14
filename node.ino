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

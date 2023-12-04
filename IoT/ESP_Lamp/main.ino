#include "Config.h"
#include "Wifi.h"
#include "Server.h"
#include "Mqtt.h"


void setup() {
  Serial.begin(9600);
  Serial.println();
  pinMode(LED_BUILTIN, OUTPUT);
  start_AP_mode();
  bool wifi_is_on = init_WIFI(false);
  init_MQTT();
  server_init();                       
  String topic = "esp8266/command";
  String state_topic = "esp8266/state";
  mqtt_client.subscribe(topic.c_str());
  mqtt_client.publish(state_topic.c_str(), "hello there");
}

void loop() {
  server.handleClient();
  mqtt_client.loop();
}
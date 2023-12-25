#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const int triggerPin = 5;
const int echoPin = 4;

const char* wifiSSID = "yawnmain";
const char* wifiPassword = "mk666036";

const char* mqttServer = "broker.emqx.io";
const int mqttPort = 1883;
WiFiClient espClient;
PubSubClient client(espClient);

void connectToWiFi() {
  Serial.println("Connecting to Wi-Fi..");
  WiFi.begin(wifiSSID, wifiPassword);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to Wi-Fi..");
  }
  Serial.print("Connected to Wi-Fi: ");
  Serial.println(WiFi.SSID());
}

void connectToMQTT() {
  Serial.println("Connecting to MQTT...");
  while (!client.connected()) {
    if (client.connect("ESP8266_me")) {
      Serial.println("Connected to MQTT");
    } else {
      Serial.print("Failed to connect, state: ");
      Serial.println(client.state());
      delay(2000);
    }
  }
}

void measureDistanceAndPublish() {
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);

  unsigned long duration = pulseIn(echoPin, HIGH);
  float distanceCm = duration * 0.0343 / 2.0;

  if (client.publish("esp/sensor", String(distanceCm).c_str())) {
    Serial.println("Message successfully sent");
  } else {
    Serial.println("Failed to send message");
  }
}

void handleMQTTMessages() {
  client.loop();
}

void setup() {
  Serial.begin(9600);
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);

  connectToWiFi();
  client.setServer(mqttServer, mqttPort);
  connectToMQTT();
}

void loop() {
  measureDistanceAndPublish();
  handleMQTTMessages();
  delay(2000);
}

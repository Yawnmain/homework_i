#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const int ledPin1 = 5;
const int ledPin2 = 4;
const int ledPin3 = 0;
const int ledPin4 = 2;

const char* wifiNetwork = "Barya";
const char* wifiPass = "89834089400";
const char* mqttServer = "broker.emqx.io";
const int mqttPort = 1883;

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(9600);
  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  pinMode(ledPin4, OUTPUT);

  connectToWiFi();

  turnOffLeds();

  client.setServer(mqttServer, mqttPort);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}

void connectToWiFi() {
  Serial.println();
  WiFi.begin(wifiNetwork, wifiPass);
  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
    attempts++;
    if (attempts > 20) {
      Serial.println("Failed to connect to Wi-Fi");
      return;
    }
  }
  Serial.println("Connected to Wi-Fi: " + String(WiFi.SSID()));
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Connecting to MQTT...");
    if (client.connect("ESP8266Client")) {
      Serial.println("Connected to MQTT");
      Serial.println(client.subscribe("esp/sensor"));
    } else {
      Serial.print("Failed to connect, state: " + String(client.state()));
      Serial.println("...");
      delay(2000);
    }
  }
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.println("Received message in topic: " + String(topic));
  Serial.print("Received message: ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
  int distance = atoi((char*)payload);
  Serial.println("Distance: " + String(distance));
  distanceLeds(distance);
}

void distanceLeds(int distance) {
  if (distance <= 5) {
    turnOnAllLeds();
  } else if (distance <= 10 && distance >= 5) {
    turnOnFirstThreeLeds();
  } else if (distance <= 15 && distance >= 10) {
    turnOnFirstTwoLeds();
  } else if (distance <= 20 && distance >= 15) {
    turnOnFirstLed();
  } else if (distance >= 20) {
    turnOffLeds();
  }
}

void turnOnAllLeds() {
  digitalWrite(ledPin1, HIGH);
  digitalWrite(ledPin2, HIGH);
  digitalWrite(ledPin3, HIGH);
  digitalWrite(ledPin4, HIGH);
}

void turnOnFirstThreeLeds() {
  digitalWrite(ledPin1, HIGH);
  digitalWrite(ledPin2, HIGH);
  digitalWrite(ledPin3, HIGH);
  digitalWrite(ledPin4, LOW);
}

void turnOnFirstTwoLeds() {
  digitalWrite(ledPin1, HIGH);
  digitalWrite(ledPin2, HIGH);
  digitalWrite(ledPin3, LOW);
  digitalWrite(ledPin4, LOW);
}

void turnOnFirstLed() {
  digitalWrite(ledPin1, HIGH);
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin3, LOW);
  digitalWrite(ledPin4, LOW);
}

void turnOffLeds() {
  digitalWrite(ledPin1, LOW);
  digitalWrite(ledPin2, LOW);
  digitalWrite(ledPin3, LOW);
  digitalWrite(ledPin4, LOW);
}

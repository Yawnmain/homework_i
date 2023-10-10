const int LED_PIN = 13;
const int SENSOR_PIN = A0;

char currentCommand = ' ';
bool readSensor = false;
bool alarm = false;
bool autoControl = false;
bool sendSingleValue = false;

unsigned long previousMillis = 0;
const long alarmInterval = 300;
int lightLimit = 930;


void setup() {
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  long currentTime = millis();

  if (Serial.available() > 0) {
    currentCommand = Serial.read();
    processCommand(currentCommand);
  }

  if (alarm) {
    toggleLEDWithInterval();
  } else if (autoControl) {
    manageLEDBasedOnLight();
  }

  if (readSensor) {
    readAndSendSensorValue();
  }

  if (sendSingleValue) {
    readAndSendSensorValue();
    sendSingleValue = false;
  }
}

void processCommand(char command) {
  alarm = false;
  autoControl = false;
  readSensor = false;
  digitalWrite(LED_PIN, LOW);

  switch (command) {
    case 'p':
      readSensor = true;
      break;
    case 's':
      sendSingleValue = true;
      break;
	case 'y':
      digitalWrite(LED_PIN, HIGH);
      break;
    case 'n':
      digitalWrite(LED_PIN, LOW);
      break;
    case 'a':
      alarm = true;
      break;
    case 'c':
      autoControl = true;
      break;
    case 'r':
      digitalWrite(LED_PIN, LOW);
      break;
  }
}

void toggleLEDWithInterval() {
  unsigned long currentMillis = millis();
  if (currentMillis - previousMillis >= alarmInterval) {
    previousMillis = currentMillis;
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
  }
}

void manageLEDBasedOnLight() {
  int lightValue = analogRead(SENSOR_PIN);
  if (lightValue > lightLimit) {
    digitalWrite(LED_PIN, LOW);
  } else {
    digitalWrite(LED_PIN, HIGH);
  }
}

void readAndSendSensorValue() {
  int sensorValue = analogRead(SENSOR_PIN);
  Serial.print("Sensor value: ");
  Serial.println(sensorValue);
}
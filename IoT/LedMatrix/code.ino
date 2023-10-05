const int LED_PIN_1 = 9;
const int LED_PIN_2 = 8;
const int LED_PIN_3 = 7;
const int LED_PIN_4 = 6;

void activateLeds(int led1, int led2, int led3, int led4)
{
  digitalWrite(LED_PIN_1, led1);
  digitalWrite(LED_PIN_2, led2);
  digitalWrite(LED_PIN_3, led3);
  digitalWrite(LED_PIN_4, led4);
}

void deactivateLeds()
{
  activateLeds(0, 0, 0, 0);
}

int sequence1[][4]{
    {0, 0, 0, 0},    // 0
    {1, 0, 0, 1},    // 1
    {1, 0, 1, 0},    // 2
    {0, 1, 0, 1},    // 3
    {0, 1, 1, 0},    // 4
    {1, 0, 0, 0},    // 1,2
    {0, 1, 0, 0},    // 3,4
    {1, 1, 0, 1},    // 1,3
    {1, 1, 1, 0},    // 2,4
};

int sequence2[][2][4]{
    {{1, 0, 0, 1}, {0, 1, 1, 0}}, // 1,4
    {{1, 0, 1, 0}, {0, 1, 0, 1}}, // 2,3
    {{1, 0, 0, 0}, {0, 1, 0, 1}}, // 1,2,3
    {{1, 0, 1, 0}, {0, 1, 0, 0}}, // 2,3,4
    {{1, 0, 0, 1}, {0, 1, 0, 0}}, // 3,4,1
    {{1, 0, 0, 0}, {0, 1, 1, 0}}, // 4,1,2
    {{1, 0, 0, 0}, {0, 1, 0, 0}}, // 1,2,3,4
    {{0, 0, 0, 0}, {0, 0, 0, 0}}, // 
};

void lightSequence(int led1, int led2, int led3, int led4)
{
  deactivateLeds();
  activateLeds(led1, led2, led3, led4);
  delay(1000);
}

void lightDualSequence(int seq1Led1, int seq1Led2, int seq1Led3, int seq1Led4, int seq2Led1, int seq2Led2, int seq2Led3, int seq2Led4)
{
  for (int j = 0; j < 1000; j++)
  {
    activateLeds(seq1Led1, seq1Led2, seq1Led3, seq1Led4);
    delay(1);
    activateLeds(seq2Led1, seq2Led2, seq2Led3, seq2Led4);
    delay(1);
  }
}

void setup()
{
  pinMode(LED_PIN_1, OUTPUT);
  pinMode(LED_PIN_2, OUTPUT);
  pinMode(LED_PIN_3, OUTPUT);
  pinMode(LED_PIN_4, OUTPUT);
}

void loop()
{
  for (int i = 0; i < sizeof(sequence1) / sizeof(sequence1[0]); i++)
  {
    lightSequence(sequence1[i][0], sequence1[i][1], sequence1[i][2], sequence1[i][3]);
  }
  deactivateLeds();

  for (int i = 0; i < sizeof(sequence2) / sizeof(sequence2[0]); i++)
  {
    lightDualSequence(sequence2[i][0][0], sequence2[i][0][1], sequence2[i][0][2], sequence2[i][0][3], sequence2[i][1][0], sequence2[i][1][1], sequence2[i][1][2], sequence2[i][1][3]);
    deactivateLeds();
  }
}

volatile unsigned long t1 = 0;
volatile unsigned long t2 = 0;
unsigned long t3 = 0;
unsigned long t4 = 0;

volatile bool trig1 = false;
volatile bool trig2 = false;
bool trig3 = false;
bool trig4 = false;

volatile unsigned long t0 = 0;

const unsigned long WINDOW_US = 1000;

void mic1_ISR() {
  if (!trig1) {
    t1 = micros();
    trig1 = true;
    if (t0 == 0) t0 = t1;
  }
}

void mic2_ISR() {
  if (!trig2 && t0 != 0 && micros() - t0 < WINDOW_US) {
    t2 = micros();
    trig2 = true;
  }
}

void setup() {
  Serial.begin(115200);

  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(4, INPUT);
  pinMode(5, INPUT);

  attachInterrupt(digitalPinToInterrupt(2), mic1_ISR, RISING);
  attachInterrupt(digitalPinToInterrupt(3), mic2_ISR, RISING);
}

void resetEvent() {
  trig1 = false;
  trig2 = false;
  trig3 = false;
  trig4 = false;

  t1 = 0;
  t2 = 0;
  t3 = 0;
  t4 = 0;
  t0 = 0;
}

void loop() {
  // Fast polling for mic3
  if (!trig3 && t0 != 0 && micros() - t0 < WINDOW_US) {
    if (digitalRead(4) == HIGH) {
      t3 = micros();
      trig3 = true;
    }
  }

  // Fast polling for mic4
  if (!trig4 && t0 != 0 && micros() - t0 < WINDOW_US) {
    if (digitalRead(5) == HIGH) {
      t4 = micros();
      trig4 = true;
    }
  }

  // End of trigger window
  if (t0 != 0 && micros() - t0 > WINDOW_US) {

    // Ignore incomplete events
    if (t1 != 0 && t2 != 0 && t3 != 0 && t4 != 0) {
      Serial.print("t1: ");
      Serial.print(t1);
      Serial.print("  t2: ");
      Serial.print(t2);
      Serial.print("  t3: ");
      Serial.print(t3);
      Serial.print("  t4: ");
      Serial.println(t4);

      long dt12 = (long)t2 - (long)t1;
      long dt13 = (long)t3 - (long)t1;
      long dt14 = (long)t4 - (long)t1;
      long dt23 = (long)t3 - (long)t2;
      long dt24 = (long)t4 - (long)t2;
      long dt34 = (long)t4 - (long)t3;

      Serial.print("dt12: ");
      Serial.print(dt12);
      Serial.print(" us   dt13: ");
      Serial.print(dt13);
      Serial.print(" us   dt14: ");
      Serial.println(dt14);

      Serial.print("dt23: ");
      Serial.print(dt23);
      Serial.print(" us   dt24: ");
      Serial.print(dt24);
      Serial.print(" us   dt34: ");
      Serial.println(dt34);

      Serial.println("-------------------");
    }

    resetEvent();
  }
}

int led[] = {2, 3, 4, 5, 6, 7, 8, 13};
bool estados[] = {false, false, false, false, false, false, false, false};

void setup() {
  for (int i = 0; i < 8; i++) {
    pinMode(led[i], OUTPUT);
  }
  
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  if (Serial.available() > 0) {
    int idx_led = Serial.readString().toInt() - 1;
    estados[idx_led] = !estados[idx_led];
    digitalWrite(led[idx_led], estados[idx_led]);
    
    if (estados[idx_led]) {
      Serial.print("Led ");
      Serial.print(idx_led + 1);
      Serial.println(" encendido");
    } else {
      Serial.print("Led ");
      Serial.print(idx_led + 1);
      Serial.println(" apagado");
    }
  }
  
  delay(100);
}
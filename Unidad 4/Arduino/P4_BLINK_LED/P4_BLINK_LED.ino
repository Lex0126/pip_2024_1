
int led = 13;
int led2 = 4;

void setup() {
  pinMode(led, OUTPUT);
  pinMode(led2, OUTPUT);
  Serial.begin(9600); // Iniciar la comunicación serial a 9600 baudios
}

void loop() {
  digitalWrite(led, HIGH);
  Serial.println("Led 1 prendido");
  delay(1000);
  digitalWrite(led, LOW);
  Serial.println("Led 1 apagado");
  delay(1000);

  digitalWrite(led2, HIGH);
  Serial.println("Led 2 prendido");
  delay(1000);
  digitalWrite(led2, LOW);
  Serial.println("Led 2 apagado");
  delay(1000);
}

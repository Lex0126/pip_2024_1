
// arduino posee un led interno de pruebas en el pin digital 13
int led= 13;

int v;

void setup() {
  Serial.begin(9600);

  pinMode(led,OUTPUT);


}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led,HIGH);
  Serial.println("Led prendido");
  delay(1000);
  digitalWrite(led,LOW);
  Serial.println("Led Apagado");
  delay(1000);
}
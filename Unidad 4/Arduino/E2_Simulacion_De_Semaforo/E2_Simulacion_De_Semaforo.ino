// arduino posee un led interno de pruebas en el pin digital 13

int verde= 3;
int amarillo=5;
int rojo=7;


void setup() {
  Serial.begin(9600);

  pinMode(verde,OUTPUT);
  pinMode(amarillo,OUTPUT);
  pinMode(rojo,OUTPUT);


}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(verde,HIGH);
  delay(5000);
  digitalWrite(verde,LOW);
  delay(200);
  ////
  digitalWrite(verde,HIGH);
  delay(200);
  digitalWrite(verde,LOW);
  delay(200);
  ////
  digitalWrite(verde,HIGH);
  delay(200);
  digitalWrite(verde,LOW);
  delay(200);
  ////
  digitalWrite(amarillo,HIGH);
  delay(3000);
  digitalWrite(amarillo,LOW);
  delay(200);
  /////
  digitalWrite(amarillo,HIGH);
  delay(200);
  digitalWrite(amarillo,LOW);
  delay(200);
  ///////
  digitalWrite(amarillo,HIGH);
  delay(200);
  digitalWrite(amarillo,LOW);
  delay(200);
  ////////
  digitalWrite(rojo,HIGH);
  delay(5000);
  digitalWrite(rojo,LOW);
  delay(200);
  ///////
  digitalWrite(rojo,HIGH);
  delay(200);
  digitalWrite(rojo,LOW);
  delay(200);
  ///////
  digitalWrite(rojo,HIGH);
  delay(200);
  digitalWrite(rojo,LOW);
  delay(200);
}

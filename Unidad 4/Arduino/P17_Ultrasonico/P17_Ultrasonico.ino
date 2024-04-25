
int Pin_echo= 13;
int Pin_trig= 12;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(Pin_trig, OUTPUT);
  pinMode(Pin_echo,OUTPUT);


}
int pulso,cm;
void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(Pin_trig,LOW);
  delayMicroseconds(2);
  digitalWrite(Pin_trig,HIGH);
  delayMicroseconds(10);
  digitalWrite(Pin_trig,LOW);

  pulso = pulseIn(Pin_echo,HIGH);
  cm =pulso/29/2;

  Serial.println("Distancia:"+String(cm)+ "cm.");
  delay(100);


}

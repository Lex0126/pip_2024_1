int ENA = 3;
int Ini1 = 5;



void setup() {
  // put your setup code here, to run once:
  pinMode(Ini1 , OUTPUT);

///ENA no lleva pinmod
  Serial.begin(9600);
  Serial.setTimeout(10);


}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int v = Serial.readString().toInt();
      digitalWrite(Ini1,1);
      analogWrite(ENA,v);
  }
  delay(100);

}
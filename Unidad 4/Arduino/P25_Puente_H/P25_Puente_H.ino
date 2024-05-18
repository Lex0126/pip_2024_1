int ENA = 3;
int Ini1 = 5;
int Ini2 = 6;


void setup() {
  // put your setup code here, to run once:
  pinMode(Ini1 , OUTPUT);
  pinMode(Ini2,OUTPUT);
///ENA no lleva pinmod
  Serial.begin(9600);
  Serial.setTimeout(10);


}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int v = Serial.readString().toInt();
    if(v==0){
      Serial.println("Detenerse");
      digitalWrite(Ini1,0);
      digitalWrite(Ini2,0);
      analogWrite(ENA,0);
    }
    else if(v==1){
      Serial.println("Girar Izquierda");
      digitalWrite(Ini1,0);
      digitalWrite(Ini2,1);
      analogWrite(ENA,255);
    }
    else if(v ==2){
      Serial.println("Girar Derecha");
      digitalWrite(Ini1,1);
      digitalWrite(Ini2,0);
      analogWrite(ENA,255);
    }else{
      Serial.println("Moviemiento no valido");
    }
  }
  delay(100);

}

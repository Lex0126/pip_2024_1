int led = 2;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
   pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);


}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int v =Serial.readString().toInt();
    digitalWrite(led,v);
  }

}

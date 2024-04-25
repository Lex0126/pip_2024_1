int PIR=2;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(PIR,INPUT_PULLUP);

}
int val;
void loop() {
  // put your main code here, to run repeatedly:
  val=digitalRead(PIR);
  Serial.println("Senal:"+String(val));

  delay(100);


}

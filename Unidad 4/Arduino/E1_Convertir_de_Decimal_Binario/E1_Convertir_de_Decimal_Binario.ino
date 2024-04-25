
int led[]={2,3,4,5,6,7,8,9};
void setup() {
  // put your setup code here, to run once:
  for(int i=0; i<8; i++){
    pinMode(led[i],OUTPUT);

  }
  Serial.begin(9600);
  Serial.setTimeout(10);


}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    int num=Serial.readString().toInt();
    int digits[8] = {0,0,0,0,0,0,0,0};
    int contdigitos = 0;
    while(num>0){
      int temp = num%2;
      digits[contdigitos++]=temp;
      num=num/2;
    }
    for (int i =0; i<8;i++){
      Serial.print(String(digits[i])+"A");
      digitalWrite(led[i],digits[i]);
    }
  }

}

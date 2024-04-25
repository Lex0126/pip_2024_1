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
  for(int num =0; num<=255; num++){
    int digits[8] = {0,0,0,0,0,0,0,0};
    int contdigitos = 0;
    int tempNum = num;
    while(tempNum>0){
      int temp = tempNum%2;
      digits[contdigitos++]=temp;
      tempNum=tempNum/2;
    }
    for (int i =0; i<8;i++){
      Serial.print(String(digits[i])+"A");
      digitalWrite(led[i],digits[i]);
    }
    delay(2000);
  }

}

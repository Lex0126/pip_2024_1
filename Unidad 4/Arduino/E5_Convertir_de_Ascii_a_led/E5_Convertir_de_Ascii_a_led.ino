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
    String num=Serial.readString();
    int ascii=num.charAt(0);

    int digits[8] = {0,0,0,0,0,0,0,0};
    int contdigitos = 0;
    while(ascii>0){
      int temp = ascii%2;
      digits[contdigitos++]=temp;
      ascii=ascii/2;
    }
    for (int i =0; i<8;i++){
      Serial.print(String(digits[i])+"A");
      digitalWrite(led[i],digits[i]);
    }
  }

}
int led[] = {2, 3, 4, 5, 6, 7, 8, 9}; 
int nivelLED = 0; 

void setup() {
  for(int i = 0; i < 8; i++){
    pinMode(led[i], OUTPUT); 
    digitalWrite(led[i], LOW); 
  }
  
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  if(Serial.available()){
    nivelLED = Serial.readString().toInt(); 
    
    if(nivelLED >= 0 && nivelLED <= 8){
      for(int i = 0; i < 8; i++){
        if(i < nivelLED){
          digitalWrite(led[i], HIGH); 
        } else {
          digitalWrite(led[i], LOW); 
        }
      }
    }
  }
}


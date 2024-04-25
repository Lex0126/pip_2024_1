void setup() {
  // put your setup code here, to run once:
  //modulouart ...modulo asicrono universal de transmision y recpcion de datos
  Serial.begin(9600); //inicializa la comunicacion serial...
  //valores a los que se comunica arduino con otros dispositivos..

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println(" hola! :D  :3");
  delay(500);/// milesecs

}

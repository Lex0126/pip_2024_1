//voltaje de referencia: 5v
//bits de resolucion:  10bits de resolucion... 1024 valores posibles

//cada valor que les da el arduino se distancia uno del otro  en 4.8mV


// la senal analogica del arduino funciona con los pines analogicos(0,1,2,3,4,5)

int potenciometro = A0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  //pinmode no se utiliza para pines analogicos...

  //nota: un pin analogico solo es de entrada...


}
int valor;
void loop() {
  // put your main code here, to run repeatedly:

  valor= analogRead(potenciometro);
  Serial.println(valor);
  delay(100);

}

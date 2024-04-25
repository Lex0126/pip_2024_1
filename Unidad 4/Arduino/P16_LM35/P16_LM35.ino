

int lm35 =A0;

// ADC = conversor analogo digital
//convierte una senal analogica a una senal digital
// voltaje de referencia :5v
//bits de resolucion :10 .... 2'10 = 1024 valores posibles
// 0v = 0
// 5v = 1023

// 5/1023 = .0048volts = 4.8mv

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

}
int valor;
void loop() {
  // put your main code here, to run repeatedly:

  valor = analogRead(lm35);
  Serial.print("Valor leido:"+ String(valor));

  valor =(5.0 *valor *100.01)/ 1023.0;

  Serial.println("Temp:"+ String(valor));

  delay(100);


}

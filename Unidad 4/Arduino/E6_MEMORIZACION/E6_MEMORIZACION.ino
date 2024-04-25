int led[] = {2, 3, 4, 5, 6, 7, 8, 9};
String secuencia = "";
int indice = 0;

void setup() {
  for (int i = 0; i < 8; i++) {
    pinMode(led[i], OUTPUT);
    digitalWrite(led[i], LOW);
  }

  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  if (Serial.available()) {
    secuencia = Serial.readString(); // Leemos la secuencia
    indice = 0; // Reiniciar el índice para comenzar la secuencia desde el principio
  }

  // Verificamos si la secuencia metida tiene datos
  if (secuencia.length() > 0) {
    // Encender el LED correspondiente y luego apagarlo
    int ledIndex = secuencia.charAt(indice) - '0' - 1; // Convertir el caracter a un índice de LED un ejemplo es que tenemos un 0 en ascci y restamos al indice nos queda el numero real y ese numero real lo restamos con menos 1 para tener la posicion en 0 como es en C
    digitalWrite(led[ledIndex], HIGH);
    delay(1000); 
    digitalWrite(led[ledIndex], LOW);
    Serial.print(secuencia);

    // Incrementar el índice para pasar al siguiente LED en la secuencia
    indice++;
    if (indice >= secuencia.length()) {
      indice = 0; // Si llegamos al final de la secuencia, volver al principio

    }
  }
}
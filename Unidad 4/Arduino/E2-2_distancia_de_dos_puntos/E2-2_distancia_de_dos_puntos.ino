int estado = 0;
float x1, y1;
float x2, y2;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  if (estado == 0) {
    Serial.println("Ingrese la coordenada x del primer punto:");
    estado++;
  } else if (estado == 1) {
    if (Serial.available() > 0) {
      x1 = Serial.readString().toFloat();
      estado++;
    }
  } else if (estado == 2) {
    Serial.println("Ingrese la coordenada y del primer punto:");
    estado++;
  } else if (estado == 3) {
    if (Serial.available() > 0) {
      y1 = Serial.readString().toFloat();
      estado++;
    }
  } else if (estado == 4) {
    Serial.println("Ingrese la coordenada x del segundo punto:");
    estado++;
  } else if (estado == 5) {
    if (Serial.available() > 0) {
      x2 = Serial.readString().toFloat();
      estado++;
    }
  } else if (estado == 6) {
    Serial.println("Ingrese la coordenada y del segundo punto:");
    estado++;
  } else if (estado == 7) {
    if (Serial.available() > 0) {
      y2 = Serial.readString().toFloat();
      estado++;
      float distancia = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));
      Serial.println("La distancia entre los dos puntos es: " + String(distancia));
      Serial.println("¿Desea calcular otra distancia entre dos puntos? (1=Sí, 0=No)");
    }
  } else if (estado == 8) {
    if (Serial.available() > 0) {
      int v = Serial.readString().toInt();
      if (v == 1) {
        estado = 0;
      } else {
        estado = 9;
      }
    }
  } else if (estado == 9) {
    Serial.println("Acabando el programa");
  }
  delay(100);
}

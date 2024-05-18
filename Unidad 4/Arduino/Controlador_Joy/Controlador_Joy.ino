#define VRX_PIN A0 // Arduino pin connected to VRX pin
#define VRY_PIN A1 // Arduino pin connected to VRY pin
#define SW_PIN 2 
#define LED_PIN_1 4  // Pin connected to LED 1
#define LED_PIN_2 5   // Pin connected to the switch (if you have one)

int xValue = 0; // To store value of the X axis
int yValue = 0;
int vida =2; // To store value of the Y axis

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Read analog X and Y values
  xValue = analogRead(VRX_PIN);
  yValue = analogRead(VRY_PIN);

  // Send the values to the serial port
  Serial.print(xValue);
  Serial.print(",");
  Serial.println(yValue);
  if (vida == 2) {
    digitalWrite(LED_PIN_1, HIGH);
    digitalWrite(LED_PIN_2, HIGH);
  } 
 if (vida == 1) {
    digitalWrite(LED_PIN_1, HIGH);
    digitalWrite(LED_PIN_2, LOW);
  }
  if (vida == 0) {
    digitalWrite(LED_PIN_1, LOW);
    digitalWrite(LED_PIN_2, LOW);
  }  
  
  

  

  delay(200); // Adjust the delay as needed
}

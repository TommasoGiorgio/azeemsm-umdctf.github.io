const int bellPin = 6;
void setup() {
  pinMode(bellPin, INPUT);
  Serial.begin(9600);

}

void loop() {
  int bellState = digitalRead(bellPin);
  if(bellPin){
    Serial.println("ring!");
  }

}

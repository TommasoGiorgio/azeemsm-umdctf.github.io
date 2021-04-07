const int bellPin = 5;
void setup() {
  // put your setup code here, to run once:
  pinMode(bellPin, INPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  int bellState = digitalRead(bellPin);
  if(bellPin){
    Serial.println("ring!");
  }

}

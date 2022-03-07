byte i = 0;

void setup() {
  
  Serial.begin(9600);

}

void loop() {
  
  if(i >= 100){
  i = 0;
  }

  Serial.println(i);
  delay(50);
  i++;
  
}

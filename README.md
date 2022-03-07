# MajorProjectEEE

The Idea is to make an electrical enegry monitoring system and graphically represent the data.

Also implimenting a method to detect, Identify fault on line if any with a protection mechanism.


```ino

int i = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(i <10){
  Serial.println(i);
  i++;
  delay(100);}
  else{ 
    while(i>0)
    {
      Serial.println(i);
      i--;
      delay(100);
      }
   }
}

```


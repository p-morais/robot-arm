#include <Servo.h>

Servo elbow;
void setup() 
{
  Serial.begin(9600); 
  Serial.println("Ready"); 
  Serial.setTimeout(50);
  elbow.attach(13);
}

void loop() 
{
  if (Serial.available())
  { 
    String str = Serial.readString(); // read the incoming data
    Serial.println(str); 

    int pos = str.toInt();
    elbow.write(pos);
    delay(15); // delay for 1/10 of a second
  }
}

#include <Servo.h>
int echo = 12, trig = 13;
int greenLed = 11, redLed = 8;
Servo servo1, servo2;
float dst(){
  digitalWrite(trig, 0);
  delayMicroseconds(5);
  digitalWrite(trig, 1);
  delayMicroseconds(10);
  digitalWrite(trig, 0);
  return pulseIn(echo, 1);
}
void setup() {
  Serial.begin(9600);
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(redLed, OUTPUT);
  servo1.attach(10);
  servo2.attach(9);
  Serial.println(-1);
}

void loop() {
  Serial.println(-1);
  float x = dst();
  float d = x / 58.2; //centimetre
  Serial.println(d);
  if(d <= 15){
    delay(1000);
    Serial.println(0);
    delay(3000);
    int read = Serial.read();
    if(read == '2'){
      servo1.write(1);
      servo2.write(179);
      digitalWrite(redLed, 1);
      digitalWrite(greenLed, 0);
    }
    else{
      servo1.write(179);
      servo2.write(1);
      digitalWrite(greenLed, 1);
      digitalWrite(redLed, 0);
    }
    Serial.println(-1);
    delay(1500);
    servo1.write(90);
    servo2.write(90);
  }
  delay(2000);
}

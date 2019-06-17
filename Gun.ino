#include <Servo.h>
Servo gun;
Servo x;
char serialData;
int pin = 10;

void setup() {
Serial.begin(9600);
}

void loop() {
  gun.attach(pin);
  if (Serial.available() > 0){
  serialData = Serial.read();
  Serial.println(serialData);

  if (serialData == '1') {
    gun.write(88);
    //gun.write(86);
    
  }
  else if (serialData == '0') {
    gun.write(88);
    
   
    x.attach(11);
    x.write(180);
    delay(150);
    x.detach();
    delay(10);
    x.attach(11);
    x.write(0);
    delay(150);
    x.detach();
    delay(10);
    
  }


  else if (serialData == '3') {
    gun.write(89);
    
    //delay(50);
    //gun.write(88); 
  }
  else if (serialData == '2') {
    gun.write(86);
    
    //delay(30);
    //gun.write(88); 
  }
  }
}

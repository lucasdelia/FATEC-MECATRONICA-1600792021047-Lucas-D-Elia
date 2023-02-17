#include <Servo.h>

servo servo1;

int servo_pin = 3,

void setup(){
    pinMode(servo_pin,OUTPUT);

}

void loop(){

    for(int i=0; i>120; i++){
        servo.write(i);
        delay(500)
    }
}

#include <avr/io.h>
#include <Arduino.h>
#include <Wire.h>
#include <SoftwareSerial.h>
//Carga los archivos .h y .cpp para los sensores
#include "src/MeSingleLineFollower.h"
#include "src/MeCollisionSensor.h"
#include "src/MeBarrierSensor.h"
#include "src/MeNewRGBLed.h"
#include <MeMegaPi.h>
#include <Arduino_FreeRTOS.h>


MeBarrierSensor barrier_60(60);
MeBarrierSensor barrier_61(61);
MeBarrierSensor barrier_62(62);
MeCollisionSensor collision_65(65); 
MeCollisionSensor collision_66(66); 

//TaskHandle_t vTaskHanldleMBot; 
//TaskHandle_t vTaskHanldleSensores;
  
void setup() {

  //DDRB = 0XFF;
  UCSR2B = (1<<TXEN2) | (1<<RXEN2);   //INITIALIZE USART0
  UCSR2C = (1<<UCSZ21) | (1<<UCSZ20);
  
  UBRR2L = 103; 
  
   xTaskCreate(vTaskMbot,"Mbot TASK",100,NULL,2,NULL);
   xTaskCreate(vTaskSensores,"Sensor TASK",100,NULL,1,NULL); 

  
  unsigned char ch;
  
  DDRB = 0xFF; //declarar puertos como output para todos los motores
  DDRC = 0xFF;
  DDRH = 0xFF;
  DDRG = 0xFF;
  
  TCCR1A = 0b10100001;
  TCCR4A = 0b00101001;
  TCCR1B = 0b00001100;
  TCCR4B = 0b00001100;
  
  int n = 51; //se setea la velocidad de los motores al 20%
  
  OCR1A = n;
  OCR1B = n;
  OCR4C = n;
  OCR4B = n;
  
  //PORTB = 0b01100000; // pines de enable para motores (5,6)
  PORTC = 0b00010101; // pines para motores (0, 2,4)
  //PORTH = 0b00110000;  //pines para enable de motores (4, 5)
  PORTG = 0b00000001; // pin para motor 3

}

void forward(){
  PORTC = 0b00101010; // pines para motores (0, 2,4)
  PORTG = 0b00000010; // pin para motor 3
}

void backward(){
  PORTC = 0b00010101;
  PORTG = 0b00000001;
}
void left(){
  PORTC = 0b00010110; // pines para motores (0, 2,4)
  PORTG = 0b00000010; // pin para motor 3
}

void right(){
  PORTC = 0b00101001; // pines para motores (0, 2,4)
  PORTG = 0b00000001; // pin para motor 3
}

void stopp(){
  PORTC = 0b00000000; // pines para motores (0, 2,4)
  PORTG = 0b00000000; // pin para motor 3
  
}

void barrierB(){
  int barrier;  
  if(barrier_60.isBarried() || barrier_61.isBarried()){ //Condicional para parar los motores si el sensor detecta un obstaculo
     barrier = 1; 
     while (!(UCSR2A &(1<< UDRE2)));
     UDR2 = barrier;   
  }
  else{
    barrier = 2; 
     while (!(UCSR2A &(1<< UDRE2)));
     UDR2 = barrier;   
  }
}

void collision(){
  int coll; 
  if (collision_65.isCollision() || collision_66.isCollision()){
    coll = 3; 
    while (!(UCSR2A &(1<< UDRE2)));
    UDR2 = coll;   
  }
  else{
    coll = 4; 
    while (!(UCSR2A &(1<< UDRE2)));
    UDR2 = coll;   
  } 
}


void vTaskMbot (void * pvParameters){
  while (1){

  while (!(UCSR2A&(1<<RXC2)));// WAIT UNTIL NEW DATA
  char ch = UDR2;
  //UDR0 = ch;

    if (ch == 'f') //elementos enviados al serial 
    {
      forward(); 
    }
    if (ch == 's') //parar
    {
      stopp();
    }
    if (ch == 'b') //atras
    {
      backward();
    }
    if (ch == 'r') //derecha
    {
      right();
    }
    if (ch == 'l') //izquierda
    {
      left();
    }
    vTaskDelay(100/portTICK_PERIOD_MS); 
  }
}

void vTaskSensores (void * pvParameters){
  while(1){
    barrierB(); 
    collision(); 
    vTaskDelay(100/portTICK_PERIOD_MS); 
  }
}


void loop() {
  }

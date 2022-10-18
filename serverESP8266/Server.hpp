#include "Kannbal.hpp"
ESP8266WebServer server(80);
int digital_id;
String temp_id;

bool defineState(String quey_state){
  if(quey_state == "on") return false; else return true;
}

int defineDigitalValue(String query_value){
  return query_value.toInt();
}

void setDigitalValue(){
  SingleActuator single_actuator = SingleActuator(digital_id);
  
  if(server.arg(String("status")).length() > 0){
    Serial.println("Set Bool State");
    bool state = defineState(server.arg(String("status")));
    single_actuator.changeState(state);
  }
  if(server.arg(String("value")).length() > 0){
    Serial.println("Set PWM Value");
    int value = defineDigitalValue(server.arg(String("value")));
    Serial.println(value);
    single_actuator.pwmValue(value);
  }
}

void setDigitalGenericValue(){
   temp_id = server.arg(String("id"));
   digital_id = temp_id.toInt();
   Serial.println(digital_id);
   setDigitalValue();
   server.send(200, "text/plain", String("OK"));
}

void setServo(){
  // TODO  
}

void setRGB(){
  // TODO
}

void getAnalogicSensor(){
  TemperatureSensor sensor = TemperatureSensor(A0);
   float temp = sensor.getValue();
   server.send(200, "text/plain", String(temp));
}

// Funcion que se ejecutara en la URI '/'
void handleRoot() 
{
   server.send(200, "text/plain", "Hola mundo!");
}

void handleNotFound() 
{
   server.send(404, "text/plain", "Not found");
}

void InitServer()
{
    /* query params
      id= numbre or String
      status = ON | OFF
      value =  0-255
    */
   // Ruteo para '/'
   server.on("/", handleRoot);
 
   // Definimos dos routeos
   server.on("/generic-digital", HTTP_POST, setDigitalGenericValue);
   server.on("/rgb", HTTP_POST, setRGB);
   server.on("/servo", HTTP_POST, setServo);
   server.on("/analogic-sensor", HTTP_GET, getAnalogicSensor);
 
   server.onNotFound(handleNotFound);
 
   server.begin();
   Serial.println("HTTP server started");
}

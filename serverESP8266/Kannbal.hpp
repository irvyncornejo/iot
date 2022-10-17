
class SingleActuator{
  public:
    int pin;
  SingleActuator(int number){
    pin=number;
    pinMode(pin, OUTPUT);
  }
  void changeState(bool ref){
    digitalWrite(pin, ref);
  }
  void pwmValue(int value){
    analogWrite(pin, value);
  }
};

class TemperatureSensor{
  public:
    int pin;
  TemperatureSensor(int number){
    pin=number;
  }
  float getValue(){
    int valuePin = analogRead(pin);
    float tempC = (3.3 * valuePin * 100.0)/1024;
    return tempC;
  }
};

class Motor{
  public:
    int pinA;
    int pinB;
  Motor(int poloA, int poloB){
    pinA=poloA;
    pinB=poloB;
    pinMode(pinA, OUTPUT);
    pinMode(pinB, OUTPUT);
  }
  void toTurn(bool valueA, bool valueB){
    if(valueA != valueB){
      digitalWrite(pinA, valueA);
      digitalWrite(pinB, valueB);
    }
  }
  void toStop(){
    digitalWrite(pinA, LOW);
    digitalWrite(pinB, LOW);
  }
};

int led=2;

void setup(){
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);
}

void loop(){
    if(Serial.available()>0){
        char var=Serial.read();

        if(var=='A'){
             digitalWrite(LED_BUILTIN, HIGH);
        }
        if(var=='B'){
             digitalWrite(LED_BUILTIN, LOW);
        }

    }
  
}

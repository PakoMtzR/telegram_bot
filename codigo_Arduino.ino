const int pinTimbre = 2;
const int pinGas= 4;

String info_Timbre = "";
String info_Gas = "";
String mensaje = "";


void setup() {
    Serial.begin(9600);
    pinMode(pinGas, INPUT);
    pinMode(pinTimbre, INPUT); 
}

void loop() {
    if ((digitalRead(pinTimbre) == 1) || (digitalRead(pinGas) == 1))
    {
        info_Timbre += digitalRead(pinTimbre);
        info_Gas += digitalRead(pinGas);
        mensaje = 'T' + info_Timbre + 'G' + info_Gas; 
        Serial.println(mensaje);
    }
    info_Timbre = "";
    info_Gas = "";
    delay(200);
}
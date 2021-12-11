// Deninimos los pines
const int pinTimbre = 2;
const int pinGas= 4;

// Declaramos las variables donde guardaremos toda la informacion que recolectemos
String info_Timbre = "";
String info_Gas = "";
String mensaje = "";

// Configuracion inicial
void setup() {
    Serial.begin(9600);
    pinMode(pinGas, INPUT);
    pinMode(pinTimbre, INPUT); 
}

void loop() {
    
    // Se comprueban si tanto el timbre y el sensor han detectado algo para poder mandar informacion en el monitor serial
    if ((digitalRead(pinTimbre) == 1) || (digitalRead(pinGas) == 1))
    {
        info_Timbre += digitalRead(pinTimbre);
        info_Gas += digitalRead(pinGas);
        mensaje = 'T' + info_Timbre + 'G' + info_Gas; 
        Serial.println(mensaje);
    }
    
    // Limpiamos nuestras variables
    info_Timbre = "";
    info_Gas = "";

    // Pausamos un momento el programa para que no tenga sobre carga de trabajo
    delay(200);
}
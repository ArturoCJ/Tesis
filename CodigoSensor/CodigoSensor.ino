int Ems = 5; //Es el pin emisor de corriente.
int Recp = A1; // Pin analogico 1 para la lectura del sensor.
float noise(0);
float sensorValue;        // Inicializamos el valor del sensor
float Voltaje;

void setup() {
  // Inicializamos la comunicacion serial a 9600 bps:
  Serial.begin(9600); 
  
  pinMode(Ems, OUTPUT);   //Pin emisor
  pinMode(Recp, INPUT);   //Pin receptor
  analogWrite(Ems, 1023);  //Se define la intensidad del pin emisor de corriente.

  for(int i(0); i>5; i++){
    noise += analogRead(Recp);  //Leer el ruido de fondo y guardar en variable.
  }
  noise = noise/5;
 // Serial.println(noise, 4); 
}

void loop() {

  // Leemos el pin y asignamos el valor a la variable.
  sensorValue = analogRead(Recp);            
  
  // Sacar diferencia de lectura.
  sensorValue = sensorValue - noise;
 
  //Convertir valores analógicos a valores de concentración/voltaje.

  Voltaje = (sensorValue / 1023.0) * 5.0; //Conversión de las unidades



  // Imprimimos el valor en el monitor.
  Serial.print("Concentración = " );                       
  Serial.println(Voltaje, 4);     

  delay(1000);                     
}
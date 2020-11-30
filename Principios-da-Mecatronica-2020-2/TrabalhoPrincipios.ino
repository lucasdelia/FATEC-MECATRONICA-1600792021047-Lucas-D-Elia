int pinLedR = 3;
int pinLedG = 5;
int pinLedB = 6;
int pinLDR = 0;
int valorLDR = 0;  
 
void setup()
{
  pinMode(pinLedR, OUTPUT);
  pinMode(pinLedG, OUTPUT);
  pinMode(pinLedB, OUTPUT);
  
  Serial.begin(9600);
}
 
void loop()
{
  digitalWrite(pinLedR, LOW);
  digitalWrite(pinLedG, LOW);
  digitalWrite(pinLedB, LOW);

  valorLDR= analogRead(pinLDR);
  
  Serial.println(valorLDR);
 
  if(valorLDR > 223){
  analogWrite(pinLedR, 51);
  delay(500);
  analogWrite(pinLedR, 0);
  delay(500);
  analogWrite(pinLedG, 51);
  delay(500);
  analogWrite(pinLedG, 0);
  delay(500);
  analogWrite(pinLedB, 51);
  delay(500);
  analogWrite(pinLedB, 0);
  delay(500);
  }
  if(valorLDR > 512){
  analogWrite(pinLedR, 102);
  delay(500);
  analogWrite(pinLedR, 0);
  delay(500);
  analogWrite(pinLedG, 102);
  delay(500);
  analogWrite(pinLedG, 0);
  delay(500);
  analogWrite(pinLedB,102);
  delay(500);
  analogWrite(pinLedB, 0);
  delay(500);
  }
  if(valorLDR > 768){
  analogWrite(pinLedR, 153);
  delay(500);
  analogWrite(pinLedR, 0);
  delay(500);
  analogWrite(pinLedG, 153);
  delay(500);
  analogWrite(pinLedG, 0);
  delay(500);
  analogWrite(pinLedB, 153);
  delay(500);
  analogWrite(pinLedB, 0);
  delay(500);
  }
  if(valorLDR > 845){
  analogWrite(pinLedR, 204);
  delay(500);
  analogWrite(pinLedR, 0);
  delay(500);
  analogWrite(pinLedG, 204);
  delay(500);
  analogWrite(pinLedG, 0);
  delay(500);
  analogWrite(pinLedB, 204);
  delay(500);
  analogWrite(pinLedB, 0);
  delay(500);
  }
  if(valorLDR > 956){
  analogWrite(pinLedR, 255);
  delay(100);
  analogWrite(pinLedR, 0);
  delay(100);
  analogWrite(pinLedG, 255);
  delay(100);
  analogWrite(pinLedG, 0);
  delay(100);
  analogWrite(pinLedB, 255);
  delay(100);
  analogWrite(pinLedB, 0);
  delay(100);}
}
  

// sketch para testar o driver TxRx do shield multisensor do Arduino
int LedRed = 12;
int LedBlue = 13;
int Sw1 = 2;
int Sw2 = 3;
int Pb;
int val;
char caractere;
String texto = "";

void setup() {
  Serial.begin(9600);
  pinMode(LedRed, OUTPUT);// configura o led12 como saída
  pinMode(LedBlue, OUTPUT);// configura o led13 como saída
  pinMode(Sw1, INPUT);// configura a porta 2 como entrada com resistor pull-up interno
  pinMode(Sw2, INPUT);// configura a porta 3 como entrada com resistor pull-up interno
}

void loop() {
  texto = "";                          // o que acontece se eu comentar essa linha?
  while (Serial.available() > 0) {     // enquanto tiver alguma coisa disponível na serial...
    caractere = Serial.read();         // ... faz-se a leitura e coloca-se na variável caractere
    if (caractere != '\r') {           // enquanto o caractere for diferente de '\r' (ou enter), pula a linha. Está identificando como sendo o final da mensagem
      texto.concat(caractere);          // concatena os caracteres na variável "texto"
    }
    else {
      if (texto == "LigaVermelho") {
        digitalWrite(LedRed, HIGH);
        Serial.println("o led vermelho foi acionado");
      }
      if (texto == "LigaAzul") {
        digitalWrite(LedBlue, HIGH);
        Serial.println("o led azul foi acionado");
      }
      if (texto == "DesligaVermelho") {
        digitalWrite(LedRed, LOW);
        Serial.println("o led vermelho foi desligado");
      }
      if (texto == "DesligaAzul") {
        digitalWrite(LedBlue, LOW);
        Serial.println("o led azul foi desligado");
      }
      if (texto == "LerA0") {//potenciômetro
        val = analogRead(A0);
        Serial.println(val);
      }
      if (texto == "LerA1") {// LDR
        val = analogRead(A1);
        Serial.println(val);
      }
      if (texto == "Entrada1") {
        Pb = digitalRead(Sw1);
        if (Pb == 1) {
          Serial.println("a chave 1 nao foi pressionada");
        }
        else {
          Serial.println("a chave 1 foi pressionada");
        }
      }
      if (texto == "Entrada2") {
        Pb = digitalRead(Sw2);
        if (Pb == 1) {
          Serial.println("a chave 2 nao foi pressionada");
        }
        else {
          Serial.println("a chave 2 foi pressionada");
        }
      }
    }
    delay(10);
  }
}

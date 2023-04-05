// sketch para testar o driver TxRx do shield multisensor do Arduino
int LedRed = 12;
int LedBlue = 13;
int Sw1 = 2;
int Sw2 = 3;
int Pb;
int val;
char caractere;
String texto = "";
// Definindo os pinos do buzzer e do botão
const int buzzer = 5;
// Definindo as notas musicais
const int c = 261;
const int d = 294;
const int e = 329;
const int f = 349;
const int g = 391;
const int gS = 415;
const int a = 440;
const int aS = 455;
const int b = 466;
const int cH = 523;
const int cSH = 554;
const int dH = 587;
const int dSH = 622;
const int eH = 659;
const int fH = 698;
const int fSH = 740;
const int gH = 784;
const int gSH = 830;
const int aH = 880;

// Definindo os tempos das notas musicais
const int tempoNota = 100;
const int tempoPausa = 2;

// Definindo a música do tema do jogo Mario
int melody[] = {eH, eH, 0, eH, 0, cH, eH, 0, gH, 0, 0, 0, g, 0, 0, 0, cH, 0, 0, g, 0, 0, e, 0, 0, aH, 0, b, 0, a, 0, 0, g, eH, g, a, 0, f, g, 0, eH, 0, cH, d, b, 0, 0, cH, 0, 0, g, 0, 0, e, 0, 0, aH, 0, b, 0, a, 0, 0, g, eH, g, a, 0, f, g, 0, eH, 0, cH, d, b, 0, 0, cH, 0, 0, g, 0, 0, e, 0, 0, aH, 0, b, 0, a, 0, 0, g, eH, g, a, 0, f, g, 0, eH, 0, cH, d, b, 0, 0, cH, 0, 0, g, 0, 0, e, 0, 0, aH, 0, b, 0, a, 0, 0, g, eH, g, a, 0, f, g, 0, eH, 0, cH, d, b, 0, 0, cH, 0, 0, g, 0, 0, e, 0, 0, aH, 0, b, 0, a, 0, 0, g, eH, g, a, 0, f, g, 0, eH, 0, cH, d, b, 0, 0, cH, 0, 0, g, 0, 0, e, 0, 0, aH, 0, b, 0, a, 0, 0, g, eH, g, a,};
// Definindo a função para tocar uma nota musical
void playNota(int nota, int tempo) {
int duracao = tempoNota / tempo;
tone(buzzer, nota, duracao);
delay(duracao * tempoPausa);
noTone(buzzer);
}

// Definindo a função para tocar a música
void playMelody() {
for (int i = 0; i < sizeof(melody)/sizeof(melody[0]); i++) {
if (melody[i] == 0) {
delay(tempoNota);
} else {
playNota(melody[i], 1);
}
}
}

// Definindo a função para aguardar o botão ser pressionado
void waitForButton() {
while (!digitalRead(Sw1)) {
// Espera o switch ser pressionado
}
delay(100);
}

void setup() {
  Serial.begin(9600);
  pinMode(LedRed, OUTPUT);// configura o led12 como saída
  pinMode(LedBlue, OUTPUT);// configura o led13 como saída
  pinMode(Sw1, INPUT);// configura a porta 2 como entrada com resistor pull-up interno
  pinMode(Sw2, INPUT);// configura a porta 3 como entrada com resistor pull-up interno
  pinMode(buzzer, OUTPUT);
  pinMode(Sw1, INPUT_PULLUP);
}

void loop() {
  int volume = 255;
  tone(buzzer, volume);
  analogWrite(buzzer, volume);
  waitForButton(); // Aguarda o botão ser pressionado
  playMelody(); // Toca a música
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
      if (texto == "toca mario") {
        playMelody();
        Serial.println("A música de Mario está tocando");
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

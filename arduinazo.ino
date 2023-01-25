

//Motor 1
int ENA = 8;
int IN1 = 2;
int IN2 = 3;

//Motor 2
int ENB = 9;
int IN3 = 4;
int IN4 = 5;

//Motor 3
int ENC = 10; 
int IN5 = 6;
int IN6 = 7;


void setup() 
{
 pinMode (ENA, OUTPUT);
 pinMode (ENB, OUTPUT);
 pinMode (ENC, OUTPUT);
 pinMode (IN1, OUTPUT);
 pinMode (IN2, OUTPUT);
 pinMode (IN3, OUTPUT);
 pinMode (IN4, OUTPUT);
 pinMode (IN5, OUTPUT);
 pinMode (IN6, OUTPUT) ;
  
}

void Tensar ()
{
digitalWrite (IN1, HIGH);
digitalWrite (IN2,LOW);
analogWrite (ENA, 80);

digitalWrite (IN3, HIGH);
digitalWrite (IN4,LOW);
analogWrite (ENB, 80);

digitalWrite (IN5, HIGH);
digitalWrite (IN6,LOW);
analogWrite (ENC, 80);
}

void Destensar ()
{
digitalWrite (IN1, LOW);
digitalWrite (IN2,HIGH);
analogWrite (ENA, 80);

digitalWrite (IN3, LOW);
digitalWrite (IN4,HIGH);
analogWrite (ENB, 80);

digitalWrite (IN5, LOW);
digitalWrite (IN6,HIGH);
analogWrite (ENC, 80);
}

void Parar ()
{
digitalWrite (IN1, LOW);
digitalWrite (IN2,LOW);
analogWrite (ENA, 0);

digitalWrite (IN3, LOW);
digitalWrite (IN4,LOW);
analogWrite (ENB, 0);

digitalWrite (IN5, LOW);
digitalWrite (IN6,LOW);
analogWrite (ENC, 0);
}


void loop() 
{
  Tensar();
  delay (2500);
  Destensar();
  delay(2500);
  
 
}

#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT.h>

#define DHTPIN PA1
#define DHTTYPE DHT11

LiquidCrystal_I2C lcd(0x27, 16, 2);
DHT dht(DHTPIN, DHTTYPE);
byte degree_symbol[8] =
{
0b00111,
0b00101,
0b00111,
0b00000,
0b00000,
0b00000,
0b00000,
0b00000
};

void setup()
{

lcd.begin();
dht.begin();
lcd.backlight();
lcd.setCursor(0,0);
lcd.print(“Electronics Hub”);
lcd.setCursor(0,1);
lcd.print(“DHT11 with STM32”);
delay(2000);
lcd.clear();
lcd.setCursor(0,0);
lcd.print(“Temperature = “);
lcd.setCursor(0,1);
lcd.print(“Humidity = “);
lcd.createChar(0, degree_symbol);
lcd.setCursor(12,0);
lcd.write(0);
lcd.print(“C”);
lcd.setCursor(14,1);
lcd.print(“%”);
}

void loop()
{
float hum = dht.readHumidity();
float tem = dht.readTemperature();
lcd.setCursor(7,0);
lcd.print(tem);
lcd.setCursor(8,1);
lcd.print(hum);
}
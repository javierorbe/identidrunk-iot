from raspi.lcd import LCD


if __name__=="__main__":
    lcd = LCD()
    lcd.setRGB(0, 100, 0)
    lcd.setText("Hello world\nThis is an LCD test")

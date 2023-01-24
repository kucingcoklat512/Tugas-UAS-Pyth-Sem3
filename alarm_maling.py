import utime
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# library utime digunakan sebagai pemberi waktu delay pada program

# informasi oled
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
# informasi pin yang dipasang dengan alat-alat
pir1kamar = machine.Pin(28, machine.Pin.IN, machine.Pin.PULL_DOWN)
pir2tamu = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(14, machine.Pin.OUT)
def pir_handler(pin):
    # untuk melakukan/menghandle interrupt
    utime.sleep_ms(100)
    # untuk mencegah nyalanya alarm karena "jitter" dari sensor
    if pin.value():
        if pin is pir1kamar:
            print("Pergerakan terdeteksi pada kamar tidur!")
            oled.text("Pergerakan", 0, 0)
            oled.text("terdeteksi", 7, 10)
            oled.text("pada", 5, 20)
            oled.text("kamar tidur", 22, 30)
            oled.show()
        elif pin is pir2tamu:
            print("Pergerakan terdeteksi pada ruang tamu!")
            oled.text("Pergerakan", 0, 0)
            oled.text("terdeteksi", 7, 10)
            oled.text("pada", 5, 20)
            oled.text("ruang tamu", 22, 30)
            oled.show()
        for i in range(25):
        # alarm akan berputar sebanyak 25 kali kemudian mati
            led.toggle()
            buzzer.toggle()
            utime.sleep_ms(100)
            # LED dan buzzer nilainya berubah LOW ke HIGH atau sebaliknya dengan delay
            # 100ms
# interrupt handler kedua
pir1kamar.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
pir2tamu.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)
while True:
    led.toggle()
    utime.sleep(5)

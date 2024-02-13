from machine import Pin, I2C, Timer
from imu import MPU6050
from ssd1306 import SSD1306_I2C
import time
import _thread as th

i2c1 = I2C(0, scl= Pin(21), sda= Pin(20)) #MPU
i2c2 = I2C(1, scl= Pin(19), sda= Pin(18)) #Oled

height = 64
weigth = 128
ax= 0.0
ay= 0.0
az= 0.0
t= 0.0

oled = SSD1306_I2C(weigth, height, i2c2)
mpu = MPU6050(i2c1)


def oledPrint():
    while True:
        oled.fill(0)
        oled.text("ax:" + str(ax),0,4)
        oled.text("ay:" +str(ay),0,16)
        oled.text("az:" +str(az),0,28)
        oled.text("temp:" +str(t),0,48)
        oled.show()
        time.sleep(0.5)


th.start_new_thread(oledPrint, ())


while True:
    ax = mpu.accel.x
    ay = mpu.accel.y
    az = mpu.accel.z
    t = mpu.temperature
    time.sleep(0.5)
    
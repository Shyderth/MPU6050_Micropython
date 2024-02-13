from machine import Pin, I2C, Timer
from imu import MPU6050
from ssd1306 import SSD1306_I2C
import time
import _thread as th

#Creamos los objetos I2C para conectar el giroscopio y la pantalla oled
i2c1 = I2C(0, scl= Pin(21), sda= Pin(20)) #MPU
i2c2 = I2C(1, scl= Pin(19), sda= Pin(18)) #Oled

#definimos el alto y ancho de la pantalla Oled
height = 64
weigth = 128
#Definimos los valores iniciales de las variables de rotacion obtenidas por el giroscopio
ax= 0.0
ay= 0.0
az= 0.0
t= 0.0

#Creamos los objetos propios del giroscopio y la Oled
oled = SSD1306_I2C(weigth, height, i2c2)
mpu = MPU6050(i2c1)

#Creamos una funcion encargada de imprimir en la pantalla oled los datos recibidos por el giroscopio
def oledPrint():
    while True:
        oled.fill(0)
        oled.text("ax:" + str(ax),0,4)
        oled.text("ay:" +str(ay),0,16)
        oled.text("az:" +str(az),0,28)
        #El giroscopio cuenta con un medidor de temperatura incorporado
        oled.text("temp:" +str(t),0,48)
        oled.show()
        time.sleep(0.5)

#Creamos un hilo para que uno de los nucleos del microcontrolador se encargue unicamente de mostrar la informacion
th.start_new_thread(oledPrint, ())

#Mediante un ciclo infinito obtenemos los datos del giroscopio cada medio segundo y actualizamos las variables que se muestran
#en la pantalla Oled
while True:
    ax = mpu.accel.x
    ay = mpu.accel.y
    az = mpu.accel.z
    t = mpu.temperature
    time.sleep(0.5)
    

# MPU6050 con Micropython
Para el funcionamiento del codigo es necesario importar en el microcontrolador las dos librerias encargadas de traducir los datos obtenidos con el giroscopio. Estas librerias fueron creadas por Peter Hinch y Sebastian Plamauer. Pueden encontrarse en: https://github.com/micropython-IMU/micropython-mpu9150.git
* IMPORTANTE: descargar unicamente los archivos ``imu.py`` (para crear el objeto tipo giroscopio) y ``vector3d.py`` (para traducir los datos obtenidos del sensor), los demas encontrados en el github del creador son para otros giroscopios y casos especificos

import time
import math

class Fusion:
    def getIMUFusion(a,g,m):
        GYRO_SENS = 65.536 # Each IMU has a specific sensitivity factor that you need to scale raw data into deg/s
        ACCEL_SENS = 1 # I changed some settings on my openlog board, but normally I would need a scaling factor for the accelerometer as well
        pitch = 0
        roll = 0
        last_time = time.time()
        accel = a
        gyro = g
        magn = m
        
        # Integrating gyroscope data
        dt = time.time() - last_time
        last_time = time.time()
        pitch += (gyro[0]/GYRO_SENS)*dt
        roll -= (gyro[1]/GYRO_SENS)*dt

        # Only use accelerometer when it's steady (magnitude is near 1g)
        forceMagnitude = math.sqrt(accel[0]**2 + accel[1]**2 + accel[2]**2)
        if forceMagnitude > 0.9 and forceMagnitude < 1.1:
            pitch = pitch*0.95 + math.atan2(accel[1], math.sqrt(accel[0]**2 + accel[2]**2) )*180/math.pi *0.05
            roll = roll*0.9 + math.atan2(-accel[0], accel[2])*180/math.pi *0.05
        
        p = (pitch*180/math.pi)
        r = (roll*180/math.pi)
        return (p,r)

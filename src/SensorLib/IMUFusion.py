import time
import math

class Fusion:
    def getIMUFusion(a,g,m):
        GYRO_SENS = 65.536 # Each IMU has a specific sensitivity factor that you need to scale raw data into deg/s
        #ACCEL_SENS = 1 # I changed some settings on my openlog board, but normally I would need a scaling factor for the accelerometer as well
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
    
Accel_pitch = 0
Gyro_pitch = 0
Comp_pitch = 0
Predicted_pitch = 0

Gyro_roll = 0
Accel_roll = 0
Comp_roll = 0
Predicted_roll = 0

dt = 0.02
Q = 0.1 # Prediction Estimate Initial Guess
R = 5 # Prediction Estimate Initial Guess
P00 = 0.1 # Prediction Estimate Initial Guess
P11 = 0.1 # Prediction Estimate Initial Guess
P01 = 0.1 # Prediction Estimate Initial Guess

Kk0 = 0
Kk1 = 0

def calFusion(self,a,g,m):
    accel = a
    gyro = g
    magn = m
    
    
    Accel_pitch = atan2((accel[1]) / 256, (accel[2]) / 256) * 180 / PI
    Gyro_pitch = Gyro_pitch + ((gyro[0]) / 14.375) * dt
    
    Comp_pitch = Gyro_pitch
    Predicted_pitch = Predicted_pitch + ((gyro[0]) / 14.375) * dt # Time Update step 1
    
    Accel_roll = atan2((accel[0]) / 256, (accel[2]) / 256) * 180 / PI
    Gyro_roll = Gyro_roll - ((gyro[1]) / 14.375) * dt
    
    Comp_roll = Gyro_roll;
    Predicted_roll = Predicted_roll - ((gyro[1]) / 14.375) * dt # Time Update step 1

    P00 += dt * (2 * P01 + dt * P11) #Projected error covariance terms from derivation result: Time Update step 2
    P01 += dt * P11 # Projected error covariance terms from derivation result: Time Update step 2
    P00 += dt * Q # Projected error covariance terms from derivation result: Time Update step 2
    P11 += dt * Q # Projected error covariance terms from derivation result: Time Update step 2
    Kk0 = P00 / (P00 + R) # Measurement Update step 1
    Kk1 = P01 / (P01 + R) # Measurement Update step 1
    
    Predicted_pitch += (Accel_pitch - Predicted_pitch) * Kk0 # Measurement Update step 2
    Predicted_roll += (Accel_roll - Predicted_roll) * Kk0 # Measurement Update step 2
    
    P00 *= (1 - Kk0) # Measurement Update step 3
    P01 *= (1 - Kk1) # Measurement Update step 3
    P11 -= Kk1 * P01 # Measurement Update step 3
    alpha = 0.98
    Comp_pitch = alpha*(Comp_pitch+Comp_pitch*dt) + (1.0 - alpha)*Accel_pitch # Complimentary filter
    Comp_roll = alpha*(Comp_roll+Comp_roll*dt) + (1.0 - alpha)*Accel_roll # Complimentary filter
    angle_z = gyro[2]
    print(angle_z)

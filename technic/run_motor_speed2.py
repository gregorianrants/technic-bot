from Motors.motors import motors
from behaviours.MotorSpeed2 import MotorSpeed
from Encoders.Encoder2 import Encoder
import asyncio
import time

left_encoder = Encoder(motors.left_motor,'left',log_data='test')
right_encoder = Encoder(motors.right_motor,'right')


left_motor_speed = MotorSpeed(left_encoder,motors.left_motor,40)
right_motor_speed = MotorSpeed(right_encoder,motors.right_motor,40)


right_motor_speed.start()
left_motor_speed.start()

try:
    right_motor_speed.start()
    left_motor_speed.start()
    time.sleep(10)
except KeyboardInterrupt:
    print('interupted')
    left_motor_speed.stop()
    right_motor_speed.stop()
    left_encoder.finish()
finally:
    print('finally')
    left_motor_speed.stop()
    right_motor_speed.stop()




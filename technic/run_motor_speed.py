from Motors.motors import motors
from Encoders.encoders import left_encoder,right_encoder
from behaviours.MotorSpeed import MotorSpeed
import asyncio

left_motor_speed = MotorSpeed(left_encoder,motors.left_motor)
right_motor_speed = MotorSpeed(right_encoder,motors.right_motor)
left_encoder.sleep = 0.025
right_encoder.sleep = 0.025


right_motor_speed.start()
left_motor_speed.start()


async def stop():
    await asyncio.sleep(10)
    left_motor_speed.stop()
    right_motor_speed.stop()
    left_encoder.stop()
    right_encoder.stop()
    





async def main():
    right_encoder_task = asyncio.create_task(right_encoder.start())
    left_encoder_task = asyncio.create_task(left_encoder.start())
    stop_task = asyncio.create_task(stop())
    
    await right_encoder_task

try:
    asyncio.run(main())
except KeyboardInterrupt:
    left_motor_speed.stop()
    right_motor_speed.stop()
finally:
    print('finally')





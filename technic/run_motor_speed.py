from Motors.motors import motors
from Encoders.encoders import left_encoder,right_encoder
from behaviours.MotorSpeed import MotorSpeed
import asyncio


def find_V_R(V_L,R_L,w):
    return (V_L * (R_L+w))/R_L

V_L = 15
V_R = find_V_R(V_L,20,115)

print(V_R)



left_motor_speed = MotorSpeed(left_encoder,motors.left_motor,20)
right_motor_speed = MotorSpeed(right_encoder,motors.right_motor,20)
left_encoder.sleep = 0.02
right_encoder.sleep = 0.02




right_motor_speed.start()
left_motor_speed.start()


async def stop():
    await asyncio.sleep(10)
    left_motor_speed.stop()
    right_motor_speed.stop()
    left_encoder.stop()
    right_encoder.stop()
    

async def main():
    left_encoder_task = asyncio.create_task(left_encoder.start())
    right_encoder_task = asyncio.create_task(right_encoder.start())
    stop_task = asyncio.create_task(stop())
    
    await right_encoder_task

try:
    asyncio.run(main())
except KeyboardInterrupt:
    left_motor_speed.stop()
    right_motor_speed.stop()
finally:
    print('finally')





from sshkeyboard import listen_keyboard_manual
from Motors.motors import motors
import asyncio
from Encoders.encoders import left_encoder
import time







time.sleep(1)







async def start_listening():
    #do i need to put a sleep in here, how often does it poll input may use up resources?
    await listen_keyboard_manual(
        on_press=press,
    )

async def main():
  listen = asyncio.create_task(start_listening())
  left_encoder_task = asyncio.create_task(left_encoder.start())
  await listen

async def press(key):
    print(f"'{key}' pressed")
    if(key=='up'):
        motors.forward(40)
    elif(key=='down'):
        motors.backward(40)
    elif(key=='left'):
        motors.pivot_left(30)
    elif(key=='right'):
        motors.pivot_right(30)
    elif(key=='space'):
        motors.stop()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    motors.stop()
finally:
    motors.stop()

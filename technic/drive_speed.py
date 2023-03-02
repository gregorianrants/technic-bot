from sshkeyboard import listen_keyboard_manual
import asyncio
from technic.robots.Speed_Control import SpeedControlRobot

bot = SpeedControlRobot()

async def start_listening():
    #do i need to put a sleep in here, how often does it poll input may use up resources?
    await listen_keyboard_manual(
        on_press=press,
    )

async def main():
  listen = asyncio.create_task(start_listening())
  runRobot = asyncio.create_task(bot.start())
  await listen

async def press(key):
    print(f"'{key}' pressed")
    if(key=='up'):
        bot.forward(300)
    elif(key=='down'):
        bot.backward(20)
    elif(key=='left'):
        bot.pivot_left(20)
    elif(key=='right'):
        bot.pivot_right(20)
    elif(key=='space'):
        bot.stop()


def release(key):
    print(f"'{key}' released")

try:
    asyncio.run(main())
except KeyboardInterrupt:
    bot.stop
finally:
    bot.stop
from sshkeyboard import listen_keyboard_manual
from Motors import Motors
import asyncio
from EncoderCounter import EncoderCounter



bot = Motors()



async def start_listening():
    #do i need to put a sleep in here, how often does it poll input may use up resources?
    await listen_keyboard_manual(
        on_press=press,
    )

async def main():
  listen = asyncio.create_task(start_listening())
  await listen

async def press(key):
    print(f"'{key}' pressed")
    if(key=='up'):
        bot.forward(50)
    elif(key=='down'):
        bot.backward(30)
    elif(key=='left'):
        bot.pivot_left(30)
    elif(key=='right'):
        bot.pivot_right(30)
    elif(key=='space'):
        bot.stop()

try:
    asyncio.run(main())
except KeyboardInterrupt:
    bot.stop()
finally:
    bot.stop()

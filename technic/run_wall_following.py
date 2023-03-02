print(__name__)
from distance_sensors.distance_emitter import distance_emitter 
from behaviours.WallFollowing import WallFollowing
import asyncio


from event_emitter_asyncio.EventEmitter import EventEmitter



wall_follower = WallFollowing()
wall_follower.start()

async def main():
    distance_task = asyncio.create_task(distance_emitter.start())
    await distance_task


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('stopiing')
finally:
    print('finally')
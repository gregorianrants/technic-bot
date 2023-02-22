from Distance import Distance

distance = Distance(sleep=1)

import asyncio




async def main():
  async for value in distance.distance_gen():
    value


asyncio.run(main())

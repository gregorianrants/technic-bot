from Motors import Motors
from pid_controller import PIController
from Distance import Distance
import asyncio


class WallFollowing:
    def __init__(self,motors,distance_gen):
      self.running = False
      self.motors = motors
      self.distance_gen = distance_gen
      self.set_point = 30 #cm
      self.controller = PIController(proportional_constant=1.1,integral_constant=0.15,derivative_constant=0.1)
      self.previous_r1 = None
      self.current_r1 = None
      self.previous_r2 = None
      self.current_r1 = None
      self.forward_speed = 30

    def updateDistances(self,r1,r2):
     self.previous_r1 = self.current_r1
     self.current_r1 = r1
     self.previous_r2 = self.current_r1
     self.current_r2 = r1

    def handleNewData(self,r1,r2): 
      self.updateDistances(r1,r2)
      if(self.current_r1==100.0 and self.previous_r1!=100):
        return
      if(not self.previous_r1):
          left_speed = self.forward_speed
          right_speed = self.forward_speed
      else:
        error = r1-r2  #+ve if pointing away from wall/furhter to left
        adjustment = self.controller.get_value(error)
        left_speed = self.forward_speed+adjustment
        right_speed = self.forward_speed - adjustment
      print(left_speed,right_speed)
      self.motors.set_left(left_speed)
      self.motors.set_right(right_speed)

    

    async def start(self):
      print('asdfsadfsdf')
      self.motors.forward(self.forward_speed)
      self.running = True
      async for distance in self.distance_gen():
        if self.running == False: 
          self.motors.stop()
          break
        self.handleNewData(distance['r1'],distance['r2'])

    def stop(self):
        self.running = False


motors = Motors()
distance_sensors = Distance(sleep=0.05)
wall_following = WallFollowing(motors,distance_sensors.distance_gen)

async def main():
  start = asyncio.create_task(wall_following.start())
  await start


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print('asdfsadfsadf')
    wall_following.stop()
    motors.stop()
finally:
    wall_following.stop()
    motors.stop()

motors.stop()

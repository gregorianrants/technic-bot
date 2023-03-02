from buildhat import Motor
import asyncio
import time


## TODO wheels may keep spinning after reset and give bad initial values on next use
## consider adding a start method.

class Counter():
  def __init__(self,motor):
    self.motor = motor
    self.count = 0  
    self.time_interval = 0
    self.speed = 0
    self.previous_count = self.motor.get_position()
    self.previous_time = time.time()
    self.wheel_diameter = 276 #mm

  def getSpeed(self,time_interval,angle_interval):
    angle_as_fraction = angle_interval/360
    distance_traveled = angle_as_fraction*self.wheel_diameter
    speed = distance_traveled/time_interval
    return speed

  def update(self):
    latest = self.motor.get_position()
    latest_time = time.time()
    time_interval = latest_time - self.previous_time
    angle_interval = abs(latest-self.previous_count)
    self.count = self.count + angle_interval
    self.speed = self.getSpeed(time_interval,angle_interval)
    self.previous_count = latest
    self.previous_time = latest_time

  def reset(self):
    self.count = 0
    self.time_interval = 0

  
 
class EncoderCounter(object):
  def __init__(self,left_motor,right_motor,sleep=0.05):
    self.sleep = sleep
    self.left_motor = left_motor
    self.right_motor = right_motor
    self.left_counter = Counter(self.left_motor)
    self.right_counter = Counter(self.right_motor)
    self.left_count  = self.left_counter.count
    self.right_count = self.right_counter.count
      
  def reset(self):
    self.left_counter.reset()
    self.right_counter.reset()

  def update(self):
    self.right_counter.update()
    self.left_counter.update()
    
  

  async def position_generator(self):
    while True:
      await asyncio.sleep(0.05)
      self.update()
      result =  {
        'left': self.left_counter.count,
        'right': self.right_counter.count,
        'left_speed': self.left_counter.speed,
        'right_speed': self.right_counter.speed
        }
      print(result)
      yield result

 


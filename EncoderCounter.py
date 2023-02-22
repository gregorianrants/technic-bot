from buildhat import Motor
import asyncio


## TODO wheels may keep spinning after reset and give bad initial values on next use
## consider adding a start method.

class Counter():
  def __init__(self,motor):
    self.motor = motor
    self.count = 0
    self.previous = self.motor.get_position()

  def update(self):
    latest = self.motor.get_position()
    self.count = self.count + abs(latest-self.previous)
    self.previous = latest

  def reset(self):
    self.count = 0

  
 
class EncoderCounter(object):
  def __init__(self,left_motor,right_motor):
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
      yield {
        'left': self.left_counter.count,
        'right': self.right_counter.count
        }

 


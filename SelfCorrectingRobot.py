from EncoderCounter import EncoderCounter
import time
from pid_controller import PIController
from Motors import Motors
import asyncio

class Counter():
  def __init__(self):
    self.count = 0
    self.previous_time = None
    self.previous_count = None
    self.ticks_per_second = None


  def tick(self,count):
    if self.previous_time==None and self.previous_count ==None:
      self.previous_time = time.time()
      self.previous_count = count

    elif time.time()-self.previous_time >=1:
      self.previous_time = time.time()
      self.ticks_per_second = count - self.previous_count
      self.previous_count = count
      #print('ticks per second',self.ticks_per_second)

  def reset(self):
    self.count = 0
    self.previous_time = None
    self.previous_count = None
    self.ticks_per_second = None
      

      
class SelfCorrectingRobot():
  def __init__(self):
    self.motors = Motors()
    self.state = 'stopped'
    self.encoder = EncoderCounter(self.motors.left_motor,self.motors.right_motor)
    self.forward_speed = 50
    #self.pid = PIController(proportional_constant=0.1, integral_constant=0.001)
    #self.pid = PIController(proportional_constant=0.05,integral_constant=0.02,derivative_constant=0.01)
    self.pid = PIController(proportional_constant=0.05,integral_constant=0.02,derivative_constant=0.005)

  def forward(self,speed):
    self.forward_speed = speed
    self.reset()
    self.state = 'forward'
    self.motors.set_left(self.forward_speed)
    self.motors.set_right(self.forward_speed)

  def stop(self):
    self.state='stopped'
    self.motors.stop()
    self.reset()

  def backward(self,speed):
    print('going back')
    self.reset()
    self.state = 'backward'
    self.motors.backward(speed)
               
  def pivot_left(self,speed):
    self.reset()
    self.state = 'pivot_left'
    self.motors.pivot_left(speed)

  def pivot_right(self,speed):
    self.reset()
    self.state = 'pivot_right'
    self.motors.pivot_right(speed)
         
  def count(self):
    self.left_counter.tick(self.left_encoder.pulse_count)
    self.right_counter.tick(self.left_encoder.pulse_count)

  def reset(self):
    self.encoder.reset()

  def update(self,left,right):
    if(self.state=='forward'):
      print('left',left)
      print('right',right)
      error = left-right
      adjustment = self.pid.get_value(error)
      print('adjustment',adjustment)
      left_speed = int(self.forward_speed-adjustment)
      right_speed = int(self.forward_speed + adjustment)
      # left_speed = self.forward_speed
      # right_speed = self.forward_speed
      self.motors.set_left(left_speed)
      self.motors.set_right(right_speed)
      #self.count()

  async def start(self):
    async for counts in self.encoder.position_generator():
      print(counts)
      self.update(counts['left'],counts['right'])
    # while True:
    #   self.update()
    #   await asyncio.sleep(0.01)
    




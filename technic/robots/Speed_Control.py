from Encoders.EncoderCounter import EncoderCounter
import time
from utilities.pid_controller import PI_PVD_Controller
from Motors.Motors import Motors
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
      

      
class SpeedControlRobot():
  def __init__(self):
    self.motors = Motors()
    self.state = 'stopped'
    self.encoder = EncoderCounter(self.motors.left_motor,self.motors.right_motor,sleep=0.1)
    #self.pid = PIController(proportional_constant=0.1, integral_constant=0.001)
    #self.pid = PIController(proportional_constant=0.05,integral_constant=0.02,derivative_constant=0.01)
    # self.p = 0.01
    # self.k = 0
    # self.d = 0
    self.p = 0.01
    self.k = 0
    self.d = 0.005
    self.pid_left = PI_PVD_Controller(self.p,self.k,self.d)
    self.pid_right = PI_PVD_Controller(self.p,self.k,self.d)
    self.left_power = 0
    self.right_power = 0

  def forward(self,speed):
    self.left_power = int(self.left_power)
    self.right_power = int(self.right_power)
    self.reset()
    self.state = 'forward'

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
      left_error = left-350
      right_error = right-350
      left_adjustment = self.pid_left.get_value(left_error,left)
      right_adjustment = self.pid_right.get_value(right_error,right)
      print('left_error', left_error)
      print('left_adjustment',left_adjustment)
      self.left_power = int(self.left_power-left_adjustment)
      self.right_power = int(self.right_power-right_adjustment)
      # left_speed = self.forward_speed
      # right_speed = self.forward_speed
      self.motors.set_left(self.left_power)
      self.motors.set_right(self.right_power)
      #self.count()

  async def start(self):
    async for counts in self.encoder.position_generator():
      self.update(counts['left_speed'],counts['right_speed'])
    # while True:
    #   self.update()
    #   await asyncio.sleep(0.01)
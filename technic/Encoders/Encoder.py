from event_emitter_asyncio.EventEmitter import EventEmitter
import asyncio
import time
from Motors.motors import motors

class Encoder(EventEmitter):
  def __init__(self,motor,name):
    super().__init__()
    self.motor = motor
    self.count = 0  
    self.time_interval = 0
    self.speed = 0
    self.previous_count = self.motor.get_position()
    self.previous_time = time.time()
    self.wheel_diameter = 276 #mm
    self.name = name
    self.sleep = 0.025
    self.running = False

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

  def stop(self):
    self.running = False

  async def start(self):
    self.running = True
    while True:
      await asyncio.sleep(self.sleep)
      self.update()
      val = {f'count': self.count, f'speed': self.speed}
      #print(val)
      self.emit(f'{self.name}_encoder',val)
      if(self.running==False):
        break
    print('encoder stopped')


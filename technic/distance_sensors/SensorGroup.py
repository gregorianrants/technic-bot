import time
from DistanceSensor import DistanceSensor
import RPi.GPIO as GPIO

def seconds_to_milliseconds(seconds):
    return seconds*1000

DELAY_BETWEEN_PINGS_IN_MS = 50

class SensorGroup:
  def __init__(self,sensors=[],delay_between_pings_ms=DELAY_BETWEEN_PINGS_IN_MS):
    self.sensors = sensors
    self.readings = {}
    self.delay_between_pings_ms = delay_between_pings_ms

  def measure(self):
    for sensor in self.sensors:
      startTime = time.time()
      self.readings[sensor.name]=sensor.getReading()
      while(seconds_to_milliseconds(time.time()-startTime)<self.delay_between_pings_ms):
            pass
    return self.readings

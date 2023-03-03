import asyncio
import time
import pathlib
import os
import numpy as np
import matplotlib.pyplot as plt
import json

class Encoder():
  def __init__(self,motor,name,log_data=False):
    super().__init__()
    self.motor = motor
    self.count = 0  
    self.wheel_diameter = 276 #mm
    self.name = name
    self.running = False
    self.handle_rotation=None
    self.speeds = []
    self.motor.set_rotation_callback(self._handle_rotation)
    self.log_data = log_data

  def _handle_rotation(self,aSpeed,aPos,aApos):
      speed = self.getSpeed(aSpeed)
      self.speeds.append(speed)
      if(self.handle_rotation):
        self.handle_rotation(speed)

  def getSpeed(self,aSpeed):
    speed =  (aSpeed/360)*self.wheel_diameter
    return speed
  
  def reset(self):
    self.count = 0

  def finish(self):
    self.motor.set_rotation_callback(False)
    if(self.log_data):
      tune_data_folder = pathlib.Path.cwd().joinpath('data',self.log_data)
      file_index = len(os.listdir(tune_data_folder))
      file_suffix = f'{file_index}'
      write_file_path = tune_data_folder.joinpath(f'{self.name}_{file_suffix}')
      json_path = f'{write_file_path}.json'
      png_path = f'{write_file_path}.png'
      with open(json_path,'w') as f:
        json.dump(
           self.speeds,f,indent=2)
      plt.plot(self.speeds,marker='.')
      plt.savefig(png_path)
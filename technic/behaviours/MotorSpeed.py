from utilities.pid_controller import PIController
import json
import time
import pathlib
import os
import numpy as np
import matplotlib.pyplot as plt

print(pathlib.Path.cwd())

class MotorSpeed:
    def __init__(self,encoder,motor,speed=0):
      self.encoder = encoder
      self.motor = motor
      self.p = 0.005
      self.k = 0.001
      self.d = 0.0025
      self.pid = PIController(self.p,self.k,self.d)
      ##power should probably be passed by previouse behaviour
      self.power=20
      self.errors = []

    def stop(self):
       self.motor.stop()
       tune_data_folder = pathlib.Path.cwd().joinpath('tune_motor_speed')
       file_index = len(os.listdir(tune_data_folder))
       file_suffix = f'{file_index}_p-{self.p}_k-{self.k}_d-{self.d}'
       write_file_path = tune_data_folder.joinpath(f'{self.encoder.name}_{file_suffix}')
       json_path = f'{write_file_path}.json'
       png_path = f'{write_file_path}.png'
       with open(json_path,'w') as f:
          json.dump(
             {
              'p':self.p,
              'k':self.k,
              'd':self.d,
              'errors': self.errors,
             },f,indent=2)
       plt.plot(self.errors)
       plt.savefig(png_path)
          

    async def update(self,encoder_values):
      speed = encoder_values['speed']
      error = speed-400
      self.errors.append(error)
      adjustment = self.pid.get_value(error)
      print('error', error)
      print('djustment',adjustment)
      self.power = int(self.power-adjustment)
      self.motor.pwm(self.power)
 
    def start(self):
      self.encoder.add_listener(f'{self.encoder.name}_encoder',self.update)
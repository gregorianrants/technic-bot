from utilities.pid_controller import PIController
import json
import time
import pathlib
import os
import numpy as np
import matplotlib.pyplot as plt

print(pathlib.Path.cwd())

class MotorSpeed:
    def __init__(self,encoder,motor,set_point=40):
      self.motor = motor
      self.p = 0.01
      self.k = 0.00
      self.d = 0.001
      self.pid = PIController(self.p,self.k,self.d)
      ##power should probably be passed by previouse behaviour
      self.power=set_point/2
      self.errors = []
      self.set_point = set_point
      self.encoder = encoder
      self.running = False

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
          

    def update(self,speed):
      error = speed-self.set_point
      self.errors.append(error)
      adjustment = self.pid.get_value(error)
      self.power = self.power-adjustment
      self.motor.pwm(self.power)

    def handle_rotation(self,speed):
       self.update(speed)
       
    def start(self):
      self.running = True
      self.motor.pwm(self.power)
      time.sleep(0.01)
      self.encoder.handle_rotation = self.handle_rotation

    def stop(self):
       self.encoder.handle_rotation = None
       self.motor.stop()
       
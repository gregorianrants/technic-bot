import numpy as np
import pathlib
import json
import matplotlib.pyplot as plt

path = pathlib.Path.cwd().joinpath('tune_motor_speed','left_10.json')
f = open(path)
data = json.load(f)
errors = data['errors']
errors = np.array(errors)[10:]

plt.plot(errors)
plt.savefig("dummy_name.png")



print(data)
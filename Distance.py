import asyncio
from gpiozero import DistanceSensor,Device
from time import sleep

class Distance:
    def __init__(self,sleep=0.05):
        self.R2_TRIG = 26
        self.R2_ECHO = 19
        self.r2_sensor = DistanceSensor(echo=self.R2_ECHO,trigger=self.R2_TRIG)
        self.R1_TRIG = 21
        self.R1_ECHO = 20
        self.r1_sensor = DistanceSensor(echo=self.R1_ECHO,trigger=self.R1_TRIG)  
        self.sleep=sleep

    async def distance_gen(self):
        while True:
            await asyncio.sleep(self.sleep)
            values = {
                'r2': self.r2_sensor.distance*100,
                'r1': self.r1_sensor.distance*100
            }
            print(values)
            yield values
from buildhat import Motor,MotorPair
import time
class Motors:
        def __init__(self):
                self.left_motor = Motor('C')
                self.right_motor = Motor('D')
                
                
        def convert_speed(self,speed):
                return speed/100

        def set_left(self,speed):
                speed = self.convert_speed(speed)
                self.left_motor.pwm(-speed)

        def set_right(self,speed):
                speed = self.convert_speed(speed)
                self.right_motor.pwm(speed)

        def set_both(self,speed):
                self.set_right(speed)
                self.set_left(speed)
                

        def stop(self):
                self.left_motor.pwm(0)
                self.right_motor.pwm(0)

        def forward(self,speed):
                self.set_both(speed)

        def backward(self,speed):
                self.set_both(-speed)

        def pivot_left(self,speed):
                self.set_left(-speed)
                self.set_right(speed)

        def pivot_right(self,speed):
                self.set_left(speed)
                self.set_right(-speed)



from buildhat import Motor as BuildHatMotor
import time


def convert_pwm(pwm_100):
                
                return pwm_1

class Motor():
        def __init__(self,port,direction):
                self.motor = BuildHatMotor(port)
                self.direction = direction
                print(self.motor)
        
        def get_position(self):
                return self.motor.get_position()
        
        def pwm(self,pwm_100):
                pwm_1 = pwm_100/100
                self.motor.pwm(self.direction*pwm_1)

        def stop(self):
                self.motor.stop()

        

class Motors:
        def __init__(self):
                self.left_motor = Motor('C',-1)
                self.right_motor = Motor('D',1)
                # self.left_motor = BuildHatMotor('C')
                # self.right_motor = BuildHatMotor('D')
                time.sleep(2)
                print('initialised motors')
                
        def convert_speed(self,speed):
                return speed/100
                
        def set_left(self,pwm_100):
                self.left_motor.pwm(pwm_100)
                
        def set_right(self,pwm_100):
                self.right_motor.pwm(pwm_100)

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



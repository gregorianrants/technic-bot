from buildhat import Motor
import time

leftmotor = Motor('C')
# leftmotor.plimit(1.0)
# leftmotor.bias(0.4)

rightmotor = Motor('D')

# rightmotor.plimit(1.0)
# rightmotor.bias(0.4)

# def sequence():
#     leftmotor.start(speed=50)
#     rightmotor.start(speed=-50)
#     time.sleep(2)
#     leftmotor.stop()
#     rightmotor.stop()
#     time.sleep(0.5)
#     leftmotor.start(speed=50)
#     rightmotor.start(speed=50)
#     time.sleep(2)
#     leftmotor.stop()
#     rightmotor.stop()
#     time.sleep(0.5)
#     leftmotor.start(speed=50)
#     rightmotor.start(speed=-50)
#     time.sleep(2)
#     leftmotor.stop()
#     rightmotor.stop()
#     time.sleep(0.5)

# for i in range(3):
#     sequence()

rightmotor.pwm(0.3)
time.sleep(1)
print(rightmotor.get_position())
time.sleep(2)
rightmotor.pwm(0)







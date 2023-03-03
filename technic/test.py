import time

from buildhat import Motor

left_motor = Motor('C')
right_motor = Motor('D')


left_motor.plimit(0.9)
left_motor.bias(0.35)
right_motor.plimit(0.9)
right_motor.bias(0.35)

def stop():
    left_motor.stop()
    right_motor.stop()

def forward():
    print('sleeping for 1')
    time.sleep(1)
    print('going forward')
    left_motor.start(speed=-40)
    right_motor.start(speed=40)
    

def left():
    print('sleeping for 1')
    time.sleep(1)
    print('going left')
    left_motor.start(speed=-40)
    right_motor.start(speed=-40)
    

def right():
    print('sleeping for 1')
    time.sleep(1)
    print('going right')
    left_motor.start(speed=40)
    right_motor.start(speed=40)
    

def back():
    print('sleeping for 1')
    time.sleep(1)
    print('going back')
    left_motor.start(speed=-40)
    right_motor.start(speed=40)
    


def stop():
    print('stopping')
    left_motor.stop()
    right_motor.stop()
    print('stopped')
print('hello')


try: 

    forward()
    print(left_motor.get())
    time.sleep(2)
    print(left_motor.get())
    time.sleep()
    print(left_motor.get())
    
    
  
except KeyboardInterrupt:
    stop()
except Exception as e:
    print(e)






from .Encoder import Encoder
from Motors.motors import motors

left_encoder = Encoder(motor=motors.left_motor,name='left')
right_encoder = Encoder(motor=motors.right_motor,name='right')
import time

# download from: https://github.com/zhcong/ULN2003-for-ESP32
# file: https://github.com/zhcong/ULN2003-for-ESP32/blob/master/Stepper.py

# based on: https://github.com/IDWizard/uln2003
# (c) IDWizard 2017, # MIT License.

### usage:
### https://github.com/zhcong/ULN2003-for-ESP32/blob/master/main.py
# import Stepper
# from machine import Pin

# # connected to ESP32, Pin 32,33,25,26
# # using default parameters: delay=2, mode='HALF_STEP'
# In1 = Pin(32,Pin.OUT)
# In2 = Pin(33,Pin.OUT)
# In3 = Pin(25,Pin.OUT)
# In4 = Pin(26,Pin.OUT)
# s1 = Stepper.create(In1,In2,In3,In4)
# #
# # one revolution is about 509 steps
# s1.step(100)      # 100 steps clockwise
# s1.step(100,-1)   # 100 steps counter clockwise
# s1.angle(180)     # 180 degree  clockwise
# s1.angle(360,-1)  # 180 degree counter clockwise

# only test for uln2003
class Stepper:
    FULL_ROTATION = int(4075.7728395061727 / 8) # http://www.jangeox.be/2013/10/stepper-motor-28byj-48_25.html

    HALF_STEP = [
        [0, 0, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
    ]

    FULL_STEP = [
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 1]
    ]
    def __init__(self, mode, pin1, pin2, pin3, pin4, delay):
    	if mode=='FULL_STEP':
        	self.mode = self.FULL_STEP
        else:
        	self.mode = self.HALF_STEP
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        self.delay = delay  # Recommend 10+ for FULL_STEP, 1 is OK for HALF_STEP

        # Initialize all to 0
        self.reset()

    def step(self, count, direction=1):
        """Rotate count steps. direction = -1 means backwards"""
        for x in range(count):
            for bit in self.mode[::direction]:
                self.pin1(bit[0])
                self.pin2(bit[1])
                self.pin3(bit[2])
                self.pin4(bit[3])
                time.sleep_ms(self.delay)
        self.reset()
    def angle(self, r, direction=1):
    	self.step(int(self.FULL_ROTATION * r / 360), direction)
    def reset(self):
        # Reset to 0, no holding, these are geared, you can't move them
        self.pin1(0) 
        self.pin2(0) 
        self.pin3(0) 
        self.pin4(0)

def create(pin1, pin2, pin3, pin4, delay=2, mode='HALF_STEP'):
	return Stepper(mode, pin1, pin2, pin3, pin4, delay)

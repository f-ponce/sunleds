#!/usr/bin/env python

from __future__ import print_function
import time
from find_fly_angle import find_fly_angle
from led_pwm_control import LEDController 
import numpy as np
import rospy
import csv
import os


timestr = time.strftime("sundata_%Y%m%d_%H%M%S", time.localtime())
directory = '/home/francescavponce/catkin/src/sunleds/data/'
filename = os.path.join(directory,'sun_data_%s.csv'%timestr)
sun_ids = open(filename,'w')

dev = LEDController('/dev/led-device')

suns = [3,5,6,9]

shuffle_suns = suns
np.random.shuffle(shuffle_suns)
print(shuffle_suns)
sun_ids.write('{0}\n'.format(shuffle_suns))

time_stripe = 31#31
time_dark = 300#300
sun_time = 300#300 
sun_intensity = 50

#stripe+dark
dev.set_value(shuffle_suns[0], 0)
time.sleep(time_stripe)
dev.set_value(shuffle_suns[0], 0)
time.sleep(time_dark)
#sun 1
dev.set_value(shuffle_suns[0], sun_intensity)
print(shuffle_suns[0])
time.sleep(sun_time*2)
dev.set_value(suns[0], 0)

#sun 2
dev.set_value(shuffle_suns[1], sun_intensity)
print(shuffle_suns[1])
time.sleep(sun_time*2)
dev.set_value(suns[1], 0)

#sun 1 again
dev.set_value(shuffle_suns[0], sun_intensity)
print(shuffle_suns[0])
time.sleep(sun_time)
dev.set_value(suns[0], 0)

dev.set_value(shuffle_suns[0], 0)
time.sleep(sun_time*2)


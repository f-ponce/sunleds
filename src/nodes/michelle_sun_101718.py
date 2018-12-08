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

time_sun_off_stripe = 31
time_sun_off_dark = 120
time_sun_on1 = 300
sun_intensity = 50

#sun off while stripe on
dev.set_value(shuffle_suns[0], 0)
time.sleep(time_sun_off_stripe)
#sun off while dark
dev.set_value(shuffle_suns[0], 0)
time.sleep(time_sun_off_dark)
#sun ON 
dev.set_value(shuffle_suns[0], sun_intensity)
time.sleep(time_sun_on1)
dev.set_value(shuffle_suns[0], 0)

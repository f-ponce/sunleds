#!/usr/bin/env python

from __future__ import print_function
import time
from find_fly_angle import find_fly_angle
from led_pwm_control import LEDController 
import numpy as np
import rospy
import csv
import os
import datetime

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

time_sun_1 = 10
time_sun_2 = 180
time_sun_3 = 0
time_sun_4 = 180
time_sun_5 = 360
time_sun_6 = 180
time_sun_7 = 0
time_sun_8 = 180

sun_intensity_off = 0
sun_intensity = 50

nowtime = datetime.datetime.now().strftime("%H%M%S_%f")
sun_ids.write('{0} {1} {2}\n'.format(nowtime, shuffle_suns[0], sun_intensity_off));
dev.set_value(shuffle_suns[0], sun_intensity_off)
time.sleep(time_sun_1)

nowtime = datetime.datetime.now().strftime("%H%M%S_%f")
sun_ids.write('{0} {1} {2}\n'.format(nowtime, shuffle_suns[0], sun_intensity));
dev.set_value(shuffle_suns[0], sun_intensity)
time.sleep(time_sun_2)

nowtime = datetime.datetime.now().strftime("%H%M%S_%f")
sun_ids.write('{0} {1} {2}\n'.format(nowtime, shuffle_suns[0], sun_intensity_off));
dev.set_value(shuffle_suns[0], sun_intensity_off)
time.sleep(time_sun_3)

nowtime = datetime.datetime.now().strftime("%H%M%S_%f")
sun_ids.write('{0} {1} {2}\n'.format(nowtime, shuffle_suns[1], sun_intensity));
dev.set_value(shuffle_suns[1], sun_intensity)
time.sleep(time_sun_4)

nowtime = datetime.datetime.now().strftime("%H%M%S_%f")
sun_ids.write('{0} {1} {2}\n'.format(nowtime, shuffle_suns[1], sun_intensity));
dev.set_value(shuffle_suns[1], sun_intensity)
time.sleep(time_sun_5)

nowtime = datetime.datetime.now().strftime("%H%M%S_%f")
sun_ids.write('{0} {1} {2}\n'.format(nowtime, shuffle_suns[1], sun_intensity));
dev.set_value(shuffle_suns[1], sun_intensity)
time.sleep(time_sun_6)

nowtime = datetime.datetime.now().strftime("%H%M%S_%f")
sun_ids.write('{0} {1} {2}\n'.format(nowtime, shuffle_suns[1], sun_intensity_off));
dev.set_value(shuffle_suns[1], sun_intensity_off)
time.sleep(time_sun_7)

nowtime = datetime.datetime.now().strftime("%H%M%S_%f")
sun_ids.write('{0} {1} {2}\n'.format(nowtime, shuffle_suns[0], sun_intensity));
dev.set_value(shuffle_suns[0], sun_intensity)
time.sleep(time_sun_8)

nowtime = datetime.datetime.now().strftime("%H%M%S_%f")
sun_ids.write('{0} {1} {2}\n'.format(nowtime, shuffle_suns[0], sun_intensity_off));
dev.set_value(shuffle_suns[0], sun_intensity_off)




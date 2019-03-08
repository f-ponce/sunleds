#!/usr/bin/env python
from __future__ import print_function

import time
import random
import numpy as np
import os
import sys
import datetime
import roslib
import rospy
import functools
import threading

import std_msgs.msg

from basic_led_strip_ros.msg import LEDValue

timestr = time.strftime("sundata_%Y%m%d_%H%M%S", time.localtime())
directory = '/home/francescavponce/catkin/src/sunleds/data/'
filename = os.path.join(directory,'sun_data_%s.csv'%timestr)
sun_ids = open(filename,'w')

class LedStrip(object):


    def __init__(self):
        rospy.init_node('led_value_test_pub')
        self.led_value_pub = rospy.Publisher('set_led_value', LEDValue, queue_size=10)
        self.num_led = 106 # Temporary get from service later


    def run(self):
    
        done = False
        a = 5
        
        led_pos = 3
        counter = 0
        
        red = a
        green = a
        blue = a
        
        while (not rospy.is_shutdown()) and (not done):

            if counter ==0:
                t0 = rospy.Time.now()
                sun_ids.write('{0}\n'.format(t0));
                rospy.sleep(11)
                led_pos = 5
                header = std_msgs.msg.Header()
                header.stamp = rospy.Time.now()
                self.led_value_pub.publish(LEDValue(header,led_pos,red,green,blue))
                sun_ids.write('{0} {1} {2} {3} {4} \n'.format(header, led_pos, red, green, blue));
                rospy.sleep(180)
                counter += 1
            elif counter==1:
                red = a
                green = a
                blue = a
                header = std_msgs.msg.Header()
                header.stamp = rospy.Time.now()
                self.led_value_pub.publish(LEDValue(header,led_pos,red,green,blue))
                sun_ids.write('{0} {1} {2} {3} {4} \n'.format(header, led_pos, red, green, blue));
                rospy.sleep(1)
                led_pos += 1
                if led_pos >= self.num_led-1:
                    led_pos = 3
                    red = a
                    green = a
                    blue = a
                    counter += 1                    
            elif counter==2:
                t1 = rospy.Time.now()
                sun_ids.write('{0}\n'.format(t1));
                led_pos = 3
                red = 0
                green = 0
                blue = 0
                header = std_msgs.msg.Header()
                header.stamp = rospy.Time.now()
                self.led_value_pub.publish(LEDValue(header,led_pos,red,green,blue))
                sun_ids.write('{0} {1} {2} {3} {4} \n'.format(header, led_pos, red, green, blue));
                rospy.sleep(10)
                counter += 1
            elif counter==3:
                t2 = rospy.Time.now()
                sun_ids.write('{0}\n'.format(t2));
#                rospy.sleep(1)
                led_pos = 5
                red = a
                green = a
                blue = a
                header = std_msgs.msg.Header()
                header.stamp = rospy.Time.now()
                self.led_value_pub.publish(LEDValue(header,led_pos,red,green,blue))
                sun_ids.write('{0} {1} {2} {3} {4} \n'.format(header, led_pos, red, green, blue));
                rospy.sleep(120)
                counter += 1
            elif counter==4:
                red = a
                green = a
                blue = a
                header = std_msgs.msg.Header()
                header.stamp = rospy.Time.now()
                self.led_value_pub.publish(LEDValue(header,led_pos,red,green,blue))
                sun_ids.write('{0} {1} {2} {3} {4} \n'.format(header, led_pos, red, green, blue));
                rospy.sleep(1)
                led_pos += 1
                if led_pos >= self.num_led-1:
                    led_pos = 3
                    red = a
                    green = a
                    blue = a
                    counter += 1
            elif counter>4:
                done = True


# -------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    node = LedStrip()
    node.run()

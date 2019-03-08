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

    def publish_leds(self, led_pos, red, green, blue):
        header = std_msgs.msg.Header()
        header.stamp = rospy.Time.now()
        self.led_value_pub.publish(LEDValue(header,led_pos,red,green,blue))
        
    def dither_leds(self, led_pos):
        #1. 1 led, high intensity
        self.t0 = 0.1
        self.t1 = 1
        self.i0 = 0
        self.i1 = 5
        self.ih = 2
        self.red, self.green, self.blue = self.i1,self.i1,self.i1
        self.publish_leds(led_pos, self.red, self.green, self.blue)
        rospy.sleep(self.t0)
        
        
        #2. 2 leds, low intensity
        self.red, self.green, self.blue = self.ih,self.ih,self.ih
        self.publish_leds(led_pos, self.red, self.green, self.blue)
        led_pos += 1
        self.red, self.green, self.blue = self.ih,self.ih,self.ih
        self.publish_leds(led_pos, self.red, self.green, self.blue)
        rospy.sleep(self.t0) 
        
        led_pos -= 1
        #3. turn off led1
        self.red, self.green, self.blue = self.i0,self.i0,self.i0
        self.publish_leds(led_pos, self.red, self.green, self.blue)
        
        led_pos += 1
        
        #4. increase intensity led2
        self.red, self.green, self.blue = self.i1,self.i1,self.i1
        self.publish_leds(led_pos, self.red, self.green, self.blue)
        rospy.sleep(self.t0)

    def run(self):
    
        done = False
        
        led_pos = 3
        counter = 0
        rospy.sleep(1)
        while (not rospy.is_shutdown()) and (not done):
            self.dither_leds(led_pos)
            led_pos += 1
            if led_pos >= self.num_led:
                self.red, self.green, self.blue = self.i0,self.i0,self.i0
                self.publish_leds(led_pos, self.red, self.green, self.blue)
                led_pos = 3

## -------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    node = LedStrip()
    node.run()

#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import rospy
from first_package import drone
import random

pub = rospy.Publisher("drone_topic", drone, queue_size = 10)

rospy.init_node("publisher", anonymous = True)

rate = rospy.Rate(10)

i = 0

while(not rospy.is_shutdown()):

    drone_info = drone()

    drone_info.id = 1
    drone_info.name = "drone_zey"
    drone_info.speed = random.randint(5, 25)
    drone_info.temperature = random.uniform(20, 30)
    drone_info.batteryStatus = 4000 - i

    rospy.loginfo(drone_info)

    pub.publish(drone_info)

    rate.sleep()

    i = i + 1

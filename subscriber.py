#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import rospy 
from first_package.msg import drone

def function(data):

    rospy.loginfo("received datas: (id, name, speed, temperature, battery status)", data.id, data.name , data.speed, data.temperature, data.batteryStatus)


rospy.init_node("subscriber", anonymous = True)

rospy.Subscriber("drone_topic", drone, function)
rospy.spin()
#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import rospy
from first_package.srv import wordCounter

def countWord(data):

    return len(data.words.split())

rospy.init_node("service_server")

service = rospy.Service("Word Counter", wordCounter, countWord)
rospy.spin()

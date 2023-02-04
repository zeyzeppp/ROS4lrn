#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
from first_package.srv import wordCounter
import sys

rospy.init_node('service_client')

rospy.wait_for_service('word_counter') 

say = rospy.ServiceProxy('word_counter',wordCounter)

words = ' '.join(sys.argv[1:])

count = say(words)


print("Words:", words, "Count:", count.counter)
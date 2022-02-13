#!/usr/bin/env python3
#Code to move turtle in turtlesim in different patterns

import rospy
from geometry_msgs.msg import Twist
import math

def pattern_movement():
    #defining node
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('send_vel', anonymous=True)
    v = 1.0
    flag = 0
    rate = rospy.Rate(1)
    
    while not rospy.is_shutdown():
        vel = Twist()
        
        #uncomment following snippets for different patterns
        
        '''
        #circle:
        vel.linear.x = 11.0
        vel.linear.y = 0.0
        vel.angular.z = 5.0
        '''
        
        '''
        #spiral:
        vel.linear.x = v
        vel.linear.y = 0.0
        vel.angular.z = 5.0
        v+=0.00003
        '''
        
        #'''
        #sq spiral:
        if flag == 0:
            vel.linear.x = v
            vel.linear.y = 0.0
            vel.angular.z = 0.0
            flag = 1
        elif flag == 1:
            vel.linear.x = 0.0
            vel.linear.y = v
            vel.angular.z = 0.0
            v = -1*(v-(-1)**v)
            flag = 0
        rate.sleep()
        #'''
        
        #pubishing required velocity
        pub.publish(vel)

if __name__ == '__main__':
    try:
        pattern_movement()
    except rospy.ROSInterruptException:
        pass

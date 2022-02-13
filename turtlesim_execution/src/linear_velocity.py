#!/usr/bin/env python3
#Code to give linear velocity to a turtle in turtlesim

import rospy
from geometry_msgs.msg import Twist

def give_velocity():
	#define node:
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('send_vel', anonymous=True)
    
    #repeat till node is shut down
    while not rospy.is_shutdown():
    	#defining velocity values
        vel = Twist()
        vel.linear.x = 11.0
        vel.linear.y = 1.0
        vel.angular.z = 0.0
        
        #publish velocity
        pub.publish(vel)

if __name__ == '__main__':
    try:
        give_velocity()
    except rospy.ROSInterruptException:
        pass

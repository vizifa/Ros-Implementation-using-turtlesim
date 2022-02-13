#!/usr/bin/env python3
#Code to control turtle in turtlesim using keyboard

import getch
import rospy
from geometry_msgs.msg import Twist

def keyboard_control():
    
    #defining node
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('send_vel', anonymous=True)
    
    vel = Twist()
    
    #repeat till node is shut down 
    while not rospy.is_shutdown():
        
        key = getch.getch()

	#turning left
        if(key == 'a'):
            vel.linear.x = 0.0
            vel.linear.y = 0.0
            vel.angular.z = 5.0
            
        #turning right
        elif(key == 'd'):
            vel.linear.x = 0.0
            vel.linear.y = 0.0
            vel.angular.z = -5.0
            
        #moving forward
        elif(key == 'w'):
            vel.linear.x = 5.0
            vel.linear.y = 0.0
            vel.angular.z = 0.0
            
        #moving backward
        elif(key == 's'):
            vel.linear.x = -5.0
            vel.linear.y = 0.0
            vel.angular.z = 0.0
         
        #publish velocity   
        pub.publish(vel)

if __name__ == '__main__':
    try:
        keyboard_control()
    except rospy.ROSInterruptException:
        pass

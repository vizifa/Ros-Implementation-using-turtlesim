#!/usr/bin/env python3
#code to move turtle in turtlesim to a goal using PID contoller

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt

class Turtle:
    def __init__(self):
        rospy.init_node('go_to_goal', anonymous = True)
        self.vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        self.pose = data

    def distance(self, goal):
        return sqrt(pow((goal.x - self.pose.x), 2) + pow((goal.y - self.pose.y), 2))

    def goToGoal(self):
        goal = Pose()
        goal.x = float(input("x: " ))
        goal.y = float(input("y: " ))

        tolerance = 0.1
        vel_msg = Twist()

        while self.distance(goal) >= tolerance:
            vel_msg.linear.x = 1.5 * self.distance(goal)
            vel_msg.angular.z = 6* (atan2(goal.y - self.pose.y, goal.x - self.pose.x) - self.pose.theta)

            self.vel_pub.publish(vel_msg)

            self.rate.sleep()

        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.vel_pub.publish(vel_msg)

        rospy.spin()

if __name__ == '__main__':
    try:
        x = Turtle()
        x.goToGoal()
    except rospy.ROSInterruptException:
        pass

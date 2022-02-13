#!/usr/bin/env python3

import rospy
import numpy as np
from nav_msgs.msg import OccupancyGrid, Path
from geometry_msgs.msg import PoseStamped   

class sahayak:
    def __init__(self):
        rospy.init_node('a_star', anonymous = True)
        self.path_pub = rospy.Publisher('/path', Path, queue_size=10)
        self.goal_sub = rospy.Subscriber('/move_base_simple/goal', PoseStamped, self.update_goal)
        self.map_sub = rospy.Subscriber('/map', OccupancyGrid, self.update_map)
        self.map_pub = rospy.Publisher('/my_map', OccupancyGrid, queue_size=10)

        self.path = Path()
        self.goal = PoseStamped()
        self.map = OccupancyGrid()

        self.have_goal = False
        self.have_map = False

        self.modified_goal_x = 0
        self.modified_goal_y = 0

    def update_goal(self, data):
        self.goal = data
        self.have_goal= True

    def update_map(self, data):
        self.map = data
        self.have_map = True

    def show(self):
        print("Starting...")

        while not rospy.is_shutdown():
            if(self.have_map and self.have_goal):
                print(self.goal.pose.position.x, self.goal.pose.position.y, self.goal.pose.position.z)

                x = int(self.goal.pose.position.x/0.03 + 1661)
                y = int(self.goal.pose.position.y/0.03 + 1661)

                print(x, y)

                p = int(x*3328 + y)
                print(self.map.data[p])

                print("OPP")
                p = int(y*3328 + x)
                print(self.map.data[p])

                path = Path()
                path.header.seq = self.map.header.seq
                path.header.stamp = rospy.Time.now()
                path.header.frame_id = self.map.header.frame_id

                x=y=0
                for i in range(100):

                    f = PoseStamped()
                    f.pose.position.x = (1661 - x)*0.03
                    f.pose.position.y = (1661 - y)*0.03
                    x-=1
                    y-=1

                    path.poses.append(f)
                
                self.path_pub.publish(path)
                p = input("H")
                '''
                occupancy = np.zeros((3328, 3328))
                for i in range(3328):
                    for j in range(3328):
                        p = i*3328 + j
                        occupancy[i][j] = self.map.data[p]

                mymap = OccupancyGrid()
                
                for i in range(3328):
                    for j in range(3328):
                        mymap.data.append(occupancy[i][j])
                         
                print("publishing")
                self.map_pub.publish(mymap)

                rospy.spin()
                '''

if __name__ == '__main__':
    try:
        x = sahayak()
        x.show()
    except rospy.ROSInterruptException:
        pass
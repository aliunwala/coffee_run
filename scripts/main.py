#!/usr/bin/env python

import roslib; roslib.load_manifest('coffee_run')
import rospy
import actionlib
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped
from move_base_msgs.msg import MoveBaseAction

def coffee_run():
    rospy.init_node('coffee_run', anonymous=True)
    r = rospy.Rate(10) # 10hz
    #pub = rospy.Publisher('move_base_simple/goal', PoseStamped)
    #while not rospy.is_shutdown():
        #pubdata = PoseStamped()
        #rospy.loginfo(pubdata)
        #pub.publish(pubdata)
        #r.sleep()

    client = actionlib.SimpleActionClient("move_base/goal", MoveBaseAction)
    rospy.loginfo("Waiting For Server")
    client.wait_for_server()
    #goal = MoveBaseAction()
    #client.send_goal(goal)
    #rospy.loginfo("Goal to Elevator Sent")
    rospy.loginfo("Moving to Elevator Now")
    #client.wait_for_result(rospy.Duration.from_sec(5.0))


if __name__ == '__main__':
    try:
        coffee_run()
    except rospy.ROSInterruptException: pass

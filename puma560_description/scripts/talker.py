#!/usr/bin/env python

import sys

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float64

def talker():
    pub_waist = rospy.Publisher('/puma560/joint_waist_position_controller/command', Float64, queue_size=10)
    pub_shoulder = rospy.Publisher('/puma560/joint_shoulder_position_controller/command', Float64, queue_size=10)
    pub_elbow = rospy.Publisher('/puma560/joint_elbow_position_controller/command', Float64, queue_size=10)
    pub_bend = rospy.Publisher('/puma560/joint_wrist_bend_position_controller/command', Float64, queue_size=10)
    pub_roll = rospy.Publisher('/puma560/joint_wrist_roll_position_controller/command', Float64, queue_size=10)
    pub_lgrip = rospy.Publisher('/puma560/joint_left_gripper_position_controller/command', Float64, queue_size=10)
    pub_rgrip = rospy.Publisher('/puma560/joint_right_gripper_position_controller/command', Float64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
    #hello_str = "hello world %s" % rospy.get_time()
    #rospy.loginfo(hello_str)
        if sys.argv[1]=='zero':
            pub_waist.publish(Float64(data=0))
            pub_shoulder.publish(Float64(data=0))
            pub_elbow.publish(Float64(data=0))
            pub_bend.publish(Float64(data=0))
            pub_roll.publish(Float64(data=0))
            pub_lgrip.publish(Float64(data=0))
            pub_rgrip.publish(Float64(data=0))
        elif sys.argv[1]=='home':
            pub_waist.publish(Float64(data=-1.47))
            pub_shoulder.publish(Float64(data=1.47))
            pub_elbow.publish(Float64(data=0))
            pub_bend.publish(Float64(data=0))
            pub_roll.publish(Float64(data=0))
            pub_lgrip.publish(Float64(data=0))
            pub_rgrip.publish(Float64(data=0))
        else:
            pub_waist.publish(Float64(data=float(sys.argv[1])))
            pub_shoulder.publish(Float64(data=float(sys.argv[2])))
            pub_elbow.publish(Float64(data=float(sys.argv[3])))
            pub_bend.publish(Float64(data=float(sys.argv[4])))
            pub_roll.publish(Float64(data=float(sys.argv[5])))
            pub_lgrip.publish(Float64(data=float(sys.argv[6])))
            pub_rgrip.publish(Float64(data=float(sys.argv[6])))
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

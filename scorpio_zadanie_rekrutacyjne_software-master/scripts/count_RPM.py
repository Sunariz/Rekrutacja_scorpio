#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import UInt16
from std_msgs.msg import Float32

start_position = 0
start_time = time.time()

def UInt16_callback(msg: UInt16):
    global start_position
    global start_time
    rospy.loginfo(str(time.time()) + str(msg))

    position = int(str(msg)[6::])

    posittion_difference = position - start_position

    if abs(posittion_difference) > abs(position - 4096+start_position):
        posittion_difference = position - 4096+start_position

    RPM = Float32()
    RPM = Float32(posittion_difference/4096*2*3.14/(time.time()-start_time)) # predkosc katowa wyrazona w radianach na sekunde

    start_position = position
    start_time = time.time()

    pub.publish(RPM)


if __name__ == '__main__':
    rospy.init_node("count_RPM")
    rospy.loginfo("Node has been started.")
    rate = rospy.Rate(2)

    pub = rospy.Publisher("/virtual_dc_motor_driver/get_velocity", Float32, queue_size=10)
    sub = rospy.Subscriber("/virtual_dc_motor/get_position", UInt16, callback=UInt16_callback)
        
    rospy.spin()

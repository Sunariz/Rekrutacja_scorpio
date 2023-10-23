#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8
from std_msgs.msg import Float32

def Float32_callback(msg: Float32):
    rospy.loginfo(str(msg))
    val = Int8(2)
    pub.publish(val)


if __name__ == '__main__':
    rospy.init_node("control_velocity")
    rospy.loginfo("Node has been started.")

    pub = rospy.Publisher("/virtual_dc_motor/set_cs", Int8, queue_size=10)
    sub = rospy.Subscriber("/virtual_dc_motor_controller/set_velocity_goal", Float32, callback=Float32_callback)
        
    rospy.spin()

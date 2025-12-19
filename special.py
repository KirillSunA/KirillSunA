"""
CHANGE COLOR LIGHT BY CH6
"""
#!/usr/bin/env python3
import rospy
from mavros_msgs.msg import RCIn
from clover.srv import SetLEDEffect

last_state = None

def cb(msg):
    global last_state

    ch6 = msg.channels[5]  # CH6 = индекс 5
    state = ch6 > 1500     # True = захват включен

    if state == last_state:
        return  # ничего не менялось

    if state:
        set_led(effect='blink', r=255, g=0, b=0)  # захват ВКЛ
    else:
        set_led(effect='fill', r=0, g=0, b=255)   # захват ВЫКЛ

    last_state = state

rospy.init_node('gripper_led_indicator')
set_led = rospy.ServiceProxy('/led/set_effect', SetLEDEffect)
rospy.Subscriber('/mavros/rc/in', RCIn, cb)
rospy.spin()
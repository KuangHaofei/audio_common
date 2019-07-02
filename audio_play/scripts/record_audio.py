#!/usr/bin/env python
import numpy as np
import sounddevice as sd

import rospy
import os

if __name__ == '__main__':
    rospy.init_node("audio_talker", anonymous=True)
    host = rospy.get_param("host", "192.168.43.217")
    port = rospy.get_param("port", "5001")
    os.system("gst-launch-1.0 autoaudiosrc ! audioconvert ! audioresample ! alawenc ! rtppcmapay ! udpsink "
              "host={} port={}".format(host, port))

    rospy.spin()
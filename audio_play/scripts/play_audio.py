#!/usr/bin/env python
import rospy
import os

if __name__ == '__main__':
    rospy.init_node("audio_listener", anonymous=True)

    port = rospy.get_param('port', "5001")

    os.system("gst-launch-1.0 udpsrc port={} caps=\"application/x-rtp\" ! rtppcmadepay ! alawdec ! alsasink"
              .format(port))

    rospy.spin()
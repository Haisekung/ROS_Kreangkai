#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
import os

frame = Tk()
frame.title("GUINAJAEIEI")
frame.geometry("400x200")

rospy.init_node("GUI_Remote")
pub = rospy.Publisher("turtle1/cmd_vel",Twist, queue_size=10)

def fw():
	print("fw")
	cmd = Twist()
	cmd.linear.x = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	
def bw():
	print("bw")
	cmd = Twist()
	cmd.linear.x = -1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	
def sl():
	print("sl")
	cmd = Twist()
	cmd.linear.y = 1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	
def sr():
	print("sr")
	cmd = Twist()
	cmd.linear.y = -1.0
	cmd.angular.z=0.0
	pub.publish(cmd)
	
def rr():
	print("rr")
	cmd = Twist()
	cmd.linear.y = 0.0
	cmd.angular.z= -1.0
	pub.publish(cmd)
	
def rl():
	print("rl")
	cmd = Twist()
	cmd.linear.y = 0.0
	cmd.angular.z= 1.0
	pub.publish(cmd)
	
def back_gr():
	print("reset")
	os.system('rosservice call /reset')
	
B1 = Button(text = "FW", command=fw)
B1.place(x=73, y=20)

B2 = Button(text = "BW", command=bw)
B2.place(x=73, y=130)

B3 = Button(text = "SL", command=sl)
B3.place(x=20, y=80)

B4 = Button(text = "SR", command=sr)
B4.place(x=128, y=80)

B5 = Button(text = "RR", command=rr)
B5.place(x=328, y=80)

B6 = Button(text = "RL", command=rl)
B6.place(x=228, y=80)

B7 = Button(text = "RESET", command=back_gr)
B7.place(x=278, y=150)

frame.mainloop()


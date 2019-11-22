#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2019 Thomas Castleman <contact@draugeros.org>
#				  Ryan Coons <rcoons@unca.edu>
#				  Alexander Goldstaub <agoldsta@unca.edu>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
#This is the main file. We can call other files if we need to, but try to just define functions instead

#Import the Modules we need, preferably with only the functions and classes we need to reduce RAM usage
#use the system() command to run outside scripts
from os import system
#use argv to take input on the command line
from sys import argv
#import algorithim to use
import "dijkstra-algorithim.py"

#Define Functions
#Ajacentcy function
def ajac(Point_A,Point_B):
	#Vars should be lists of length 2 containing ints
	#check if point A and point B are ajacent to each other either horizontally,
	#vertically, or diagonally
	#Return 0 if horizontal
	#return 1 if vertical
	#return 2 if diagonal
	#return 3 if either:
	#	Point A IS Point B
	#	Point A and Point B ARE NOT ajacent

	#Are Point A and Point B the same?
	if (Point_A == Point_B):
		return 3
	#are point A and point B diagonal to each other
	elif ( ((Point_A[0] - 1) == Point_B[0]) or ((Point_A[0] + 1) == Point_B[0]) ) and ((Point_A[1] - 1) == Point_B[1]) or ((Point_A[1] + 1) == Point_B[1]):
		return 2
	#Are Point A and Point B vertical to each other
	elif ((Point_A[0] - 1) == Point_B[0]) or ((Point_A[0] + 1) == Point_B[0]):
		return 1
	#Are point A and Point B horizontal to each other
	elif ((Point_A[1] - 1) == Point_B[1]) or ((Point_A[1] + 1) == Point_B[1]):
		return 0
	#else
	else:
		return 3

#Check to make sure all points on route are connected
def check_connected(route_list):
	for each in range(0:len(route_list)):
		if ( route_list[each][1] == route_list[each + 1][0] ):
			continue
		else:
			return 1
	return 0


#Define Initial Variables
#Street List, this will be 2D
#This WAS a dictionary, until I realized that was egreegious and not needed
MAP = []

#Version of the project. Any time you make a major change, bump the number by one.
VERSION = "0.0.2-alpha1"
#Use argc so we don't go over the length of argv
argc = len(argv)

#Do all the I/O and processing we need
try:
	if (argc > 1):
		if (argv[1] == "-h" or argv[1] == "--help"):
			print("\nFor now, main.py does nothing other than print this help dialog and print the current version.")
		elif (argv[1] == "-v" or argv[1] == "--version"):
			print("\nCSCI-183 Project Version %s" % (VERSION))
		else:
			print("\nOption not supported. Please try '-h' or '--help'.")
	else:
		print("\nNo options passed. Exiting . . .")
except:
	print("\nAn error has occured.")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main.py
#
#  Copyright 2019 Thomas Castleman <contact@draugeros.org>
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

#Define Functions

#Define Initial Variables
#Version of the project. Any time you make a major change, bump the number by one.
VERSION = "0.0.1-alpha1"
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
except:
	print("\nAn error has occured.")

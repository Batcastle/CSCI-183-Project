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

############################################################

# Import the Modules we need, preferably with only the functions and classes we need to reduce RAM usage

# use the check_output() command to run outside scripts and return output
from subprocess import check_output

# use argv to take input on the command line
from sys import argv

# Treat 2D lists as R-style arrays
import numpy as np

##########################################################################

#Define Functions

#print 2D vector in a nice, easy to read method
def pretty_best_path_output(best_path,distance):
	print("START (%s)---> " % (best_path[0]),end="")
	for each in range(len(best_path) - 1):
		if (each == 0):
			continue
		print("%s ---> " % (best_path[each]), end="")
	print("END (%s)" % (best_path[len(best_path) - 1]))
	print("TOTAL DISTANCE: %s" % (distance))

#
def options(data):
    option_view = ''
    for i in data:
        option_view = option_view + ' ' + str(i)
    return(option_view)

#
def grab(data):
    lencheck = ''
    for i in data:
        lencheck = str(i)
    return(lencheck)

#
def cleanup(A):
	fresh = []
	for i in range(len(A)):
		if A[i] in fresh:
			continue
		else:
			fresh.append(A[i])
	return fresh

#
def Trueval(A,paths):
    pathval = []
    for i in range(len(paths)):
        total = 0
        for j in range(len(paths[i])):
            total = total + A[paths[i][j][0]][paths[i][j][1]]
        pathval.append(total)
    return(pathval)

#
def optimize(A,path):
    val = 9999999999999999999999999999999
    best = []
    Check = Trueval(A,path)
    for i in range(len(Check)):
        if (Check[i] < val):
            val = Check[i]
            best = i
    return([val,best])

# function to take easiest path and return it. Returns False if there is no valid path
def pathfinder(A,start,end):
	if (start > end):
		c = start
		start = end
		end = c
	B = np.array(list.copy(A))
	if (end == len(B[0])-1):
		adj = 1
	else:
		adj = 2
	row = 0
	col = start   #initialize row and column indices
	noback = []   #list that saves columns that cannot be returned to
	working_paths = []     #list of indices traversed, aka path taken
	path_attempt = []
	q = 0 #used for possible range vals
	p = 0 # ""
	while (p < len(B[0])):
		if (col == end):
			working_paths.append(path_attempt)
			path_attempt = []
			B = np.array(list.copy(A))
			q = q + 1
			row = 0
			col = start
			noback = []
			if ((len(B[0]) - q ) == 0):
				p = p + 1
				q = 0
			for i in range(p,len(B[0])-q):
				B[i] = 0
				B[:,i] = 0
		if (row > (len(B[0]) - adj)):
			B = np.array(list.copy(A))
			row = 0
			col = start
			noback = []
			path_attempt = []
			q = q + 1
			if ((len(B[0]) - q ) == 0):
				p = p + 1
				q = 0
			for i in range(p,len(B[0])-q):
				B[i] = 0
				B[:,i] = 0
		for i in noback:
			if (row == i):
				row = row + 1
		if (B[row][col] > 0):
			path_attempt.append([row,col])
			noback.append(col)
			col = row
			row = 0
		else:
			row = row + 1
	return(working_paths)

#
def run(A,D,LOCATIONS):
	p = ''
	q = cleanup(pathfinder(A[grab(A)],int(D[0])-1,int(D[1])-1))
	for i in range(D[2]):
		c = optimize(A[D[3+i]],q)
		path_list = []
		for i in range(len(q[c[1]])):
			if (i == 0):
				path_list.append(LOCATIONS[q[c[1]][i][1]])
			path_list.append(LOCATIONS[q[c[1]][i][0]])
		pretty_best_path_output(path_list,c[0])
	return print(p)


##########################################################################

#Define Initial Variables

#Version of the project. Any time you make a major change, bump the number by one.
VERSION = "0.1.0-alpha2"

#
Display=[]

#Use argc so we don't go over the length of argv
argc = len(argv)

################################################################################

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
		# All this is code to receive and translate output from main.R
		CSV_DATA = check_output(["./main.R"])
		# force into correct encoding
		CSV_DATA = str(CSV_DATA)
		# convert to list
		CSV_DATA = list(CSV_DATA)
		#delete unnecessary characters
		del(CSV_DATA[1])
		del(CSV_DATA[0])
		del(CSV_DATA[len(CSV_DATA) - 1])
		# rejoin
		CSV_DATA = "".join(CSV_DATA)
		# resplit into a list of strings, each string is a row in
		# the initial CSV file
		CSV_STRINGS = CSV_DATA.split("\\n")
		CSV_DATA = []
		for each in CSV_STRINGS:
			CSV_DATA.append(each.split())
		LOCATIONS = CSV_DATA[0]
		del(LOCATIONS[0])
		del(CSV_DATA[0])
		for each in range(0,(len(CSV_DATA) - 1)):
			del(CSV_DATA[each][1])
			del(CSV_DATA[each][0])
		for each in range(0,(len(CSV_DATA) - 1)):
			for each1 in range(0,(len(CSV_DATA[each]) - 1)):
				if (CSV_DATA[each][each1] == "NA"):
					CSV_DATA[each][each1] = 0
		for each in range(0,(len(CSV_DATA) - 1)):
			for each1 in range(0,(len(CSV_DATA[each]))):
				CSV_DATA[each][each1] = int(CSV_DATA[each][each1])
		del(CSV_DATA[len(CSV_DATA) - 1])
		A = {"FlightPath":CSV_DATA}
		# CSV_DATA contains data more easily refrenced by Python
		# CSV_STRINGS contains the same data, but in a more human-readable format
		print('Parameters for Start Location/End Location are the integers 1-' + str(len(A[grab(A)][0])))
		for each in range(1,len(LOCATIONS) + 1):
			print("%s : %s" % (each, LOCATIONS[each - 1]))
		try:
			Display.append(int(input('\nStart Location: ')))
			Display.append(int(input('\nEnd Location: ')))
			Display.append(int(input('\nAmount of variables (options will include: ' + str(options(A)) + ' ): ')))
			for i in range(0,Display[2]):
				Display.append(input('\nVariable ' + str(i + 1) + '\n'))
			run(A,Display,LOCATIONS)
		except Exception as err:
			print('Please pay attention to the prompts and enter the data exactly as displayed, keep in mind that each word in the options is a different variable name ')
			print("ERROR: %s " % (err))


except Exception as err:
	print("\nAn error has occured.")
	print("ERROR: %s " % (err))

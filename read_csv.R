#!/usr/bin/Rscript
# -*- coding: utf-8 -*-
#
#  main.R
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
#Main R File
# Get list of options passed
argv = commandArgs(trailingOnly=TRUE)
argc = length(argv)
# set output "window"
options(width=10000)
VERSION = "0.0.3-alpha1"

if ( argc >= 1 ){
	# Help and version options
	if (argv[1] == "-h" | argv[1] == "--help"){
		cat("main.R is used to read the file 'flightmap.csv' in the same directory as this file, and is only supposed to be called by 'main.py'.Please only interact with 'main.py' from command line.")
	} else if (argv[1] == "-v" | argv[1] == "--version"){
		cat(VERSION)
	} else {
		cat("Option not supported. Please try '-h' or '--help'.")
	}
} else {
	# Read CSV
	flightmap = read.csv("flightmap.csv")
	# print just the data we needed
	print(flightmap[1:10,1:11])
}

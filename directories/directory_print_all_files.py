# Purpose:  Print all files inside a directory using DFS traversal
#           Does not print directory or root

# Import the os library
import os

# For the root, directory, and files in .\ directory
for root, directory, files in os.walk('.'):
	# If the directory list is [] then we are in the bottom file
	if len(directory) == 0:
		for file in files:
			print "File: " + file
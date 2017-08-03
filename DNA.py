#  File: DNA.py

#  Description: find longest common base sequence in two DNA strands

#  Student Name: Eun Seo

#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created: 10/13/15

#  Date Last Modified: 10/13/15

def main():
 import string

 # read file
 in_file = open("dna.txt", "r")

 # read line by line
 num_pairs = in_file.readline()
 # clean up input
 num_pairs = num_pairs.strip()
 # convert str to int
 num_pairs = int(num_pairs)
 # read all pairs of dna strands
 
 for i in range (num_pairs):
 	# read 1st str
 	st1 = in_file.readline()
 	st2 = in_file.readline()
 	# sanitize data
 	st1 = st1.strip()
 	st2 = st2.strip()
 	# make data uppercase
 	st1 = st1.upper()
 	st2 = st2.upper()

 	# order strand by size 
 	print("Pair ", i+1, ": ", end="", sep = "")
 	
 	if(len(st1) > len(st2)):
 		dna1 = st1
 		dna2 = st2
 	else:
 		dna1 = st2
 		dna2 = st1

 	# get all substr of dna2
 	flag = True
 	window = len(dna2)
 	while (window > 1):
 		start = 0
 		if (flag == False):
 			break
 		while ((start + window) <= len(dna2)):
 			substrand = dna2[start : start + window]
 			if (dna1.find(substrand) == -1):
 				pass
 			else:
 				match = dna2[start:start + window]
 				if (flag == False):
 					print("        ", match)
 				else:
 					print(match)
 				flag = False
 			start += 1

 		# when match not found, decrease window
 		if (flag == True):
 			window -=1
 		if (window == 1):
 			print("No common sequence found")

 # close files
 in_file.close()

main()
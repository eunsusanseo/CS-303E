#  File: ISBN.py

#  Description: program to verify valid ISBNs

#  Student Name: Eun Seo

#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created: 10/20/15

#  Date Last Modified: 10/20/15

def main():
 import string

 # read file
 in_file = open("ISBN.txt", "r")
 
 # write to new file
 out_file = open("isbnOut.txt", "w")


 # read ISBN line by line as a string
 flag = True
 
 for line in in_file:
 	ISBN = line.strip()

 	line = line.strip() # strip newline ch
 	line = line.replace("-", "") # remove "-"

 	sum_line = 0

 	if (line[-1] == "x") or (line[-1] == "X"):
 		flag = False
 		sum_line += 10
 		line = line.replace("x", "")
 		line = line.replace("X", "")
 	else:
 		flag = True

 	if line[:9].isdigit(): # check until last digit
 		# check if last digit X
 		isbn = []
 		for i in range (len(line)):
 			isbn.append(line[i]) # isbn = now a list
		
 		# NEED FIRST CUMULATIVE SUM
 		isbn_s1 = []
 		s1 = 0
 		for i in range(len(isbn)):
 			# must change to int bc ch_list is a string
 			ch = int(isbn[i])
 			s1 += ch
 			isbn_s1.append(s1)
 		
 		if (flag == True):
 			isbn_s1 = isbn_s1
 		if (flag == False): 
 			isbn_s1.append(s1+sum_line)
 		#print(isbn_s1)
 		#print(flag)

 		# NEED 2ND CUMULATIVE SUM
 		# add s1 partial sum of ISBN
 		isbn_s2 = []
 		s2 = 0
 		for i in range(len(isbn_s1)):
 			# must change to int bc ch_list is a string
 			ch2 = int(isbn_s1[i])
 			s2 += ch2
 		# print(s2)

 		if (s2 % 11 == 0):
 			out_file.write(ISBN + " valid\n")
 		else:
 			out_file.write(ISBN + " invalid\n") #incorrect
 	else: 
 		out_file.write(ISBN + " invalid\n")
 	
 in_file.close()
 out_file.close()

main()

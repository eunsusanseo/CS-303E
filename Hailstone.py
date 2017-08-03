#  File: Hailstone.py

#  Description: Get number with longest cycle length

#  Student Name: Eun Seo

#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created: 9/19/15

#  Date Last Modified: 9/19/15


def main():
 
 # declare variables
 n_count = 0
 count = 0
 max_count = 0
 max_num = 0

 # prompt user for input
 beg = int(input("Enter starting number of the range: "))
 end = int(input("Enter ending number of the range: "))

 # check if both numbers positive
 while (beg <= 0 or end <= 0 or beg >= end):
 	 beg = int(input("Enter starting number of the range: "))
 	 end = int(input("Enter ending number of the range: "))

 while (beg <= end):
     count = 0
     start_n = beg
     n = beg
     while (n > 1):
         if (n % 2 == 0):
             n = n // 2
             count = count + 1
         else:
             n = n * 3 + 1
             count = count + 1
     
     if (count >= max_count):
         max_count = count
         max_num = start_n
     else:
         max_count = max_count
     beg = beg + 1
 
 message = "The number %s has the longest cycle length of %s." %(max_num, max_count)

 print(message)

main()

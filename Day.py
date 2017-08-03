#  File: Day.py

#  Description: Print out day of the week for input date

#  Student Name: Eun Seo

#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created: 9/13/15

#  Date Last Modified: 9/13/15

# add in code for leap year

# NOTES: while - indefinite; if - loops once
def main():

# input year and check range
 c = int(input("Enter year: "))
 
 while (c < 1900) or (c > 2100):
 	c = int(input("Enter year: "))
 	
# input month and check range
 a = int(input("Enter month: "))
 
 while (a < 1) or (a > 12):
 	a = int(input("Enter month: "))

# input day and check range
 b = int(input("Enter day: "))

 while (((a == 1) or (a == 3) or (a == 5) or (a == 7) or (a == 8) or (a == 10) or (a == 12)) and (b > 31)):
 		b = int(input("Enter day: "))

 while (((a == 4) or (a == 6) or (a == 9) or (a == 11)) and (b > 30)):
 		b = int(input("Enter day: "))

 while (((a == 2) and ((c % 400 == 0) or (c % 4 == 0 and c % 100 != 0))) and (b > 29)):
		b = int(input("Enter day: "))

 while (((a == 2) and ((c % 400 != 0) or (c % 4 != 0 and c % 100 != 0))) and (b > 28)):
 		b = int(input("Enter day: "))

# change input month to new calendar month
 if (a == 1):
 	a = 11
 elif (a == 2):
 	a = 12
 elif (a == 3):
 	a = 1
 elif (a == 4):
 	a = 2	
 elif (a == 5):
 	a = 3	
 elif (a == 6):
 	a = 4	
 elif (a == 7):
 	a = 5	
 elif (a == 8):
 	a = 6	
 elif (a == 9):
 	a = 7	
 elif (a == 10):
 	a = 8	
 elif (a == 11):
 	a = 9	
 else:
 	a = 10

# change input year to new calendar year
 if (a == 11) or (a == 12):
 	c = c - 1
 else:
 	c = c

# calculate century
 d = c // 100

# calculate year of the century
 c = c % 100

# algorithm to find day 
 w = (13 * a - 1 ) // 5 
 x = c // 4 
 y = d // 4 
 z = w + x + y + b + c - 2 * d 
 r = z % 7 
 r = (r + 7) % 7

# output day of week
 if (r == 0):
 	print("The day is Sunday.")
 elif (r == 1):
 	print("The day is Monday.")
 elif (r == 2):
 	print("The day is Tuesday.")
 elif (r == 3):
 	print("The day is Wednesday.")
 elif (r == 4):
 	print("The day is Thursday.")
 elif (r == 5):
 	print("The day is Friday.")
 else:
 	print("The day is Saturday.")

main()
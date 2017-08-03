
#  File: EasterSunday.py

#  Description: Caculate Easter Sunday

#  Student Name: Eun Seo

#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created: 09-08-15

#  Date Last Modified: 09-08-15

def main():

# input
 y = eval(input("Enter year: "))

# compute p (day)
 a = y % 19
 b = y // 100
 c = y % 100
 d = b // 4
 e = b % 4
 g = (8 * b + 13) // 25
 h = (19 * a + b - d - g + 15) % 30
 j = c // 4
 k = c % 4
 m = (a + 11 * h) // 319
 r = (2 * e + 2 * j - k - h + m + 32) % 7
 n = (h - m + r + 90) // 25
 p = (h - m + r + n + 19) % 32

# compute n (month)
 if (n == 3):
 	month = "March"
 if (n == 4):
 	month = "April"
 	
# output
 print("In {} Easter Sunday is on {} {}.".format(y, p, month))

main ()
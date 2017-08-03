#  File: CalculatePI.py

#  Description: calculate PI and difference given num and see if accuracy of PI increasees with number of throws

#  Student Name: Eun Seo
 
#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created: 10-03-15

#  Date Last Modified: 10-03-15

import math
import random

# stimulate throw of dart by generating random numbers for x and y coordinates
# determine if randomly generated point inside circle
# do as many times as posssible as specified by number of throws
# keep count 
def computePI(numthrows, numthrows2):
	calculated_PI = (numthrows / numthrows2) * 4
	return calculated_PI

# call function computePI for gien number of throws
def main():
	# ask for number of throws
	num = int(input("Enter number of throws: "))
	within_circle = 0

	# determine if randomly generated point inside the circle
	for num in range (num + 1):
		xPos = 0
		yPos = 0

		# generate random numbers
		xPos = float(random.uniform(-1.0, 1.0))
		yPos = float(random.uniform(-1.0, 1.0))

		# calculate length of hypot
		hypot = math.hypot(xPos, yPos)

		if (hypot < 1):
			within_circle += 1
	# calculated PI
	calculated_PI = computePI(within_circle, num)
	difference = calculated_PI - math.pi

	print("num =", '{:<10}'.format(num), "Calculated Pi =", format(calculated_PI,'.6f'), "  Difference =", format(difference, '+.6f'))
main()

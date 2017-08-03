#  File: GuessingGame.py

#  Description: program to guess number

#  Student Name: Eun Seo

#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created: 10/29/15

#  Date Last Modified: 10/29/15

import random
def main():
	print("Guessing Game")
	print()
	print("Think of a number between 1 and 100 inclusive.")
	print("And I will guess what it is in 7 tries or less.")
	print()
	response = str(input("Are you ready? (y/n): "))
	print()
	while (response != "n"):
		if (response != "y"):
			response = str(input("Are you ready? (y/n): "))
		elif (response == "y"):
				lo = 1
				hi = 101
				guess_count = 1
				answer = ""
				mid = random.randint(lo, hi)

				for guess_count in range (1, 8):
					print("Guess %d: The number you thought was %d" %(guess_count, mid))
					answer = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
					print()
					
					while (ans(answer) == False):
						print("Guess %d: The number you thought was %d" %(guess_count, mid))
						answer = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
						print()
					
					if (answer == "1"):
						hi = mid
						mid = guess(answer, mid, lo, hi)
					elif (answer == "-1"):
						lo = mid
						mid = guess(answer, mid, lo, hi)
					elif (answer == "0"):
						print("Thank you for playing the Guessing Game.")
						exit()
				print("Either you guessed a number out of range or you had an incorrect entry.")
				exit()

	print("Bye")
	exit()

def ans(ans):
	if (ans == "1") or (ans == "0") or (ans == "-1"):
		return ans
	else:
		return False

def guess(user_answer, middle, low, high):
	if (user_answer == "1"):
		middle  = (low + high) // 2
		return middle
	elif (user_answer == "-1"):
		middle  = (low + high) // 2
		return middle
	elif (user_answer == "0"):
		print("Thank you for playing the Guessing Game.")
		exit()
	
main()
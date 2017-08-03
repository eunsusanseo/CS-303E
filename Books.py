#  File: Books.py 

#  Description: See which author's vocabulary is more extensive

#  Student Name: Eun Seo

#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created:  11/24/15

#  Date Last Modified: 11/30/15

def create_word_dict():
	global word_dict
	word_dict = {}

	dict1 = open("./words.txt", 'r')
	
	for word in dict1:
		word = word.strip()
		
		if word in word_dict:
			word_dict[word] += 1
		else:
			word_dict[word] = 1
	
	dict1.close()
	return word_dict

# 4. Remove apostrophes and punctuation marks
def parseString(st):
	# start out with empty filter_strings
	s = ""
	
	for i in range (len(st)):
		if (st[i].isalpha() == True) or (st[i].isspace() == True):
			s += st[i]
		elif (st[i] == "\'") and (st[i+1] != "s"):
			s += st[i]
		elif (st[i] >= "a") and (st[i] <= "z"):
			s += st[i]
		else:
			s += " "
	return s

def getWordFreq(file_name):	
	global word_dict
	create_word_dict()

	# open file for reading
	in_file = open(file_name, 'r')

	# create empty dictionary for word_freq
	word_freq = {}
	# create empty set for unique words
	word_set = set()

	for line in in_file:
		line = line.strip()
		line = parseString(line)

		words = line.split()

		# adding word to list
		for word in words:
			word_set.add(word)

		# adding word to dictionary	
			if word in word_freq:
				word_freq[word] = word_freq[word] + 1
			else:
				word_freq[word] = 1
	in_file.close()

	# convert word_set into word_list
	#word_list = list(word_set)

	# find capital words and add to capital_list
	capital_list = []
	for word in word_freq:
		if word[0].isupper() == True:
			capital_list.append(word)

	# check if uppercase word is equal to lowercase word
	for word in capital_list:
		lowercase_word = word.lower()
		# check if lower case word exists in word_freq dictionary
		if word in word_freq:
			if (lowercase_word in word_dict):
				word_freq[lowercase_word] = word_freq[word]
				# remove word from word_freq
				del word_freq[word]
			elif (lowercase_word in word_set):
				word_freq[lowercase_word] += word_freq[word]
				del word_freq[word]
			else:
				del word_freq[word]
	return word_freq

def wordComparison (author1, freq1, author2, freq2):
	# AUTHOR 1
	# create distinct word list1 (words without duplicates)
	distinct_words1 = len(freq1)

	# initialize total words for 1
	total_words1 = 0
	
	for word1 in freq1:
		total_words1 += freq1[word1]

	word_percentage1 = (distinct_words1 / total_words1) * 100


	#AUTHOR2
	# create distinct word list2 (words without duplicates)
	distinct_words2 = len(freq2)

	# initialize total words for 1
	total_words2 = 0
	
	for word2 in freq2:
		total_words2 += freq2[word2]

	word_percentage2 = (distinct_words2 / total_words2) * 100

	# AUTHOR 1
	print(author1)
	print("Total distinct words = ", distinct_words1)
	print("Total words (including duplicates) = ", total_words1)
	print("Ratio (% of total distinct words to total words) = ", word_percentage1)
	print()

	# AUTHOR 2
	print(author2)
	print("Total distinct words = ", distinct_words2)
	print("Total words (including duplicates) = ", total_words2)
	print("Ratio (% of total distinct words to total words) = ", word_percentage2)
	print()

	# create two sets with list of keys from two word frequency dictionaries
	freq_author1 = set(freq1)
	freq_author2 = set(freq2)

	# words that author1 used but author2 did not use
	# difference between two frequencies
	difference1 = freq_author1 - freq_author2
	frequency_diff1 = 0

	for diff in difference1:
		frequency_diff1 += freq1[diff]

	# express difference as percentage
	diff_percentage1 = (frequency_diff1 / total_words1) * 100

	# words that author2 used but author1 did not use
	difference2 = freq_author2 - freq_author1
	frequency_diff2 = 0

	for diff in difference2:
		frequency_diff2 += freq2[diff]

	# express difference as percentage
	diff_percentage2 = (frequency_diff2 / total_words2) * 100

	# PRINT OUTPUT
	print(author1, "used", len(difference1), "words that", author2, "did not use.")
	print("Relative frequency of words used by", author1, "not in common with ", author2, "=", diff_percentage1)
	print()
	print(author2, "used", len(difference2), "words that", author1, "did not use.")
	print("Relative frequency of words used by", author2, "not in common with ", author1, "=", diff_percentage2)

def main():
	global word_dict

	# create word dictionary from comprehensive Scrabble word list 
	create_word_dict()
	
	book1 = input("Enter name of first book: ")
	book2 = input ("Enter name of second book: ")
	print()
	
	# Enter names of the two authors
	author1 = input ("Enter last name of first author: ")
	author2 = input ("Enter last name of second author: ")
	print()
	
	# Get the frequency of words used by the two authors
	wordFreq1 = getWordFreq (book1)
	wordFreq2 = getWordFreq (book2)

	# Compare the relative frequency of uncommon words used by the two authors
	wordComparison (author1, wordFreq1, author2, wordFreq2)

main()

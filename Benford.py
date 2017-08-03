#  File: Benford.py 

#  Description: Using benford's law

#  Student Name: Eun Seo

#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created:  11/21/15

#  Date Last Modified: 11/22/15

def processLine(pop_num, pop_freq):
  if '1' in pop_num:
    pop_freq['1'] += 1
  elif '2' in pop_num:
    pop_freq['2'] += 1
  elif '3' in pop_num:
    pop_freq['3'] += 1
  elif '4' in pop_num:
    pop_freq['4'] += 1
  elif '5' in pop_num:
    pop_freq['5'] += 1
  elif '6' in pop_num:
    pop_freq['6'] += 1 
  elif '7' in pop_num:
    pop_freq['7'] += 1
  elif '8' in pop_num:
      pop_freq['8'] += 1
  elif '9' in pop_num:
    pop_freq['9'] += 1
  else:
    pop_freq['0'] += 1


def main():
  # open file for reading
  in_file = open ("./Census_2009.txt", "r")

  # ignore first line, store as header
  header = in_file.readline()

  pop_list = []
  pop_freq = {}
  # read subsequent lines
  pop_freq['0'] = 0
  pop_freq['1'] = 0
  pop_freq['2'] = 0
  pop_freq['3'] = 0
  pop_freq['4'] = 0
  pop_freq['5'] = 0
  pop_freq['6'] = 0
  pop_freq['7'] = 0
  pop_freq['8'] = 0
  pop_freq['9'] = 0
  
  for line in in_file:
    # initialize dictionary
    line = line.strip()
    pop_data = line.split()
    # ['State', 'City', 'population']
    # get very last number, population in list
    pop_num = pop_data[-1]
    pop_first_num = pop_num[0]
    processLine(pop_first_num, pop_freq)
  pop_pairs = list(pop_freq.items())
  
  
  items = [[x, y] for (x, y) in pop_pairs]
  items.sort()

  item_sum = 0
  for i in range (1, len(items)):
    item_sum += (items[i][1])

  print("Digit", "\t", "Count", "\t", "%")
  for i in range (1, len(items)):
    digit = (items[i][0])
    count = (items[i][1])
    percentage = ((items[i][1])/item_sum)*100
    print("%s \t %i \t %.1f" %(digit, count, percentage))

  in_file.close()

main()
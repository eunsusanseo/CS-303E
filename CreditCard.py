#  File: CreditCard.py

#  Description: program to check CC #s

#  Student Name: Eun Seo

#  Student UT EID: es29857

#  Course Name: CS 303E

#  Unique Number: 50470

#  Date Created: 10/24/15

#  Date Last Modified: 10/24/15
import sys
def main():
    
    num = int(input("Enter a 15 or 16-digit card number: "))
    num = str(num)
    flag = True 
    num = is_valid(num)

    if (num == False):
        print("Not a 15 or 16-digit number")
        sys.exit()
    else:
        if (len(num) == 16):
            if ((num[0] == 3 and num[1] == 4) and (num[0] == 3 and num[1] == 7)):
                print("Valid American Express credit card number")
                sys.exit()
            elif (((num[0] == "3" and num[1] == "4") or (num[0] == "3" and num[1] == "7")) or ((num[0] == "6" and num[1] == "0" and num[2] == "1" and num[3] == "1") or (num[0] == "6" and num[1] == "4" and num[2] == "4") or (num[0] == "6" and num[1] == "5")) or ((num[0] == "5" and num[1] == "0") or (num[0] == "5" and num[1] == "1") or (num[0] == "5" and num[1] == "2") or (num[0] == "5" and num[1] == "3") or (num[0] == "5" and num[1] == "4") or (num[0] == "5" and num[1] == "5")) or (num[0] == "4")):
                idx_odd = 1
                sum_odd = 0
                while (idx_odd < len(num)):
                    odd = 0
                    odd = 2 * int(num[idx_odd])
                    sum_odd += odd
                    idx_odd += 2
    
            # multiply, sum even numbers
                idx_even = 0
                sum_even = 0
                while (idx_even < len(num)):
                    even = 0
                    even = int(num[idx_even])
                    sum_even += even
                    idx_even += 2
                    final_sum = sum_odd + sum_even
                    cc_type(num)
                else:
                    print("Invalid credit card number")
                    sys.exit()
            else:
                if (num[0] == "1"):
                    print("Invalid credit card number")
                    sys.exit()
                else:
                    print("Valid credit card number")
                    sys.exit()
        elif (len(num) == 15) or (flag == False):
            idx_odd = 1
            sum_odd = 0
            while (idx_odd < len(num)):
                odd = 0
                odd = 2 * int(num[idx_odd])
                sum_odd += odd
                idx_odd += 2
    
            # multiply, sum even numbers
            idx_even = 0
            sum_even = 0
            while (idx_even < len(num)):
                even = 0
                even = int(num[idx_even])
                sum_even += even
                idx_even += 2
                final_sum = sum_odd + sum_even
                cc_type(num)
            else:
                print("Invalid credit card number")
                sys.exit()


# CHECK FOR VALID CC NUMBER
def is_valid(cc_num):
    if ((len(cc_num) == 15) or (len(cc_num) == 16)):
        return cc_num
    else:
        return False
    
def cc_type(cc_num):
    if ((cc_num[0] == "3" and cc_num[1] == "4") or (cc_num[0] == "3" and cc_num[1] == "7")):
        print("Valid American Express credit card number")
        sys.exit()
    elif ((cc_num[0] == "6" and cc_num[1] == "0" and cc_num[2] == "1" and cc_num[3] == "1") or (cc_num[0] == "6" and cc_num[1] == "4" and cc_num[2] == "4") or (cc_num[0] == "6" and cc_num[1] == "5")):
        print("Valid Discover credit card number")
        sys.exit()
    elif ((cc_num[0] == "5" and cc_num[1] == "0") or (cc_num[0] == "5" and cc_num[1] == "1") or (cc_num[0] == "5" and cc_num[1] == "2") or (cc_num[0] == "5" and cc_num[1] == "3") or (cc_num[0] == "5" and cc_num[1] == "4") or (cc_num[0] == "5" and cc_num[1] == "5")):
        print("Valid MasterCard credit card number")
        sys.exit()
    elif (cc_num[0] == "4"):
        print("Valid Visa credit card number")
        sys.exit()
    else:
        print("Valid  credit card number")
        sys.exit()

main()
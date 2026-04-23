#Used https://docs.python.org/3/library/re.html to learn about regular expression and used minimal AI to debug during implementation.

import re

#Make sure user inputs two integers between 1 and 8 separated by a space.
def int_check(i):
    pattern = r"^[1-8] [1-8]$"

    if re.fullmatch(pattern, i):
        #print(i)
        return i.split()
        
    else:
        #Ask again if entered incorrectly
        return int_check(input("This is an invalid placement input. Please enter an integer for column and row between 1 and 8 separated by a space: "))

#Make sure the user inputs "y" or "n"
def response_check(a):
    response1 = r"^y"
    response2 = r"^n"
    if re.fullmatch(response1, a) or re.fullmatch(response2, a):
        return a
    else:
        #Ask again if entered incorrectly
        return response_check(input("Please respond y or n: "))

if __name__ == "__main__":
    print(int_check(input()))
    #response_check(input("y/n: "))
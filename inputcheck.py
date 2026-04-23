import re

#Make sure user inputs two integers between 1 and 8 separated by a space.
def intcheck(i):
    pattern = r"^[1-8] [1-8]$"

    if re.fullmatch(pattern, i):
        #print(i)
        return i.split()
        
    else:
        #Ask again if entered incorrectly
        return intcheck(input("This is an invalid input. Please enter an integer for column and row between 1 and 8 separated by a space: "))

#Make sure the user inputs "y" or "n"
def responsecheck(a):
    response1 = r"^y"
    response2 = r"^n"
    if re.fullmatch(response1, a) or re.fullmatch(response2, a):
        return a
    else:
        #Ask again if entered incorrectly
        return responsecheck(input("Please respond y or n: "))




if __name__ == "__main__":
    print(intcheck(input()))
    #responsecheck(input("y/n: "))
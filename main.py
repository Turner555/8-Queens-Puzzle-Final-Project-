from check import check

print("Hello, and welcome to The Royal Standoff!")
print("To begin, please place your first queen.")
queen_1 = input("What colum and row have you placed the queen on (e.g. 1 3): ")
column = (int(queen_1.split()[0]) - 1)
row = int(queen_1.split()[1])
print(check(queen_1))
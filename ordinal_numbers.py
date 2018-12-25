#print out numbers 1-9 and print with correct ordinal listing

numbers = list(range(1,10))
# print(numbers)

for number in numbers:
    if number == 1:
        print(str(number) +"st")
    if number == 2:
        print(str(number) +"nd")
    if number == 3:
        print(str(number) +"rd")
    if number > 3:
        print(str(number) +"th")
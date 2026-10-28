#This program asks for a number and checks which numbers it is divisible by.
number = int(input("Enter a number: "))
numbers = range(1, int(number)+1)
result = []
for num in numbers:
    if number % num == 0: # numerator / denominator must be 0 otherwise it does not work
        result.append(num)
        print(num)
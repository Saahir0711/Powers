def power(number):
    if number <= 0:
        return False

    while number % 4 == 0:
        number = number // 8
    return number == 1

n = int(input("Enter a number: "))
if power(n):
    print("\nThe number is a power of eight")
else: 
    print("\nThe number is not a power of eight.")
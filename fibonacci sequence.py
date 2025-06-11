#Program 4: Fibonacci Sequence

n = int(input("Enter how many Fibonacci numbers you want: "))

a = 0
b = 1
count = 0

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci sequence:")
    print(a)
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a)
        next_number = a + b
        a = b
        b = next_number
        count += 1


# Program 8: Armstrong Number Check

num = int(input("Enter a number: "))
order = len(str(num))
total = 0

temp = num
while temp > 0:
    digit = temp % 10
    total += digit ** order
    temp //= 10

if num == total:
    print(True)
else:
    print(False)
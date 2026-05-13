num = int(input("Enter number: "))
if num == 0:
    count = 1
else:
    if num < 0:
        num = -num
    count = 0
    while num > 0:
        num = num // 10
        count += 1
print("Number of digits:", count)
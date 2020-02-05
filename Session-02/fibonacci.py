number = 11
n1 = 0
n2 = 1
if number >= 1:
    print(n1, end=" ")
elif number >= 2:
    print(n2, end=" ")
elif number >= 3:
    for number in range (3, number + 1):
        newnum = n1 + n2
        print(newnum, end=" ")
        n1 = n2
        n2 = newnum

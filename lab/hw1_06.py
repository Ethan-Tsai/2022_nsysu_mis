def revNum(string):
    if len(string) == 0:
        return string
    else:
        return revNum(string[1:]) + string[0]

a = input("Please enter the numbers: ")
ans=revNum(a)
print(f'Reversed positive integer number:{ans}')
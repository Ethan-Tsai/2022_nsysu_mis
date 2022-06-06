
def print_multiplication_table(n):
    for i in range(1, n+1, 1):
        for k in range(1, n+1, 1):
            ans = i*k
            print(f'{ans:3d}', end=' ')
        print('\n')



key = 1

while key == 1:
    in_n = input("Please input n: ")
    n = int(in_n)
    if n >= 1:
        print_multiplication_table(n)
    else:
        key = 0
        print("bye.")

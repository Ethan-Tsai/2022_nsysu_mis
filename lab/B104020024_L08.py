# arr = [3, 5, 7, 9]
# output = []
# for a in arr:
#     output.append(a * 11)
# print(output)

arr = [3, 5, 7, 9]
print([a*11 for a in arr])

# arr = [1, 4, 7, 10, 13, 16, 19, 22]
# output = []
# for a in arr:
#     if '1' not in str(a):
#         output.append(a)
# print(output)

arr = [1, 4, 7, 10, 13, 16, 19, 22]
print([a for a in arr if str(1) not in str(a)])

# arr = list(range(1, 101))

# def is_prime(n):
#     ...

# output = []

# for a in arr:
#     if is_prime(a):
#         output.append('{} is prime'.format(a))
# # 把上面三行改成一個 comprehension

# print(output)
# print('has', len(output))

arr = list(range(1, 101))

def is_prime(n):
    if n<2:
        return 0
    key=1
    for i in range(2,n):    
        if n%i==0:
            key=0
    return key
      
print([f'{a} is prime'  for a in arr if is_prime(a)])

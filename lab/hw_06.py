from array import array

def findpo(ary,num):
    for i in range(1,len(ary)):
        if abs(ary[i-1]-num)<=abs(ary[i]-num):
            ans=i-1   
            break
    return ans

ary=[-40, -2, 1, 4, 6, 6, 10]
print(f'There is an array: {ary}')
a = input("Enter a target number: ")
num=int(a)
print(f'Output: {ary[findpo(ary,num)]}')

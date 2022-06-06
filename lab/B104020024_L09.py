import numpy as np


ary1=np.random.rand(15)*2
print(ary1)

print("2----------------------------------")
ary2=np.random.rand(36)*5
ary3=np.reshape(ary2,(6,6))
print(ary3)

print("3----------------------------------")
ary4=np.random.rand(27).reshape(3,3,3)
mean1=np.mean(ary4,axis=0)
mean2=np.mean(ary4,axis=2)
print(ary4)
print("------")
print(f'mean(axis=0): \n{mean1}')
print("------")
print(f'mean(axis=2): \n{mean2}')


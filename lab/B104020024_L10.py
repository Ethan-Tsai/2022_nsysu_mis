import numpy as np

mar1 = np.zeros((6, 6),dtype=int) #i assign int to delete dot.

for i in range(0,6):
    mar1[i:i+1,i:i+1]=i+1
    
print(mar1)

#1-2
print("-----next------")

print(mar1[2:5,1:5])

#2-1
print("-----next------")

mar2=np.random.rand(21)*2*np.pi
print(mar2)

#2-2
print("-----next------")

print(np.cos(mar2))
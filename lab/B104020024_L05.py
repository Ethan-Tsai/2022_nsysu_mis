from tkinter import N

data = {
    'n1': 0,
    'n2': 10
}

while True:
    inputs = input('Please input your operation:')
    inputs = inputs.split(' ')
    
    # using unpacking to get each parameters
    if len(inputs) == 1: # printall, delall  **新增mulall 將全部相乘
        op = inputs[0]
    elif len(inputs) == 2: # del, new
        ...
        op=inputs[0]
        del_new_num=inputs[1]
        # unpacking inputs to op and name variables
    elif len(inputs) == 3: # add, mul
        ...
        op=inputs[0]
        add_mul_num=inputs[1]
        n=inputs[2]
        num=int(n)
        # unpacking ...
    
    # handle operation logic
    if op == 'printall':
        print(data)
    elif op == 'delall':
        ...
        data={}
    elif op == 'del':
        ...
        del data[del_new_num]
    elif op == 'new':
        ...
        data[del_new_num]=0
    elif op == 'add':
        ...
        afteradd_num = num+data[add_mul_num]
        print(f'{data[add_mul_num]} + {num} = {afteradd_num}')
        data[add_mul_num]=afteradd_num
        # calculate
        # print "old_num + number = new_num"
    elif op == 'mul':
        ...
        aftermul_num=num*data[add_mul_num]
        print(f'{data[add_mul_num]} * {num} = {aftermul_num}')
        data[add_mul_num]=aftermul_num
        # same as add
    elif op =='mulall':
        aftermulall=1
        for key in data:
            aftermulall*=data[key]
        print(aftermulall) 
    elif op == 'end':
        break
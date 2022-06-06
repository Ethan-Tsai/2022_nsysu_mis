names = ['dragon', 'meng', 'Hsuan Ju', 'yihuang']
scores = [100, 90, 59, 10]

name=input("Please input your name:  ")
sc=input("Please input your score:  ")
score=int(sc)
scores.append(score)
scores.sort(reverse=True)
rank=scores.index(score)
names.insert(rank,name)
print(f'You are rank #{rank+1} right now')

for i in range(0,len(scores)):
    a=zip(names,scores)
    print(f'{list(a)[i][0]:>10s}',end=' ')
    a=zip(names,scores)
    print(list(a)[i][1])

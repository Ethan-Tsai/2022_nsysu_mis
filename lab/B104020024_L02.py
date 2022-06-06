from os import scandir

key = 1
while(key == 1):
    sc = input("Please input your score: ")
    score = int(sc)

    word = "Congratulations! you pass this class."

    if score <= 100 and score >= 0:
        if score >= 90:
            gra = "A+"
        elif score >= 85:
            gra = "A"
        elif score >= 80:
            gra = "A-"
        elif score >= 77:
            gra = "B+"
        elif score >= 73:
            gra = "B"
        elif score >= 70:
            gra = "B-"
        elif score >= 67:
            gra = "C+"
        elif score >= 63:
            gra = "C"
        elif score >= 60:
            gra = "C-"
        elif score >= 50:
            gra = "D"
            word="Sorry, you fail this class."
        elif score >= 40:
            gra = "E"
            word="Sorry, you fail this class."   
        else:
            gra = "F"
            word="Sorry, you fail this class."
        print(f'Your grade is {gra}' )
        print('%s'%word)
    else:
        word="Your score out of range!"
        print('{:20s}'.format(word))
        key=0


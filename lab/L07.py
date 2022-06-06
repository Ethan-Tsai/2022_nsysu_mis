class Myteam:
    player_Number=0
    team_Grade=0
    
    def __init__(self):
        self.player = []
        
    def add_player(self, player_name,player_Gra):
        self.player.append(player_name)
        self.player_Number += 1
        self.team_Grade+=player_Gra
    
    def display(self):
        print(f'{self.player}  戰力:{self.team_Grade}')
        
    def __add__(self, other):
        self.player_Number += other.player_Number
        self.player += other.player
        self.team_Grade+=other.team_Grade
        return self
        
        
first=Myteam()
print("第一隊")
first.display()
first.add_player("apple",15) #新增
first.add_player("banana",30)
first.display()

second=Myteam()
print("第二隊")
second.display()
second.add_player("cat",8) #新增
second.add_player("dog",45)
second.display()

third=first+second #合
print("第三隊")
third.display()
class Animal:
    def __init__(self,name,food):
        self.name = name
        self.food = food
        
    def talk(self):
        print(f"{self.name}")    
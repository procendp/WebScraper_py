class Dog:
    def __init__(self, name, breed, age):   # self : 파이썬에서는 기본적으로 이 자리에 매개변수가 꼭 1가지 이상 있어야 함. # self가 해당하는 class 그 자체를 참조함
        self.name = name
        self.breed = breed
        self.age = age

class GuardDog(Dog):    # Dog -> 상속받음
    def __init__(self, name, breed):
        super().__init__(name, breed, 3,)
        self.aggressive = True  # 공통적이지 않은 부분

    def rrrrr(self):
        print("STAY AWAY!")

# class Puppy:
class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 1,)  #super -> 부모 class Dog 참조
        self.spoiled = True

    def woofWoof(self):
        print("WOOF! WOOF!")
        
    # def __str__(self):
    #     return f"{self.breed} puppy named {self.name} and {self.age}yrs old"

Jam = Puppy(
    name = "Jam",
    breed = "chihuahua")
Moo = GuardDog(
    name = "Moo", 
    breed = "shepherd")

Jam.woofWoof()
Moo.rrrrr()


# Jam = {
#     "name" : "Jam",
#     "XP" : 1000,
#     "team" : "Team X",
# }

# def createPlayer(name, xp, team):
#     return {
#         "name" : name,
#         "xp" : xp,
#         "team" : team,
#     }

# def introducePlayer(player):
#     name = player["name"]
#     team = player["team"]
#     print(f"Hello! My name is {name} and i play for {team}")

# # introducePlayer(Jam)

# Jam = createPlayer("Jam", 1500, "Team X")
    
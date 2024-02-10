class Human:
    def __init__(self,num_leg) -> None:
        self.eyes = 2
        self.ears = 2
        self.num_leg =num_leg
    def eat(self):
        print("i can eat")
    def work(self):
        print("i can work")
class Male(Human):
    def __init__(self,name,num_leg):
        super().__init__(num_leg) # give access to attribute in super class
        def flirt(self):
                print("i can flirt")
male = Male("George",5)
print(male.eyes)
print(male.ears)
print(male.num_leg)
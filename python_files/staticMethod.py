from datetime import datetime
class person:
    def __init__(self,name, age) -> None:
        self.name = name
        self.age = age

    def description(self):
        print("my name is {} am {} old".format(self.name,self.age))

    @classmethod #used as an instance it allocates new values to the init method
    def yearOfBirth(cls,name,byear):
        cyear = datetime.now().year
        age = cyear -byear
        return cls(name,age)
george = person.yearOfBirth("george",2002)
george.description()

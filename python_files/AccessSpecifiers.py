'''
types of access apecifiers include:
private can only be used within one class only
 public can be used outside the class
   and protected attributes can be used within the class and subclasses only 

'''
class Student:
    def __init__(self,name,rollno,age) -> None:
        self.name = name #public
        self._rollno = rollno # protected
        self.__age = age #private
    def __display(self): #private method
        print("My name is {} of admission {} {} years old" .format(self.name,self._rollno,self.__age))# use protected att inside the class
    def displayPrivateData(self):
        self.__display()
#outside the class
class Dept(Student):
    pass
b1 = Dept("Mike",5714,21)
#print(b1.name)
b1.displayPrivateData()
#print(b1.__age) cannot access private data from outside the class
#print(b1._rollno) #do not use protected attributes outside the class
print(b1._Student__age)#Access private outside
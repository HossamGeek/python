class Mammal:
    def __init__(self,name):
        self.name = name
    
    def walk(self):
        print("i'm walking")
    
    def eat(self):
        print("i'm walking")
        
class Human:
    def __init__(self,name,weight,height):
        self.name = name
        self.weight = weight
        self.height = height
        
    def speak(self):
        print("im taking now my name's "+self.name)
        
    
    def walk(self):
        print("walk avereg 120 min in day")
    
    
    
class Employee(Human,Mammal):
    
    def __init__(self,name,salary,weight,height):
        super().__init__(name,weight,height)
        self.salary = salary
        
    def work(self,hours):
        self.hours = hours
        print("he's work average "+ str(self.hours) +" salary will be"+str(int((self.hours/24)*5)+self.salary))
    
        



    # super class read left to right
    #if  class (Human) in first must declare:  
        #__init__(self,name,weight,height)
        #super().__init__(name,weight,height)
        #will implement Human->walk 
        
        #obj = Eployee(name,weight,height)

    #elif choose class (Mammal) in first must declare:
        #__init__(self,name) //only
        #super().__init__(name,)
        #will implement Mammal->walk

        #obj = Eployee(name)

    

    
#Ex:
emp1 = Employee("Hossam",1500,57,200)
emp1.walk()
emp1.speak()
emp1.work((7*30))

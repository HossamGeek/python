
#1-
    #Method Resolution Order (MRO)
    #MROsuperclasses read from left to right
    #if method the same other it called from class in the left
#2-
    #if child(second)->second(first):
        #print>>first
#3-
    #if child(third,second)->second(first)->third():
        #print>>first
        #because >> super()        




class First():
    def __init__(self):
        print("First")
    
class Second():
    def __int__(self):
        #super().__init__()
        print("second")
    #def func(self):
        #print("secound")    
class Third():
    def __int__(self):
        print("Third")
    #def func(self):
        #print("third")
class Child(Third,Second):
    def __int__(self):
        super().__init__()
        #print("this is")
    


Child().func()   



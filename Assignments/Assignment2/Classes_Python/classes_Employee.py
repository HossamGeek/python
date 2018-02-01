class Person:
    
    
    def __init__(self,name):
        self.name = name
        self.__mood = ("happy","tired","Lazy")
        self.__healthRate = None
        self.__money      = 0
    
    
    def get_health(self,rate):
        if (rate < 0 ):
            return "0%"
        if ( rate > 100):
            return "100%"
        else:
             self.__healthRate = str(rate) + "%" 
             return self.__healthRate

    
    
    def get_mood(self,num):
        return self.__mood[num]
    
    def get_money(self,count):
        self.__money = count
        return self.__money
    
    def sleep(cls,hours):
        if (hours == 7):
            print(cls.get_mood(0))
        elif (hours < 7):
            print(cls.get_mood(1))
        elif (hours > 7) :   
            print(cls.get_mood(2)) 
            
    def eat(self,meals):
        if (meals == 3):
            print(self.get_health(100))
                  
        if (meals == 2) :
            print(self.get_health(75))
                  
        if (meals == 1) :   
            print(self.get_health(50)) 
        
    
    def buy(cls,items):
        if( cls.__money <= 0 ):
            return 0
        else:    
            cls.__money -= (items)*10
            return cls.__money


        

class Car:
    def __init__(self,name):
        self.name = name
        self.__feulRate = 0
        self.__velocity = 0
    

    def get_feulRate(self,rate):
        if (rate < 0 ):
            return 0
        if ( rate > 100):
            return 100
        else:
             self.__feulRate = rate 
             return self.__feulRate

    def get_velocity(self,rate):
        if (rate < 0 ):
            return 0
        if ( rate > 200):
            return 200
        else:
             self.__velocity = rate 
             return self.__velocity

    
    def run(self,velocity, distance):
        
       
        d = distance / 1000
        
        for i in range(int(d+1)):
            if(i%10 == 0):
                if(self.__feulRate <= 0):
                    self.get_feulRate = 0
                else:    
                    self.__feulRate -= (10/100)
                    self.__velocity += 10
        
        if(self.__feulRate == 0):
            print (str(int(d))+"KM")
            return self.stop()
            
    def stop(self):
           self.__velocity = 0
            

        
        
class Employee(Person):
    email         = None
    
    def __init__(self,name,Id):
        Person.__init__(self,name)
        self.Id      = Id
        self.__salary  = 0
        self.__car           = None
        self.__distanceToWork= 0
      
    
    def get_salary(self,salary):
        if ( salary < 1000):
            return 1000
        else:
             self.__salary = salary 
             return self.__salary
        
    def work(cls,hours):
        if (hours == 8):
            print(cls.get_mood(0))
        elif (hours < 8):
            print(cls.get_mood(1))
        elif (hours > 8) :   
            print(cls.get_mood(2)) 
         
    def get_time(self,time):
        self.__time = time
        return self.__time
    
    def get_distance(self,distance):
            self.__distanceToWork = distance * 1000
            return self.__distanceToWork
    def get_nameCar(self,_name):
            self.__car = _name
            return self.__car

        
    def refuel(self,gasAmount=100):
        F = Car(self.__car)
        return F.get_feulRate(gasAmount)
               
    def drive(self,distance,time):
        d = self.get_distance(distance)
        t = self.get_time(time)
        v =  d / t 
        F = Car(self.__car)
        print(str(round(v))+"Km/hr  "+str(int(d/1000))+"Km")
        return F.run(round(v),d)

    def send_mail():
        return

class Office:
    def __init__(self,name,employees):
        self.name = name
        self.employees =employees
        
    def get_all_employees():
        return
    
    def get_employee():
        return
    
    def hire():
        return
    
    def fire(): 
        return
    
    def calculate_lateness():
        return
    
    def deduct():
        return
    
    def reward():  
        return
    

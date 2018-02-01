#python Not have overloading  

class A:
        def func(self):    
                print ('first method')
        def func(self, i):
                print ('second method',i)



a = A()

>>a.func()

typeError: func() missing 1 required positional argument: 'i'

>>a.func(7)

second method 7


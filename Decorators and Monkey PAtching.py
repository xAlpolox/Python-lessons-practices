""" from ast import arg
import time
from functools import wraps

def executionTimer(func):
    @wraps(func)
    def timeWrapper(*args, **kwargs):
        beginTime= time.time()
        result= func (*args, **kwargs)
        completeTime= time.time()
        totalTime= completeTime - beginTime
        print('The ', func.__name__, 'method was completed in ', totalTime)
        return result
    return timeWrapper

@executionTimer
def exampleMethod(n:int):
    while n != 10000:
        n+=1
print(exampleMethod(2)) """

#Monkey Patching:
import types

class MyMathClass ():
    def add (self, x, y):
        return x + y
    def monkey_patch(self):
        old_add= self.add
        def more_powerfull_add (self, x, y):
            return old_add(x, y) + 1
        self.add = types.MethodType(more_powerfull_add, self)

my_math= MyMathClass()
my_math.add( 3, 3)

my_math.monkey_patch()
my_math.monkey_patch()
my_math.monkey_patch()

print(my_math.add(3, 3))


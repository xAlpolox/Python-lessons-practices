def test_method(): print('Just a test')
class Example_MetaClass(type):
    @classmethod
    def __prepare__(cls, name, baseClasses):
        print('In __prepare__')
        return{'Test method:': test_method}
    def __new__(cls, name, baseClasses, theDictionary):
        print('In __new__')
        return type.__new__(cls, name, baseClasses, theDictionary)

class ExampleClass (metaclass=Example_MetaClass):
    def __init__(self):
        print('In:__init')
        pass
    exampleObject = 'Just a test Object'

example= ExampleClass()
print(example.exampleObject)

spam= 'Test Spam'
def local():
    spam= 'Local Spam'
def global_spam():
    global spam
    spam= 'Global spam'
global_spam()
print(spam)









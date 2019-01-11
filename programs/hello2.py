import random

'Scripting'
print(random.randint(0,9))

'functional'

def random_number():
    print(random.randint(0,9))

random_number()
'object oriented'
class Test:
    def random_number(self):
        print(random.randint(0,9))

t = Test()
t.random_number()


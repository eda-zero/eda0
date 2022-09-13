'''
The way you describe it is absolutely not possible. Assignment to a name is a fundamental feature of Python and no hooks have been provided to change its behavior.

However, assignment to a member in a class instance can be controlled as you want, by overriding .__setattr__().

class MyClass(object):
    def __init__(self, x):
        self.x = x
        self._locked = True
    def __setattr__(self, name, value):
        if self.__dict__.get("_locked", False) and name == "x":
            raise AttributeError("MyClass does not allow assignment to .x member")
        self.__dict__[name] = value

>>> m = MyClass(3)
>>> m.x
3
>>> m.x = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 7, in __setattr__
AttributeError: MyClass does not allow assignment to .x member
'''
# Python 的 obj.x = y 可以被 override ，用 __setattr__ 
class Chip:
    def __init__(self):
        pass
    def __setattr__(self, name, value):
        self.__dict__[name] = value

g = Chip("And")
g.a = 0
g.b = 1
g.o = g.a&g.b
g.toHDL()
'''
module And()
'''

print(g.__dict__)



'''
    def inputs(self, params):
        self.inputs = params
        return self
    def outputs(self, params):
        self.outputs = params
        return self
    def regs(self, params):
        self.regs = params
        return self
    def wires(self, params):
        self.wires = params
        return self
    def assign(var, exp):
        pass # ...? self.stmts.append({})
    def always(exp):
        pass
'''
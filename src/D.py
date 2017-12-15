
class ConstMeta(type):
    class ConstError(TypeError): pass        
    def __init__(self, name, bases, dict):
#        print('__init__', name, bases, dict, self, type(self))
        super(ConstMeta, self).__init__(name, bases, dict)
#        self.Min = getattr(cls, "__PARAMS__", [])
        import sys
        sys.modules[name]=self()#ConstMetaを継承したクラスのモジュールに、そのクラスのインスタンスを代入する        
    def __setattr__(self, name, value):
        if name in self.__dict__.keys(): raise self.ConstError('readonly。再代入禁止です。')
        super(ConstMeta, self).__setattr__(name, value)
#    def __set_name__(self, owner, name):
#        print(f'Descr.__set_name__({owner}, {name})')

class Spam(metaclass=ConstMeta):
#class Spam:
#    __metaclass__ = ConstMeta
    def __init_subclass__(cls, **kwargs):
        print('----------')
        super().__init_subclass__()
        print('Spam:', cls, kwargs)
        for k,v in kwargs.items(): setattr(cls, k, v)

class Ham(Spam):
    bacon=1
#    __metaclass__ = ConstMeta
#    def __init_subclass__(cls, **kwargs):
#        super().__init_subclass__(**kwargs)
#        print('Ham:', cls, kwargs)

class Egg(Ham):
    cheese=1
#    __metaclass__ = ConstMeta
#    def __init_subclass__(cls, **kwargs):
#        super().__init_subclass__(**kwargs)
#        print('Egg:', cls, kwargs)

"""
print(Ham.bacon)
Ham.bacon = 100
print(Ham.bacon)
#h = Ham()
#print(h.bacon)
"""

class_datas = (
{'name':'Ham', 'members': {'bacon':1}},
{'name':'Egg', 'members': {'bacon':2}}
)
OctaveTypes = []
for cd in class_datas:
#    Type = type(cd['name'], (object,), cd['members'])#NameError: name '__setattr__' is not defined
    Type = type(cd['name'], (Spam,), cd['members'])#NameError: name '__setattr__' is not defined
#    Type = type(cd['name'], (object,Spam), cd['members'])#TypeError: Cannot create a consistent method resolution order (MRO) for bases object, Spam
    OctaveTypes.append(Type)

print(OctaveTypes)
for t in OctaveTypes:
    print(t.bacon)
    t.bacon = 100#__main__.ConstError: readonly。再代入禁止です。
    print(t.bacon)

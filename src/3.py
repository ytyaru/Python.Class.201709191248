
class ConstMeta(type):
    class ConstError(TypeError): pass        
    def __init__(self, name, bases, dict):
#        print('__init__', name, bases, dict, self, type(self))
        super(ConstMeta, self).__init__(name, bases, dict)
        import sys
        sys.modules[name]=self()#ConstMetaを継承したクラスのモジュールに、そのクラスのインスタンスを代入する        
    def __setattr__(self, name, value):
        if name in self.__dict__.keys(): raise self.ConstError('readonly。再代入禁止です。')
        super(ConstMeta, self).__setattr__(name, value)


class Spam(type):
#class Spam:
    def __init_subclass__(cls, **kwargs):
         super().__init_subclass__()
         print('Spam:', cls, kwargs)
    class ConstError(TypeError): pass        
    def __init__(self, name, bases, dict):
        super(ConstMeta, self).__init__(name, bases, dict)
        import sys
        sys.modules[name]=self()#ConstMetaを継承したクラスのモジュールに、そのクラスのインスタンスを代入する        
    def __setattr__(self, name, value):
        if name in self.__dict__.keys(): raise self.ConstError('readonly。再代入禁止です。')
        super(ConstMeta, self).__setattr__(name, value)

class Ham(Spam, bacon=1):
    def __init_subclass__(cls, **kwargs):
         super().__init_subclass__(**kwargs)
         print('Ham:', cls, kwargs)

class Egg(Ham, cheese=1):
    def __init_subclass__(cls, **kwargs):
         super().__init_subclass__(**kwargs)
         print('Egg:', cls, kwargs)

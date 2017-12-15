class ConstMeta(type):
    class ConstError(TypeError): pass        
    def __init__(self, name, bases, dict):
        print('__init__', name, bases, dict, self, type(self))
        super(ConstMeta, self).__init__(name, bases, dict)
        import sys
        sys.modules[name]=self()#ConstMetaを継承したクラスのモジュールに、そのクラスのインスタンスを代入する        
    def __setattr__(self, name, value):
        if name in self.__dict__.keys(): raise self.ConstError('readonly。再代入禁止です。')
        super(ConstMeta, self).__setattr__(name, value)

class OctaveClass(ConstMeta):
#class OctaveClass(ConstMeta, metaclass=ConstMeta):
#class OctaveClass(type):
#    def __init__(self): pass
    class ConstError(TypeError): pass        
    def __init__(self, name, bases, dict):
        print('__init__', name, bases, dict, self, type(self))
        super(ConstMeta, self).__init__(name, bases, dict)
        import sys
        sys.modules[name]=self()#ConstMetaを継承したクラスのモジュールに、そのクラスのインスタンスを代入する        
    def __setattr__(self, name, value):
        if name in self.__dict__.keys(): raise self.ConstError('readonly。再代入禁止です。')
        super(ConstMeta, self).__setattr__(name, value)

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        print('__init_subclass__', cls, kwargs)
#        cls.Min = kwargs['Min']
#        cls.Names = kwargs['Names']
#        cls.Descriptions = kwargs['Descriptions']
        for k,v in kwargs.items():
            setattr(cls, k, v)
        """
#        cls.Min = Min
#        cls.Names = Names
#        cls.Descriptions = Descriptions
        cls.Min = kwargs['Min']
        cls.Names = kwargs['Names']
        cls.Descriptions = kwargs['Descriptions']
        """
#    def __init_subclass__(cls, **kwargs):
#        print('__init_subclass__', cls, kwargs)

    #絶対値octave(国際式,YAMAHA)をOctaveClassに変換する
    # 国際式     :-1〜9
    # YAMAHA式   :-2〜8
    # OctaveClass:0〜10 (16進数表記は使えない。key(A〜G)と被るから)
    @classmethod
    def Get(cls, octave:int) -> int:
        cls.Validate(octave)
        if cls.Min < 0: return octave + abs(cls.Min)
        elif 0 < cls.Min: return octave - abs(cls.Min) # 最低値が0より大きい方式は現在存在しない
        else: return octave
        
    @classmethod
    def Validate(cls, octave:int):
        if not(isinstance(octave, int)): raise TypeError(f'引数octaveはint型にしてください。: type(octave)={type(octave)}')
        if octave < cls.Min or cls.Min+10 < octave: raise ValueError(f"引数octaveは{cls.Min}〜{cls.Min+10}までの整数値にしてください。: octave={octave}")


class SPN(OctaveClass, Min=-1, Names={'ja': '国際式'}, Descriptions={'ja': '88鍵盤の最低音がA0になる。'}):
    def __init_subclass__(cls, **kwargs): super().__init_subclass__(**kwargs)
class YAMAHA(OctaveClass, Min=-2, Names={'ja': 'YAMAHA式'}, Descriptions={'ja': '根拠不明。'}):
    def __init_subclass__(cls, **kwargs): super().__init_subclass__(**kwargs)
class ZERO(OctaveClass, Min=0, Names={'ja': 'ゼロ式'}, Descriptions={'ja': 'OctaveClassと同値。最低周波数のオクターブを0とする。'}):
    def __init_subclass__(cls, **kwargs): super().__init_subclass__(**kwargs)

print(SPN.Min, SPN.Names, SPN.Descriptions)
print(YAMAHA.Min, YAMAHA.Names, YAMAHA.Descriptions)
print(ZERO.Min, ZERO.Names, ZERO.Descriptions)

SPN.Min = 100
print(SPN.Min, SPN.Names, SPN.Descriptions)


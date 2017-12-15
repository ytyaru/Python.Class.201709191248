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

class OctaveClass(metaclass=ConstMeta):
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

class_datas = (
{'name':'SPN', 'members': {'Min':-1, 'Names':{'ja': '国際式'}, 'Descriptions':{'ja': '88鍵盤の最低音がA0になる。'}}},
{'name':'YAMAHA', 'members': {'Min':-2, 'Names':{'ja': 'YAMAHA式'}, 'Descriptions':{'ja': '根拠不明。'}}},
{'name':'ZERO', 'members': {'Min':0, 'Names':{'ja': 'ゼロ式'}, 'Descriptions':{'ja': 'OctaveClassと同値。最低周波数のオクターブを0とする。'}}}
)

OctaveTypes = []
for cd in class_datas:
    Type = type(cd['name'], (OctaveClass,), cd['members'])
    OctaveTypes.append(Type)

print(OctaveTypes)
for t in OctaveTypes:
#    print(isinstance(t, OctaveClass))
    print(issubclass(t, OctaveClass))
    print(t.Min)
    print(t.Names)
    print(t.Descriptions)
OctaveTypes[0].Min = 100


# このソフトウェアについて

Pythonで共通の任意な親クラス、関数、変数名を持った、別名定義クラスをDRYに書きたい。（クラスインスタンスでなくクラスオブジェクト）

実現させるまで試行錯誤しまくったログ。

* 再代入禁止にしたい
    * そのための実装を個別クラスに分けたい: `type.__setattr__`, `metaclass`
* 共通処理を1箇所だけで実装したい: ふつうにclass定義する
* 上記2件を実装しつつ、同一変数名をもった別名の型をつくりたい: `type(name, bases, dict)`

# 実行

```sh
$ cd ./src/
$ python E.py
```

# 参考

感謝。

## Python

### 定数

* http://fakatatuku.hatenablog.com/entry/2015/03/26/233024

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)


# TDA for Python 

## 目的
- **Topological Data Analysis(位相的データ解析)** をPythonで動くようにしたかった．
- 音声データに対してTDAしてごにょごにょすることで遊べないかと思った．

とはいえ，実際には裏で`R`を実行しているだけ．


## TDA (Topological Data Analysis)

多次元データの位相的情報から特徴を見つけ出す手法．

詳しくはReferences参照．

# 必要なこと
- R のインストール
- R のライブラリ`TDA`のインストール
- `Matplotlib`，`Numpy`やらなにやらPythonのモジュール

# できること

- PyrhonからTDAを実行する．
- 音源データに関してフーリエ変換した後に時間遅れ座標系に写すこと．

## 時間遅れ座標系

カオス解析を用いて時系列データを相空間に写像することで、分析対象となる系への理解を行いやすい形に埋め込みを行う。

1次元の時系列信号から再構成状態空間への埋め込みを行い、アトラクタの再構成を行う。

# Reference
- [TDA sample](http://tekenuko.hatenablog.com/entry/2017/11/01/004248) R上でのTDAの使い方が書いてある
- [Delay Coordinate Embedding](https://personal.egr.uri.edu/chelidz/documents/mce567_Chapter_7.pdf)
- [位相的データ解析入門（スライド）](https://www.slideshare.net/YutakaKuroki/lytics-112543204)

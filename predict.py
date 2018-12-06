### 部屋の広さと家賃の関係を単回帰分析で表してみよう（y=ax)
# まずは具体例でパラメータ a を算出

# Numpyライブラリをインポート
import numpy as np

# ベクトルの定義（np.arrayを使う！）
x = np.array([1, 2, 3])
y = np.array([2, 3.9, 6.1])
# 平均の出し方
x.mean()
y.mean()
# 中心化
xc = x - x.mean()
yc = y - y.mean()
# 要素ごとの掛け算（要素積）
xx = xc * xc
xy = xc * yc
# リスト内を全部足す
xx.sum()
xy.sum()
a = xy.sum() / xx.sum()
# 出力
print(a)


### PandasとMatpltlibの学習 ###

# Pandasライブラリの読み込み
import pandas as pd
# CSVの読み込み
# df:data frame
df = pd.read_csv("sample.csv")
# 一部分だけ表示する（.head使う！）
print(df.head(3))

# データの抽出
x = df["x"]
y = df["y"]

# Matplotlibの読み込み
import matplotlib.pyplot as plt
# 横軸x, 縦軸yを散布図（scatter）でプロット
plt.scatter(x, y)
plt.show()

# 中心化
df_c = df - df.mean()
# データの抽出
x = df_c["x"]
y = df_c["y"]

plt.scatter(x, y)
plt.show()

### パラメータ a の計算 ###
xx = x * x
xy = x * y
a = xy.sum() / xx.sum()

plt.scatter(x, y, label="y") #実測値
plt.plot(x, a*x, label="y_hat", color="red")#予測値
plt.legend() #凡例の表示
plt.show()

### 予測値の計算（部屋の広さが40平米だったら？） ###

x_new = 40 #40平米の部屋
mean = df.mean()
mean["x"]
#中心化
xc = x_new - mean["x"]
#単回帰分析による予測
yc = a*xc
# 予測値の計算
y_hat = yc + mean["y"]

### せっかくなんで関数にしてみた ###

def predict(x):
    #定数項（今回はわかりやすさをとって算出した数値をそのまま代入しています）
    a = 10069.022519284063
    xm = 37.62222
    ym = 121065.0
    #中心化
    xc = x -xm
    #予測値の計算
    y_hat = a*xc + ym
    #出力
    return y_hat

result = predict(50)
print("家賃の相場は"+ str(result)+ "円です")
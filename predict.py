# 部屋の広さと家賃の関係を単回帰分析で表してみよう（y=ax)
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

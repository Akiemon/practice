# 具体的な値を設定してみる
text = "000000111111111111"
text[0]

# 数字を数えてまとめる関数
def get_count(text):
# 先頭を変数に代入
    _head = text[0]
    head = _head
    
    counts = []
    count = 0

    for ch in text:
        # 同じならカウントに１を足していく
        if ch == head:
            count += 1
        # 異なっていたら空のリストに追加していく
        else:
            counts.append(count)
            count = 1
            head = ch

    else:
        counts.append(count)
        
        
    return _head, counts

# 先頭の値と、カウントしたリストをそれぞれ代入
head, counts = get_count(text)

# 数列を文字列に変換する関数
def int2str(count):   
    if count < 10:
        return "0"+str(count)

    else:
        return str(count)

# エンコードする関数
def encode(text):
    head, counts = get_count(text)
    
    
    text_encode = head
    for count in counts:
        text_encode += int2str(count)
        
    return text_encode

text_encode = encode(text)
print(text_encode)

# ファイルの読み込み
with open("input.txt", "r") as f:
    text = f.read()

text_encode = encode(text)

print(len(text_encode))

print(len(text))

# 圧縮率の計算、出力
print(len(text_encode)/len(text))

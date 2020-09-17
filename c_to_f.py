c = input('請輸入攝氏溫度: ')
c = float(c)
f = c * 9 / 5 + 32
print('華氏溫度為: ', f)

f = input('請輸入華氏溫度: ')
f = float(f)
c = (f - 32) * 5 / 9
print('攝氏溫度為: ' ,c)
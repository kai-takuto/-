print('-じゃんけんゲームが始まるぞ！！-\n')
print('入力した数だけじゃんけんできるぞ！！')
print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n')
while True:
    try:
        n:int = int(input('じゃんけんしたい回数(自然数)を入力してね--->'))
        if n > 0:
            break
        else:
            raise ValueError
    except ValueError:
        pass
    print('＊＊エラー：入力した値は自然数ではありません＊＊')
    print('自然数(1, 2, 3...)を入力してください↓↓↓↓↓↓')
    
# for i in range(n):
    
    
        
print('-じゃんけんゲームが始まるぞ！！-\n')
print('入力した数だけじゃんけんできるぞ！！')
print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n')
while True:
    try:
        n:int = int(input('じゃんけんしたい回数を入力してね--->'))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        pass
    print('自然数(1, 2, 3...)を入力してください↓↓↓↓↓↓')

# for i in range(n):
    
    
        
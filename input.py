print('{:-^4}'.format('-じゃんけんゲームが始まるぞ！！-\n'))
print('{:^30}'.format('入力した数だけじゃんけんできるぞ！！\n↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n'))

while True:
    try:
        n = int(input('じゃんけんしたい回数を入力してね\n--->'))
        break
    except ValueError:
        pass
    print('数字を入力してください↓↓↓↓↓↓')

# for i in range(n):



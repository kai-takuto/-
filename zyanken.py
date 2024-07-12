print('-じゃんけんゲームが始まるぞ！！-\n')
print('入力した数だけじゃんけんできるぞ！！')
print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n')
#(グー：１,チョキ：２,パー：３)のどれかを入力させて出し手を比較
def zyanken(your_hands:int, cpu_hands:int, result:int):
    if your_hands == cpu_hands:
        print('同じ手を出した！結果はあいこ！')
        result['draw'] += 1
    elif your_hands == 1 and cpu_hands == 2:
        print('(あなた)はグー、(相手)はチョキを出した！あなたの勝ち！')
        result['win'] += 1
    elif your_hands == 1 and cpu_hands == 3:
        print('(あなた)はグー、(相手)はパーを出した！あなたの負け！')
        result['lose'] += 1
    elif your_hands == 2 and cpu_hands == 1:
        print('(あなた)はチョキ、(相手)はグーを出した！あなたの負け！')
        result['lose'] +=1
    elif your_hands == 2 and cpu_hands == 3:
        print('(あなた)はチョキ、(相手)はパーを出した！あなたの勝ち！')
        result['win'] += 1
    elif your_hands == 3 and cpu_hands == 1:
        print('(あなた)はパー、(相手)はグーを出した！あなたの勝ち！')
        result['win'] += 1
    elif your_hands == 3 and cpu_hands == 2:
        print('(あなた)はパー、(相手)はチョキを出した！あなたの負け！')
        result['lose'] += 1
    else:
        print('＊＊エラー：1~3の数字を入力してください＊＊')
    return result
while True:
    try:
        n:int = int(input('じゃんけんしたい回数(自然数)を入力してね--->'))
        if n > 0:
            break
        else:
            raise ValueError('input value is not valid integer. it must be number that larger than 0')
    except ValueError as e:
        print(e)
        print('＊＊エラー：入力した値は自然数ではありません＊＊')
        print('自然数(1, 2, 3...)を入力してください↓↓↓↓↓↓')

        
result ={'win': 0, 'lose': 0, 'draw': 0}
# for i in range(n):
    
        
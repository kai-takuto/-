import random


def judge(your_hands: int, cpu_hands: int) -> str:
    if your_hands == cpu_hands:
        return 'draw'
    if ((your_hands == 0 and cpu_hands == 1)
            or (your_hands == 1 and cpu_hands == 2)
            or (your_hands == 2 and cpu_hands == 0)):
        return 'win'
    return 'lose'


# じゃんけんの総合結果
def judge_results(results: list) -> None:
    wins: int = results.count('win')
    lose: int = results.count('lose')
    draws: int = results.count('draw')

    print(f"勝利数: {wins}")
    print(f"敗北数: {lose}")
    print(f"引き分け数: {draws}")


# じゃんけん実行
def main() -> None:
    print('-じゃんけんゲームが始まるぞ！！-\n')
    print('入力した数だけじゃんけんできるぞ！！')
    print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n')
    while True:
        try:
            n: int = int(input('じゃんけんしたい回数(自然数)を入力してね--->'))
            if n > 0:
                break
            else:
                raise ValueError('input value is not valid integer. it must be number that larger than 0')
        except ValueError as e:
            print(e)
            print('＊＊エラー：入力した値は自然数ではありません＊＊')
            print('自然数(1, 2, 3...)を入力してください↓↓↓↓↓↓')
    # 対戦結果を表示させる部分・
    results: list[str] = []
    hands: list = ['グー', 'チョキ', 'パー']
    # 出し手を選択、cpuはランダムに出すようにRev後に作成
    result: str = judge(your_hands=2, cpu_hands=1)
    player_choice: int = 2
    cpu_choice: int = 1
    # 選んだ出し手をリストの中に入れる
    player_hands: str = hands[player_choice]
    cpu_hands: str = hands[cpu_choice]
    # 対戦結果を出力
    print(f'あなた>>{player_hands}')
    print(f'相手>>{cpu_hands}')
    print(f'結果>>{result}')

    results.append(result)
    judge_results(results)


if __name__ == "__main__":
    main()

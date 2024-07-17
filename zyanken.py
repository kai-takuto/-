import random


def judge(your_hands: int, cpu_hands: int) -> str:
    if your_hands == cpu_hands:
        return '引き分け'
    if ((your_hands == 0 and cpu_hands == 1)
            or (your_hands == 1 and cpu_hands == 2)
            or (your_hands == 2 and cpu_hands == 0)):
        return '勝ち'
    return '負け'


# じゃんけんの総合結果
def judge_results(results: list) -> None:
    wins: int = results.count('勝ち')
    lose: int = results.count('負け')
    draws: int = results.count('引き分け')

    print(f"勝利数: {wins}")
    print(f"敗北数: {lose}")
    print(f"引き分け数: {draws}")


# じゃんけんをする回数を入力するところ
def fight_num() -> int:
    while True:
        try:
            n: int = int(input('じゃんけんしたい回数(自然数)を入力してね--->'))
            if n > 0:
                return n
            else:
                raise ValueError('input value is not valid integer. it must be number that larger than 0')
        except ValueError as e:
            print(e)
            print('＊＊エラー：入力した値は自然数ではありません＊＊')
            print('自然数(1, 2, 3...)を入力してください↓↓↓↓↓↓')


# じゃんけんの出し手を選択・表示
def choice_hands(round_num: int) -> None:
    results: list[str] = []
    hands: list = ['グー', 'チョキ', 'パー']

    for i in range(round_num):
        while True:
            try:
                player_choice: int = int(input('(グー：0, チョキ：1, パー：2) あなたが出す手は？：'))
                if player_choice in [0, 1, 2]:
                    break
                else:
                    raise ValueError('input value is not valid integer. it must be number 0 and 2')
            except ValueError as e:
                print(e)
                print('＊＊エラー：グー(0)、チョキ(1)、パー(2) のいずれかを入力してください＊＊')

        player_hands: str = hands[player_choice]
        cpu_choice: int = random.randint(0, 2)
        cpu_hands: str = hands[cpu_choice]

        # 出し手を選択、playerは入力、cpuはランダムに出すようにRev後に作成
        result: str = judge(player_choice, cpu_choice)
        # 対戦結果を出力
        print(f'あなた>>{player_hands}')
        print(f'相手>>{cpu_hands}')
        print(f'結果>>{result}')

        # 結果をリストに追加
        results.append(result)
    print('<<<総合結果>>>')
    judge_results(results)


# じゃんけん実行
def main() -> None:
    print('-じゃんけんゲームが始まるぞ！！-\n')
    print('入力した数だけじゃんけんできるぞ！！')
    print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n')
    round_num: int = fight_num()
    choice_hands(round_num)


if __name__ == "__main__":
    main()

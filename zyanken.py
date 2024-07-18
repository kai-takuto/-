import random


def judge(your_hands: int, cpu_hands: int) -> str:
    """
    じゃんけんの勝敗を決める関数
    入力した数字とランダムで出される数字を比較する
    :param your_hands: プレイヤーの出し手
    :param cpu_hands: CPUの出し手
    :return: 勝敗を返す
    """
    if your_hands == cpu_hands:
        return '引き分け'
    if ((your_hands == 0 and cpu_hands == 1)
            or (your_hands == 1 and cpu_hands == 2)
            or (your_hands == 2 and cpu_hands == 0)):
        return '勝ち'
    return '負け'


def judge_results(results: list) -> None:
    """
    関数judgeの結果をカウントして、総合結果を表示させる関数
    :param results: じゃんけんの勝敗の結果
    :return: 総合結果
    """
    wins: int = results.count('勝ち')
    lose: int = results.count('負け')
    draws: int = results.count('引き分け')

    print(f"勝利数: {wins}")
    print(f"敗北数: {lose}")
    print(f"引き分け数: {draws}")


def fight_num() -> int:
    """
    じゃんけんをしたい回数を入力する
    入力した値が0よりも小さい値、int型以外の値が入力された場合、エラーを返す
    :return: 入力したじゃんけんをしたい回数の値
    """

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


def choice_hands(round_num: int) -> None:
    """
    関数fight_numで入力された回数、じゃんけんで対戦することができる
    出し手を0~2で入力させ、それ以外の値が入力された場合、エラーを返す
    cpuは出し手をランダムにさせ、judge関数の中に出し手を代入して対戦させる
    :param round_num: じゃんけんをする回数
    :return: 入力した出し手の値
    """
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

        # 出し手を選択、playerは入力、cpuはランダムに出す
        result: str = judge(player_choice, cpu_choice)
        # 対戦結果を出力
        print(f'あなた>>{player_hands}')
        print(f'相手>>{cpu_hands}')
        print(f'結果>>{result}')

        # 結果をリストに追加
        results.append(result)
    print('<<<総合結果>>>')
    judge_results(results)


def main() -> None:
    """
    じゃんけんを実行する関数
    fight_numを呼び出して、choice_handsに代入することで入力した回数の対戦が可能
    :return: 実行結果
    """
    print('-じゃんけんゲームが始まるぞ！！-\n')
    print('入力した数だけじゃんけんできるぞ！！')
    print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓\n')
    round_num: int = fight_num()
    choice_hands(round_num)


if __name__ == "__main__":
    main()

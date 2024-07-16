import random


# じゃんけんの勝敗
def zyanken(your_hands: int, cpu_hands: int) -> str:
    if your_hands == cpu_hands:
        return 'draw'
    if ((your_hands == 1 and cpu_hands == 2)
            or (your_hands == 2 and cpu_hands == 3)
            or (your_hands == 3 and cpu_hands == 1)):
        return 'win'
    return 'lose'


# じゃんけんの総合結果
def zyanken_results(results: list) -> None:
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
    result: str = zyanken(your_hands=3, cpu_hands=2)
    your_hands: int = 3
    cpu_hands: int = 2

    print(f'あなたは{your_hands}を、相手は{cpu_hands}を出した')
    print(result)

    results.append(result)
    zyanken_results(results)


if __name__ == "__main__":
    main()

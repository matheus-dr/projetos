from models.calculation import Calculation


def main():
    score = 0
    play(score)


def play(score):
    continuation = 1
    while continuation != 0:
        difficulty = int(input("Informe o nível de dificuldade desejado de 1 a 4: "))
        calculation = Calculation(difficulty)
        print("Informe o resultado para a seguinte operação:")
        calculation.show_operation()
        user_answer = float(input())
        if calculation.check_result(user_answer):
            score += 1
        continuation = int(input("Deseja continuar no jogo?\n[0 - Não | 1 - Sim]\n"))
    print(f"Você finalizou com {score} pontos")


if __name__ == "__main__":
    main()

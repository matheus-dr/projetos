from random import randint


class Calculation:
    operators = ['+', '-', '*', '/']

    def __init__(self, difficulty):
        self.__difficulty = difficulty
        self.__value1 = self._generate_value
        self.__value2 = self._generate_value
        self.__operator = randint(0, 3)
        self.__result = self._generate_result

    @property
    def difficulty(self):
        return self.__difficulty

    @property
    def value1(self):
        return self.__value1

    @property
    def value2(self):
        return self.__value2

    @property
    def operator(self):
        return self.__operator

    @property
    def result(self):
        return self.__result

    @property
    def _generate_value(self):
        if self.difficulty == 1:
            return randint(0, 10)
        elif self.difficulty == 2:
            return randint(0, 100)
        elif self.difficulty == 3:
            return randint(0, 1000)
        elif self.difficulty == 4:
            return randint(0, 10000)
        else:
            return randint(-100000, 100000)

    @property
    def _generate_result(self):
        if not self.value2:
            self.__value2 = self._generate_value
        else:
            return eval(str(self.__value1) + self.operators[self.__operator] + str(self.__value2))

    def check_result(self, answer):
        boolean = False
        if self.result == answer:
            print("Resposta correta!")
            boolean = True
        else:
            print("Resposta errada!")
        print(f"{str(self.__value1) + self.operators[self.__operator] + str(self.__value2)} = {self.result}")
        return boolean

    def show_operation(self):
        print(str(self.__value1) + self.operators[self.__operator] + str(self.__value2))

    def __str__(self):
        op = ''
        if self.operator == 0:
            op = "Somar"
        elif self.operator == 1:
            op = "Subtração"
        elif self.operator == 2:
            op = "Multiplicação"
        elif self.operator == 3:
            op = "Divisão"
        else:
            pass
        return f"Valor 1: {self.value1}\nValor 2: {self.value2}\nDificuldade: {self.difficulty}\nOperação: {op}"

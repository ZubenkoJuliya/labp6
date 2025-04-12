class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        total_sum = 0
        for n in range(1, N + 1):
            total_sum += self.transform(n)
        return total_sum


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3


# Пример использования классов:
if __name__ == "__main__":
    N = 5
    summator = Summator()
    square_summator = SquareSummator()
    cube_summator = CubeSummator()

    print("Сумма натуральных чисел от 1 до {}: {}".format(N, summator.sum(N)))
    print("Сумма квадратов чисел от 1 до {}: {}".format(N, square_summator.sum(N)))
    print("Сумма кубов чисел от 1 до {}: {}".format(N, cube_summator.sum(N)))

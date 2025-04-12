class Triangle(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c


class EquilateralTriangle(object):

    def __init__(Triangle, a):
        Triangle.a = a
        Triangle.b = a
        Triangle.c = a

    def perimeter(self):
        return Triangle.perimeter(self)


if __name__ == "__main__":
    Triangle1 = Triangle(3, 7, 6)
    print(Triangle1.perimeter())
    Triangle2 = EquilateralTriangle(9)
    print(Triangle2.perimeter())

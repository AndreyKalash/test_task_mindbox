import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Абстрактный базовый класс для всех фигур.
    Определяет интерфейс для вычисления площади фигуры.
    """

    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    """
    Класс, представляющий круг.

    Атрибуты:
        radius (float): Радиус круга.
    """

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


class Triangle(Shape):
    """
    Класс, представляющий треугольник.

    Атрибуты:
        a (float): Длина первой стороны треугольника.
        b (float): Длина второй стороны треугольника.
        c (float): Длина третьей стороны треугольника.
    """

    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self) -> bool:
        """
        Проверяет, является ли треугольник прямоугольным.

        :return: True, если треугольник прямоугольный, иначе False.
        """
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)

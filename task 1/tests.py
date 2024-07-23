import unittest
from shapes import Circle, Triangle, Shape


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        """Проверяет правильность вычисления площади круга."""
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.53981633974483, places=7)

    def test_triangle_area(self):
        """Проверяет правильность вычисления площади треугольника."""
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0, places=7)

    def test_right_angled_triangle(self):
        """Проверяет, правильно ли определяется прямоугольный треугольник."""
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angled())

    def test_non_right_angled_triangle(self):
        """Проверяет, правильно ли определяется непрямоугольный треугольник."""
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_angled())

    def test_shape_calculator(self):
        """Проверяет вычисление площади для списка фигур."""
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = [shape.area() for shape in shapes]
        self.assertAlmostEqual(areas[0], 12.566370614359172, places=7)
        self.assertAlmostEqual(areas[1], 6.0, places=7)

    def test_square_area(self):
        """Проверяет добавление новой фигуры (квадрата) и расчета его площади."""
        class Square(Shape):
            def __init__(self_s, side: float):
                self_s.side = side

            def area(self_s) -> float:
                return self_s.side ** 2
            
        square = Square(4)
        self.assertAlmostEqual(square.area(), 16.0, places=7)


if __name__ == "__main__":
    unittest.main()

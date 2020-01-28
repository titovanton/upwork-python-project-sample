import random
from fractions import Fraction

from src.points import Point, Line, points


class TestPoints:
    def test_static_data(self, example_input, example_output):
        assert example_output == points(example_input)

    def test_generic_data(self, coordinate):
        input = {Point(coordinate(), coordinate()) for i in range(100)}
        p1, p2 = random.sample(input, 2)

        # center of the segment
        x3 = Fraction(p1.x+p2.x, 2)
        y3 = Fraction(p1.y+p2.y, 2)
        input.add(Point(x3, y3))

        # FIXME: weak place as uses same logic
        if p1.x == p2.x:
            a = 0
        else:
            a = Fraction(p1.y-p2.y, p1.x-p2.x)
        b = p1.y - a*p1.x
        output = points(input)
        subset = {Line(a, b)}
        assert output.issuperset(subset)

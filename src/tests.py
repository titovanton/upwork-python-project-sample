import random
from fractions import Fraction

import pytest

from src.points import Point, Line, points, CoordinateTypeError, PointTypeError


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

    def test_invalid_data(self):
        base_input = {Point(0, 0), Point(1, 1), Point(2, 2)}
        input = base_input.union({Point('10', 10)})
        with pytest.raises(CoordinateTypeError):
            points(input)
        input = base_input.union({Point(object, 10)})
        with pytest.raises(CoordinateTypeError):
            points(input)
        input = base_input.union({(1, 12)})
        with pytest.raises(PointTypeError):
            points(input)

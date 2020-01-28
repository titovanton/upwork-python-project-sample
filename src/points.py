import functools
import numbers
from collections import namedtuple
from fractions import Fraction
from itertools import combinations


Line = namedtuple('Line', ['a', 'b'])
Point = namedtuple('Point', ['x', 'y'])


class StrMixin:
    def __str__(self):
        return self.message


class CoordinateTypeError(StrMixin, TypeError):
    message = 'A coordinate must be either numeric or Fraction'


class PointTypeError(StrMixin, TypeError):
    message = 'A point must be an instance of Point'


def belongs_to_line(p1, p2, p3):
    """Takes 3 points, returns True/False if all of them belong to one line

    Points are an instances of the Point class.
    Read README.md for the explanation.
    """
    if p1.x == p2.x:
        a = 0
    else:
        a = Fraction(p1.y-p2.y, p1.x-p2.x)
    b = p1.y - a*p1.x
    if p3.y == a*p3.x + b:
        return Line(a, b)
    return None


def validate_input(func):
    """
    Validates input to be iterable of Point and every coordinate must be either numeric or Fraction.
    If it's numeric, then the validator converts it to Fraction.
    PS: must not make a side effect on the origin input value!
    """
    def _to_fraction(point):
        if not isinstance(point, Point):
            raise PointTypeError()
        x = point.x
        y = point.y
        if isinstance(x, numbers.Number):
            x = Fraction(x)
        if isinstance(y, numbers.Number):
            y = Fraction(y)
        if not (isinstance(x, Fraction) and isinstance(y, Fraction)):
            raise CoordinateTypeError()
        return Point(x, y)

    @functools.wraps(func)
    def wrapper(input):
        _input = {_to_fraction(point) for point in input}
        return func(_input)

    return wrapper


@validate_input
def points(input):
    """Takes iterable(set of points - for example), returns set of lines

    :param input: iterable[Point(<int|Fraction>, <int|Fraction>)]
    """
    output = set()
    for triple in combinations(input, 3):
        line = belongs_to_line(*triple)
        if line:
            output.add(line)
    return output

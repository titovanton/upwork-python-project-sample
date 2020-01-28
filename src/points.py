from collections import namedtuple
from fractions import Fraction
from itertools import combinations


Line = namedtuple('Line', ['a', 'b'])
Point = namedtuple('Point', ['x', 'y'])


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


def points(input):
    """Takes iterable(set of points - for example), returns set of lines"""
    output = set()
    for triple in combinations(input, 3):
        line = belongs_to_line(*triple)
        if line:
            output.add(line)
    return output

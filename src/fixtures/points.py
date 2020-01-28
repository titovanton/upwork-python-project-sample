from fractions import Fraction

import pytest
from faker import Faker

from src.points import Line, Point


@pytest.fixture()
def example_input():
    return {Point(0, 0), Point(1, 1), Point(3, 5), Point(2, 2)}


@pytest.fixture()
def example_output():
    return {Line(1, 0)}


@pytest.fixture()
def coordinate():
    fake = Faker()

    def _coordinate():
        return Fraction(fake.pyfloat(min_value=-100, max_value=100))

    return _coordinate

import pytest
import src.task4 as t4

@pytest.mark.parametrize("p, d, type, result",
[
    (100, 50, float, 50),
    (19.99, 75, float, 14.99),
    (20, 2.9, float, 0.58),
    (19.99, 2.9, float, 0.58),
    ("Big cash", "Big Deals", int, 0),
    ("Big Cash", 99, int, 0),
    (542190, "Big Deals", int, 0)
])
def test_calculate_discount(p, d, type, result):
    assert t4.calculate_discount(p, d) == result
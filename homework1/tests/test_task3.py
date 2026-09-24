import src.task3 as t3
import pytest

# Testing for sign_of_num
@pytest.mark.parametrize("n, val",
[
    (1, "+"),
    (0, "0"),
    (-1, "-"),
    (2147483647, "+"),
    (-2147483647, "-")
])
def test_sign_of_num(n, val):
    assert t3.sign_of_num(n) == val

def test_first_10_prime(capsys):
    t3.first_10_prime()
    assert "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]" in capsys.readouterr().out

def test_sum_1_to_100():
    assert t3.sum_1_to_100() == 5050
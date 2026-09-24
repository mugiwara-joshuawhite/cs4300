#imports
import src.task2 as t2
import pytest

# Testing for use_int
@pytest.mark.parametrize("a, b, expected_type, expected_value",
[
   (2, 2, str, "fish"),
   (0, 0, int, 0),
   (-1, -6, int, -7),
   (1, 6, int, 7)
])
def test_use_int(a, b, expected_type, expected_value):
    assert isinstance(t2.use_int(a, b), expected_type)
    assert t2.use_int(a, b) == expected_value

# Testing for use_float
@pytest.mark.parametrize("a, b, places, expected_type, expected_value",
[
    (2.0, 2.0, 2, float, 0.00),
    (4.5, 2.0, 2, float, 2.50),
    (3.14, 2.72, 2, float, 0.42)
])
def test_use_float(a, b, places, expected_type, expected_value):
    assert isinstance(t2.use_float(a, b, places), expected_type)
    assert t2.use_float(a, b, places) == expected_value

# Testing for use_string
@pytest.mark.parametrize("astr, bstr, expected_type, expected_value",
[
    ("Fly me to", "the moon", str, "Fly me to the moon"),
    ("And let me play", "among the stars", str, "And let me play among the stars")
])
def test_use_string(astr, bstr, expected_type, expected_value):
    assert isinstance(t2.use_string(astr, bstr), expected_type)
    assert t2.use_string(astr, bstr) == expected_value

# Testing for use_bool
@pytest.mark.parametrize("abool, bbool, expected_type, expected_value",
[
    (True, True, bool, False),
    (True, False, bool, False),
    (False, True, bool, True),
    (False, False, bool, False)
])
def test_use_bool(abool, bbool, expected_type, expected_value):
    assert isinstance(t2.use_bool(abool, bbool), expected_type)
    assert t2.use_bool(abool, bbool) == expected_value
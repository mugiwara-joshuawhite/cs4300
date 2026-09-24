import pytest
import src.task6 as t6

@pytest.mark.parametrize("filepath, result",
[
    ("task6_read_me.txt", 104),
    ("task6_forfun.txt", 9157),
    ("non-existant_file_name.void", 0)
])
def test_count_words_in_file(filepath, result):
    assert t6.count_words_in_file(filepath) == result
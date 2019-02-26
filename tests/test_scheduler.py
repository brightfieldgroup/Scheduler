# some simple tests to show functionality of pytest
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


def test_answer_working():
    assert func(3) != 99
    assert func(3) == 4

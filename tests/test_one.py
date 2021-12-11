from pyinstaller_test2.show_version import add_two_numbers

def test_one_one():
    assert 1 == 1

def test_add_two():
    assert add_two_numbers(1, 2) == 3

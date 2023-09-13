def test_equal():
    assert 1 == 1, "Number is not equal to expected"


def test_is_not_equal():
    assert 1 != 2, "Number is equal"


def test_zero_divisor():
    num1 = 10
    num2 = 0
    assert num2 != 0, "The divisor is zero"
    print("The result is:", num1 / num2)


def test_not_equal_str():
    val = "Pythonist"
    assert val != "Pythonist", "The condition is false"


def test_equal_str():
    val = "hello"
    assert val == "Pythonist", "The variable value is not equal to Pythonist"

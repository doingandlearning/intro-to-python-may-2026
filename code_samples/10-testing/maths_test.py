from maths import add, subtract, multiply, divide
import pytest

def test_does_pytest_find_this_test():
  # Arrange  - Given
  # Act      - When
  # Assert   - Then
  assert True == True

def test_two_whole_numbers_add_together_correctly():
  number1 = 10
  number2 = 20
  expected = 30

  result = add(number1, number2)

  assert result == expected
  assert add(10, 20) == 30

def test_decimals_add_together_correctly():
  assert add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract_whole_numbers_correctly():
  assert subtract(10, 3) == 7

def test_multiply_decimals_correctly():
  assert multiply(0.1, 0.2) == pytest.approx(0.02)

def test_divide_decimals_correctly():
  assert divide(0.3, 0.1) == pytest.approx(3.0)

def test_divide_by_zero_raises():
  with pytest.raises(ZeroDivisionError):
    divide(1, 0)

@pytest.mark.parametrize("a, b, expected", [
  (-100, -100, -200),
  (1_000_000, 1_000_000, 2_000_000),
  (3_000_000, 10, 3_000_010),
  (-100, 100, 0)
])
def test_valid_pairs_create_expected_result(a, b, expected):
  assert add(a, b) == expected

# decimal, large numbers, negatives
# handling NoneType
# make sure it only adds numbers - checking type

def test_it_fails_when_adding_strings():
  with pytest.raises(TypeError):
    add("1", "2")
  # try:
  #   add("1", "2")
  # except TypeError as e:
  #   assert e is not None

@pytest.mark.parametrize("a, b", [
  ([], []),
  (None, None),
  ({}, {}),
  (True, True),
  ([], {}),
  (1, [])
])
def test_various_non_numbers_fail(a, b):
  with pytest.raises(TypeError):
    add(a,b)


@pytest.mark.parametrize("a, b", [
  ("1", "2"),
  (None, 1),
  (True, 2),
  ([], 2),
])
def test_other_operations_reject_non_numbers(a, b):
  with pytest.raises(TypeError):
    subtract(a, b)
  with pytest.raises(TypeError):
    multiply(a, b)
  with pytest.raises(TypeError):
    divide(a, b)
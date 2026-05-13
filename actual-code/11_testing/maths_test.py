from maths import add
import pytest

def test_that_pytest_is_working():
  # Arrange -> creating class, getting our values ready ... setup
  # Act -> call our function, invoke our method, do the thing that we are testing
  # Assert -> what should be true if the test should pass
  assert True == True

# Happy path -> two numbers add together
def test_two_whole_numbers_add_together_correctly():
  num1 = 4
  num2 = 8
  expected = 12

  result = add(num1, num2)
 
  assert expected == result


# Edge cases -> big numbers, negatives, decimals, 
def test_two_large_numbers_give_correct_result():
  assert 2_000_000 == add(1_000_000, 1_000_000)

# parameteris(z)ing our tests
# decorator -> function that gives another function more power/capabilities
@pytest.mark.parametrize("num1, num2, expected", (
  (-200, -100, -300),
  (150, -100, 50),
  (3_000_000, 10, 3_000_010),
  (-1, 0.3, -0.7)
))
def test_pairs_of_numbers_add_together_correctly(num1, num2, expected):
  assert add(num1, num2) == expected


def test_two_decimals_add_together_correctly():
  assert add(0.1, 0.2) == pytest.approx(0.3)

# Error cases -> [] + [], "" + ""
def test_add_fails_when_two_strings_are_added():
  with pytest.raises(TypeError):
    add("", "")

@pytest.mark.parametrize("value1, value2", (
    ("", []),
    ([], []),
    ({}, {}),
    (True, True)
  )
)
def test_add_fails_when_two_invalid_types_are_added(value1, value2):
  with pytest.raises(TypeError):
    add(value1, value2)
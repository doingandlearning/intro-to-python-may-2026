from vehicle import Vehicle
import pytest

def test_vehicle_was_created_properly():
  v = Vehicle("QWEQWE", "Ford", "Transit", 2020, 1500, "Available")
  assert isinstance(v, Vehicle)
  assert v.registration == "QWEQWE"
  assert v.make == "Ford"
  assert v.model == "Transit"

def test_vehicle_is_initially_available():
  v = Vehicle("QWEQWE", "Ford", "Transit", 2020, 1500)
  assert v.is_available() == True

def test_vehicle_is_unavailable_once_it_has_been_assigned():
  # Arrange
  v = Vehicle("QWEQWE", "Ford", "Transit", 2020, 1500)

  #Act
  v.assign_driver(123)

  #Assert
  assert v.is_available() == False

def test_a_max_load_of_more_than_10000_is_rejected():
  with pytest.raises(ValueError):
    v = Vehicle("QWEQWE", "Ford", "Transit", 2020, 15000) 
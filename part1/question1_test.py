import pytest
from question1 import get_city_weather
"""
def test_get_city_weather():

  assert get_city_weather("Quito") == "22 degrees and sunny"

  assert get_city_weather("New York") == "14 degrees and rainy"
"""
@pytest.mark.parametrize(
    "input_x,expected", 
    [
      ("Quito", "22 degrees and sunny"),
      ("New York","14 degrees and rainy" ),
      ("Bogota", "None degrees and empty")
    ]
)
def test_get_city_weather(input_x,expected):
    assert get_city_weather(input_x) == expected

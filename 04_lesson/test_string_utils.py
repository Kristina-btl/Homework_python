from string_utils import StringUtils
import pytest

string_utils = StringUtils()
@pytest.mark.positive 
#1
@pytest.mark.parametrize('input_str, expected', 
                         [("skypro", "Skypro"), 
                          ("Nick", "Nick"), 
                          ("", "None")])



def test_capitalize_positive (input_str, expected):
    assert string_utils.capitalize(input_str) == expected
#2
@pytest.mark.parametrize('input_str, expected', 
                         [("  skypro  ", "skypro"), 
                          ("text", "text"), 
                          (" next", "next")])


def test_trim_positive (input_str, expected):
    assert string_utils.trim(input_str) == expected
#3
@pytest.mark.parametrize('input_str, input_symbol',
                         [("skypro", "s"), 
                          ("skypro", "o"), 
                          ("sky", "k")])


def test_contains_positive (input_str, input_symbol):
    assert string_utils.contains(input_str, input_symbol) == True

#4
@pytest.mark.parametrize('input_str, input_symbol','expected',
                         [("SkyPro", "k", "SyPro"),
                          ("SkyPro", "Pro", "Sky"),
                          ("Hello World", "l", "Heo Word"),
                          ("Test string", " ", "Teststring")])


def test_delete_symbol_positive (input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected


@pytest.mark.negative
#1
@pytest.mark.parametrize("input_str, expected", [
    ("12345", "12345"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected
#2
@pytest.mark.parametrize("input_str, expected", [
    ("   12345   ", "12345   "),
    ("", ""),
    ("   ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected
#3
@pytest.mark.parametrize('input_str, input_symbol', [
    ("skypro", "x"),
    ("sky", "z"),
    ("hello", "a")
])
def test_contains_negative(input_str, input_symbol):
    assert string_utils.contains(input_str, input_symbol) == False

#4
@pytest.mark.parametrize('input_str, input_symbol','expected',
                         [("SkyPro", "x", "SkyPro"),
                          ("SkyPro", "Prox", "SkyPro"),
                          ("", "X",pytest.raises(ValueError))
                           ])


def test_delete_symbol_negative (input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected

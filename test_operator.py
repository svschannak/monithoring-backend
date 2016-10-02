# coding: utf-8
from operator_check import OperatorCheck

def test_equal_to_true():
    element = lambda: None
    element.text = "test"
    comparison_value = "test"

    check = OperatorCheck("equal to", element, comparison_value)
    assert check.check()

def test_equal_to_ascii():
    element = lambda: None
    element.text = "48,90 €"
    comparison_value = "48,90 €"

    check = OperatorCheck("equal to", element, comparison_value)
    assert check.check()

def test_equal_to_false():
    element = lambda: None
    element.text = "test"
    comparison_value = "test123"

    check = OperatorCheck("equal to", element, comparison_value)
    assert not check.check()

def test_larger_than_true():
    element = lambda: None
    element.text = "123.1"
    comparison_value = "123.0"

    check = OperatorCheck("larger than", element, comparison_value)
    assert check.check()

def test_larger_than_false():
    element = lambda: None
    element.text = "123.0"
    comparison_value = "123.1"

    check = OperatorCheck("larger than", element, comparison_value)
    assert not check.check()

def test_less_than_true():
    element = lambda: None
    element.text = "123.0"
    comparison_value = "123.1"

    check = OperatorCheck("less than", element, comparison_value)
    assert check.check()

def test_less_than_false():
    element = lambda: None
    element.text = "123.1"
    comparison_value = "123.0"

    check = OperatorCheck("less than", element, comparison_value)
    assert not check.check()

def test_exists_true():
    element = lambda: None
    element.text = "abcd"

    check = OperatorCheck("exists", element)
    assert check.check()

def test_exists_false():
    element = None

    check = OperatorCheck("exists", element)
    assert not check.check()

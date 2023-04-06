import pytest
from series.series import fibonacci,lucas,sum_series


def test_fibonacci():
    """
    Test the fibonacci function with an input of 7.

    Ensure that the function returns the expected output of 13.
    """
    actual=fibonacci(7)
    expected=13
    assert actual == expected

def test_lucas():
    """
    Test the lucas function with an input of 6.

    Ensure that the function returns the expected output of 18.
    """
    actual=lucas(6)
    expected=18
    assert actual == expected

def test_sum_series_fibonacci():
    """
    Test the sum_series function with an input of 6, using the Fibonacci sequence.

    Ensure that the function returns the expected output of 8.
    """
    actual=sum_series(6,0,1)
    expected=8
    assert actual == expected

def test_sum_series_lucas():
    """
    Test the sum_series function with an input of 6, using the Lucas sequence.

    Ensure that the function returns the expected output of 18.
    """
    actual=sum_series(6,2,1)
    expected=18
    assert actual == expected




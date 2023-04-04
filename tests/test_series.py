import pytest
from series.series import fibonacci,lucas,sum_series


def test_fibonacci():
    actual=fibonacci(7)
    expected=13
    assert actual == expected

def test_lucas():
    actual=lucas(6)
    expected=18
    assert actual == expected

def test_sum_series_fibonacci():
    actual=sum_series(6,0,1)
    expected=8
    assert actual == expected

def test_sum_series_lucas():
    actual=sum_series(6,2,1)
    expected=18
    assert actual == expected




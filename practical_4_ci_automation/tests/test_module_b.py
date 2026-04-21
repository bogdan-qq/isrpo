import pytest

from src.module_b import filter_by_value


def test_filter_by_value_regular_case():
    rows = [{"score": 91.0}, {"score": 77.0}, {"score": 88.0}]

    result = filter_by_value(rows, "score", ">", 80)

    assert len(result) == 2


def test_filter_by_value_boundary_empty_input():
    assert filter_by_value([], "score", ">", 80) == []


def test_filter_by_value_raises_invalid_operator():
    with pytest.raises(ValueError):
        filter_by_value([{"score": 1}], "score", "~=", 0)

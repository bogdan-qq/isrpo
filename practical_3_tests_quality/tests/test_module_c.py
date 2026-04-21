import pytest

from src.module_c import calculate_stats


def test_calculate_stats_regular_case():
    stats = calculate_stats([{"score": 91.0}, {"score": 88.0}, {"score": 95.0}], "score")

    assert stats["min"] == 88.0
    assert stats["max"] == 95.0
    assert stats["avg"] == 91.33


def test_calculate_stats_boundary_single_value():
    stats = calculate_stats([{"score": 80.0}], "score")

    assert stats == {"min": 80.0, "max": 80.0, "avg": 80.0, "count": 1.0}


def test_calculate_stats_raises_when_no_numeric_values():
    with pytest.raises(ValueError):
        calculate_stats([{"score": "N/A"}], "score")

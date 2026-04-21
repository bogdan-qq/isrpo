import pytest

from src.module_a import read_csv


def test_read_csv_regular_case(tmp_path):
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("name,score,city\nAlice,91,Moscow\n", encoding="utf-8")

    rows = read_csv(str(csv_file))

    assert rows == [{"name": "Alice", "score": 91.0, "city": "Moscow"}]


def test_read_csv_boundary_case_empty_value(tmp_path):
    csv_file = tmp_path / "sample.csv"
    csv_file.write_text("name,score,city\nAlice,,Moscow\n", encoding="utf-8")

    rows = read_csv(str(csv_file))

    assert rows[0]["score"] == ""


def test_read_csv_raises_for_missing_file():
    with pytest.raises(FileNotFoundError):
        read_csv("not_found.csv")

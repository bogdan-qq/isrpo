import csv
from pathlib import Path


def read_csv(file_path: str) -> list[dict[str, object]]:
    """Read CSV file and convert numeric values to float when possible."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {file_path}")

    rows: list[dict[str, object]] = []
    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            parsed: dict[str, object] = {}
            for key, value in row.items():
                if value is None:
                    parsed[key] = value
                    continue
                stripped = value.strip()
                if stripped == "":
                    parsed[key] = stripped
                    continue
                try:
                    parsed[key] = float(stripped)
                except ValueError:
                    parsed[key] = stripped
            rows.append(parsed)
    return rows

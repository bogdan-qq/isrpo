def calculate_stats(rows: list[dict[str, object]], field: str) -> dict[str, float]:
    """Calculate min, max, avg and count for numeric values."""
    values: list[float] = []
    for row in rows:
        value = row.get(field)
        try:
            values.append(float(value))
        except (TypeError, ValueError):
            continue

    if not values:
        raise ValueError(f"No numeric values found for field '{field}'")

    return {
        "min": min(values),
        "max": max(values),
        "avg": round(sum(values) / len(values), 2),
        "count": float(len(values)),
    }

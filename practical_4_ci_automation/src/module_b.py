def filter_by_value(
    rows: list[dict[str, object]], field: str, operator: str, threshold: float
) -> list[dict[str, object]]:
    """Filter rows by numeric comparison in selected field."""
    allowed = {">", ">=", "<", "<=", "==", "!="}
    if operator not in allowed:
        raise ValueError(f"Unsupported operator: {operator}")

    result: list[dict[str, object]] = []
    for row in rows:
        value = row.get(field)
        try:
            number = float(value)
        except (TypeError, ValueError):
            continue

        condition = {
            ">": number > threshold,
            ">=": number >= threshold,
            "<": number < threshold,
            "<=": number <= threshold,
            "==": number == threshold,
            "!=": number != threshold,
        }[operator]

        if condition:
            result.append(row)

    return result

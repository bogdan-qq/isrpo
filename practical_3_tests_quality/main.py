from src.module_a import read_csv
from src.module_b import filter_by_value
from src.module_c import calculate_stats


def main() -> None:
    data = read_csv("data/sample.csv")
    filtered = filter_by_value(data, "score", ">", 80)
    stats = calculate_stats(filtered, "score")
    print("Stats for score > 80:", stats)


if __name__ == "__main__":
    main()

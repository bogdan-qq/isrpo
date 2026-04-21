import importlib.util
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent


def _load_module(module_alias: str, file_name: str):
    spec = importlib.util.spec_from_file_location(module_alias, BASE_DIR / file_name)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {file_name}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


modulA = _load_module("variant27_modulA", "27_modulA.py")
modulB = _load_module("variant27_modulB", "27_modulB.py")
modulC = _load_module("variant27_modulC", "27_modulC.py")


def _book_to_line(author: str, title: str, year: int) -> str:
    return f"{author} - {title} ({year})"


def main() -> None:
    catalog = modulA.create_catalog()

    # Demo dataset
    modulA.add_book(catalog, "Джордж Оруэлл", "1984", 1949)
    modulA.add_book(catalog, "Рэй Брэдбери", "451 градус по Фаренгейту", 1953)
    modulA.add_book(catalog, "Джоан Роулинг", "Гарри Поттер и философский камень", 1997)

    print("Каталог книг:")
    for book in modulA.list_books(catalog):
        print(_book_to_line(book.author, book.title, book.year))

    print("\nПоиск по автору 'брэд':")
    for book in modulB.search_by_author(catalog, "брэд"):
        print(_book_to_line(book.author, book.title, book.year))

    print("\nПоиск по названию 'гарри':")
    for book in modulB.search_by_title(catalog, "гарри"):
        print(_book_to_line(book.author, book.title, book.year))

    recommended = modulC.random_recommendation(catalog)
    if recommended is None:
        print("\nРекомендация: каталог пуст")
    else:
        print("\nСлучайная рекомендация:")
        print(_book_to_line(recommended.author, recommended.title, recommended.year))


if __name__ == "__main__":
    main()

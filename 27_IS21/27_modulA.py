from dataclasses import dataclass


@dataclass(frozen=True)
class Book:
    author: str
    title: str
    year: int


def create_catalog() -> list[Book]:
    """Create and return an empty in-memory catalog."""
    return []


def add_book(catalog: list[Book], author: str, title: str, year: int) -> Book:
    """Add a book to the catalog and return created entity."""
    book = Book(author=author.strip(), title=title.strip(), year=year)
    catalog.append(book)
    return book


def list_books(catalog: list[Book]) -> list[Book]:
    """Return a shallow copy to avoid external mutation."""
    return catalog.copy()

                                                                                                                                                                                      
                                                                                                                                                                          

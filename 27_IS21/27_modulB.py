def search_by_author(catalog: list[object], author_query: str) -> list[object]:
    query = author_query.strip().lower()
    if not query:
        return []
    return [book for book in catalog if query in book.author.lower()]


def search_by_title(catalog: list[object], title_query: str) -> list[object]:
    query = title_query.strip().lower()
    if not query:
        return []
    return [book for book in catalog if query in book.title.lower()]

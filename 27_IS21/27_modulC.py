import random
from typing import Optional


def random_recommendation(catalog: list[object]) -> Optional[object]:
    if not catalog:
        return None
    return random.choice(catalog)

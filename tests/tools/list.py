from random import randint
from typing import List


def create_random_list(count: int, min: int, max: int) -> List[int]:
    return [randint(min, max + 1) for _ in range(count)]
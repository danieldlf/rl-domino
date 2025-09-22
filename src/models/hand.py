from pydantic import BaseModel
from typing import List

from .stone import Stone

class Hand(BaseModel):
    stones: List[Stone]

    def get_points(self):
        total = 0
        for stone in self.stones:
            total += stone.value1 + stone.value2

        return total

    def remove_stone(self, stone: Stone):
        if stone in self.stones and isinstance(stone, Stone):
            self.stones.remove(stone)
        else:
            raise ValueError(f"Erro ao tentar remover: {stone} de {self.stones}")

    def __contains__(self, item):
        if isinstance(item, Stone):
            return (item in self.stones)
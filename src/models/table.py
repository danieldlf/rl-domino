from pydantic import BaseModel
from typing import List, Optional

from .stone import Stone
from .dorme import Dorme

class Table(BaseModel):
    dorme: Optional[Dorme]
    played_stones: List[Stone] = []
    left_end: Optional[int] = None
    right_end: Optional[int] = None

    def add_stone(self, stone: Stone, side: str):
        """Adiciona uma pedra na mesa e atualiza as pontas abertas."""

        if not self.played_stones:  # primeira jogada
            self.played_stones.append(stone)
            self.left_end, self.right_end = stone.value1, stone.value2
            return

        if side == "left":
            # Verifica e gira se necessário
            if stone.value2 == self.left_end:
                self.played_stones.insert(0, stone)
                self.left_end = stone.value1
            elif stone.value1 == self.left_end:
                stone.rotate()
                self.played_stones.insert(0, stone)
                self.left_end = stone.value1
            else:
                raise ValueError("Jogada inválida no lado esquerdo")

        elif side == "right":
            if stone.value1 == self.right_end:
                self.played_stones.append(stone)
                self.right_end = stone.value2
            elif stone.value2 == self.right_end:
                stone.rotate()
                self.played_stones.append(stone)
                self.right_end = stone.value2
            else:
                raise ValueError("Jogada inválida no lado direito")

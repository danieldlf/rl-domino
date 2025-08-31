from pydantic import BaseModel
from typing import List, Set

from .player import Player
from .dorme import Dorme
from .table import Table
from .stone import Stone

class Domino(BaseModel):
    players: List[Player]
    dorme: Dorme
    table: Table
    initial_stones: Set[Stone]

    @classmethod
    def init_game(cls):
        ...
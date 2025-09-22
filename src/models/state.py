from pydantic import BaseModel, Field
from typing import List, Optional

from .player import Player
from .table import Table
from .pair import Pair

class DominoState(BaseModel):
    players: List[Player]
    table: Table
    pairs: List[Pair]
    current_player_index: int = 0
    winner: Optional[Player] = None
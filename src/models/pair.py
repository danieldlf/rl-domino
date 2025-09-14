from pydantic import BaseModel

from .player import Player

class Pair(BaseModel):
    player1: Player
    player2: Player
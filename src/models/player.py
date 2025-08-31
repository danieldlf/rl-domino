from pydantic import BaseModel

from .hand import Hand

class Player(BaseModel):
    hand: Hand
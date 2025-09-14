from pydantic import BaseModel

from .hand import Hand
from .stone import Stone

class Player(BaseModel):
    id: int
    hand: Hand

    def remove_stone_from_hand(self, stone: Stone):
        if stone not in self.hand:
            return
        
        self.hand.remove_stone(stone)
import random

from pydantic import BaseModel
from typing import List

from .player import Player
from .dorme import Dorme
from .table import Table
from .stone import Stone
from .hand import Hand

NUM_STONES_PER_PLAYER = 6
NUM_PLAYERS = 4

class Domino(BaseModel):
    players: List[Player]
    table: Table

    @classmethod
    def init_game(cls):
        initial_stones = Domino._create_initial_stones()
        shuffled_stones = random.sample(initial_stones, k=len(initial_stones))

        players = []
        for _ in range(NUM_PLAYERS):
            hand_stones = shuffled_stones[:NUM_STONES_PER_PLAYER]
            shuffled_stones = shuffled_stones[NUM_STONES_PER_PLAYER:]
            player_hand = Hand(stones=hand_stones)
            player = Player(hand=player_hand)
            players.append(player)

        dorme = Dorme(sleeping_stones=shuffled_stones)
        table = Table(dorme=dorme)

        return cls(players=players, table=table)

    @staticmethod
    def _create_initial_stones() -> List[Stone]:
        stone_set = list()
        # +1 Para gerar o número correto de números no range
        for value1 in range(NUM_STONES_PER_PLAYER+1):
            for value2 in range(value1, NUM_STONES_PER_PLAYER+1):
                stone = Stone(value1=value1, value2=value2)
                stone_set.append(stone)

        return stone_set
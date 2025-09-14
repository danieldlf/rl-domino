import random
import networkx as nx # Lib de Grafos

from typing import List, Dict, Optional

from ..models.player import Player
from ..models.dorme import Dorme
from ..models.table import Table
from ..models.stone import Stone
from ..models.hand import Hand
from ..models.pair import Pair
from ..models.state import DominoState

MAX_STONE_VALUE = 6
NUM_STONES_PER_PLAYER = 6
NUM_PLAYERS = 4

class GameController:
    def __init__(self, num_players: int = 4, num_stones_per_player: int = 6):
        self.num_players = num_players
        self.num_stones_per_player = num_stones_per_player
        self.game_state = self._initialize_game_state()

    def _initialize_game_state(self) -> DominoState:
        initial_stones = self._create_stone_set()
        shuffled_stones = random.sample(initial_stones, k=len(initial_stones))

        players = []
        for i in range(self.num_players):
            hand_stones = shuffled_stones[:self.num_stones_per_player]
            shuffled_stones = shuffled_stones[self.num_stones_per_player:]
            
            player = Player(id=i, hand=Hand(stones=hand_stones))
            players.append(player)

        dorme = Dorme(sleeping_stones=shuffled_stones)
        table = Table(dorme=dorme)
        pairs = self._define_pairs(players)

        starting_player_index = self._define_starting_player(players)
        print(starting_player_index)

        return DominoState(
            players=players,
            table=table,
            pairs=pairs,
            current_player_index=starting_player_index
        )

    @staticmethod
    def _create_stone_set() -> List[Stone]:
        stone_set = []
        for value1 in range(MAX_STONE_VALUE + 1):
            for value2 in range(value1, MAX_STONE_VALUE + 1):
                stone_set.append(Stone(value1=value1, value2=value2))
        return stone_set

    @staticmethod
    def _define_pairs(players: List[Player], mapping: Dict[str, List[int]] = {"first_pair": [0, 2], "second_pair": [1, 3]}) -> List[Pair]:
        pairs = []
        for pair_indices in mapping.values():
            p1 = players[pair_indices[0]]
            p2 = players[pair_indices[1]]
            pairs.append(Pair(player1=p1, player2=p2))
        return pairs
    
    @staticmethod
    def _define_starting_player(players: List[Player]) -> int:
        highest_carroca = Stone(value1=0, value2=0)
        starting_index = 0
        for idx, player in enumerate(players):
            for stone in player.hand.stones:          
                if stone.is_carroca() and stone.value1 > highest_carroca.value1:
                    highest_carroca = stone
                    starting_index = idx

        return starting_index

    def get_current_player(self) -> Player:
        return self.game_state.players[self.game_state.current_player_index]
    
    def _build_graph_from_state(self) -> nx.Graph:
        graph = nx.Graph()

        stones_on_table = self.game_state.table.played_stones
        for stone in stones_on_table:
            graph.add_edge(stone.value1, stone.value2)

        return graph
    
    def get_playable_ends(self):
        """Retorna as pontas abertas da mesa."""
        if not self.game_state.table.played_stones:
            return []
        return [self.game_state.table.left_end, self.game_state.table.right_end]
    
    def is_move_valid(self, stone: Stone) -> bool:
        ends = self.get_playable_ends()
        if not ends:  # primeira jogada
            return True
        return stone.value1 in ends or stone.value2 in ends

    def play_turn(self, player: Player, stone: Stone, side: str):
        try:
            self.game_state.table.add_stone(stone, side)
            player.remove_stone_from_hand(stone)
        except ValueError:
            return False  # jogada inválida

        return self._after_play(player)
    
    def _after_play(self, player: Player):
        """Ações comuns após uma jogada."""
        winner = self.check_for_winner()
        if winner:
            return f"Jogador {winner.id} venceu!"

        self.advance_to_next_player()
        return True

    def check_for_winner(self) -> Optional[Player]:
        for player in self.game_state.players:
            if not player.hand.stones:  # Se não tem pedras na mão
                return player
        return None

    def advance_to_next_player(self):
        """Passa o turno para o próximo jogador."""
        current_index = self.game_state.current_player_index
        self.game_state.current_player_index = (current_index + 1) % self.num_players

from src.controllers import GameController  

def run_cli():
    game = GameController()
    while not game.is_game_over():
        player = game.get_current_player()
        print("\nMesa:", game.game_state.table.played_stones)
        print("Pontas:", game.get_playable_ends())
        print("Mão:", player.hand.stones)

        actions = game.get_valid_actions(player)
        for i, (stone, side) in enumerate(actions):
            print(f"{i}: {stone} ({side})")

        choice = int(input("Escolha a jogada: "))
        action = actions[choice]

        game.play_turn(player, *action)

    print("Vencedor:", game.get_winner())

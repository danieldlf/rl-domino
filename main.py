from src.controllers import GameController

def main():
    game = GameController()
    
    print("=== Jogo de Dominó (CLI) ===\n")
    while True:
        player = game.get_current_player()
        print(f"\n--- Vez do Jogador {player.id} ---")
        
        # Mostrar mesa
        print("Mesa:", game.game_state.table.played_stones)
        print("Pontas abertas:", game.get_playable_ends())

        # Mostrar mão
        for idx, stone in enumerate(player.hand.stones):
            print(f"{idx}: {stone}")

        # Input do jogador
        choice = input("Escolha a pedra (índice) ou 'p' para passar: ").strip()
        
        if choice.lower() == "p":
            game.advance_to_next_player()
            continue

        try:
            idx = int(choice)
            stone = player.hand.stones[idx]
        except (ValueError, IndexError):
            print("Entrada inválida, tente novamente.")
            continue

        # Escolher lado
        side = input("Lado (left/right): ").strip().lower()
        if side not in ["left", "right"]:
            print("Lado inválido. Tente de novo.")
            continue

        # Jogar
        result = game.play_turn(player, stone, side)
        if result == False:
            print("Jogada inválida!")
        elif isinstance(result, str):  # vitória
            print(result)
            break

if __name__ == "__main__":
    main()

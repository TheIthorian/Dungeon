from room_loop import ManageSector
from inventory_loop import player_character
from game_manager import GameManager
from entities.sector import SECTOR_TYPES


def main():
    player_character.generate_player_character_name()
    player_character.generate_player_character_stats()
    player_character.print_player_character_stats()

    # game_manager = GameManager(player_character, SECTOR_TYPES)
    # game_manager.loop()
    while player_character.health > 0:
        ManageSector()


if __name__ == "__main__":
    main()

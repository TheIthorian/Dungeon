from room_loop import ManageSector
from inventory_loop import player_character


def main():
    player_character.generate_player_character_name()
    player_character.generate_player_character_stats()
    player_character.print_player_character_stats()

    while player_character.health > 0:
        ManageSector()


if __name__ == "__main__":
    main()

from random import choice

from entities import Sector, PlayerCharacter
from display import char_print
from game_loops import room


class GameManager:
    sector_counter = 0
    previous_sector: Sector
    current_sector: Sector
    player: PlayerCharacter
    sector_types: dict[str, Sector]

    room_loop_manager: room.RoomLoopManager

    # Open closed principle
    def __init__(self, player: PlayerCharacter, sector_types: dict[str, Sector]):
        self.player = player
        self.sector_types = sector_types
        self.room_loop_manager = room.RoomLoopManager(self.player)

    def loop(self):
        new_sector = self.roll_new_sector()
        if not self.current_sector:
            char_print(
                f"\nThe daylight fades away behind you. You have entered the {new_sector.name}."
            )

        while self.player.health > 0:
            self.previous_sector = self.current_sector
            self.current_sector = new_sector
            char_print(self.current_sector.introduction_text)

            self.enter_room()

        # death

    def roll_new_sector(self) -> Sector:
        current_type = self.current_sector.name
        new_type = choice(
            list(filter(lambda x: x != current_type, self.sector_types.keys()))
        )
        return self.sector_types[new_type]

    def enter_room(self):
        self.sector_counter += 1
        char_print(
            f"\nYou enter ROOM {self.sector_counter} of the {self.current_sector.name}."
        )

        self.room_loop_manager.roll_room_encounter()

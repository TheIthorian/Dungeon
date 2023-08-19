from random import randint, choice

from entities import PlayerCharacter, Sector

from game_loops.combat import CombatLoop
from game_loops.rest import RestLoop

from time import sleep

from event_behaviours import (
    PositiveEvents,
    NegativeEvents,
    RoomSpecialEvents,
    ExploreSpecialEvents,
)

from display import char_input, char_print
from inventory_loop import LootLoop, InventoryLoop


class RoomLoopManager:
    player: PlayerCharacter

    def __init__(self, player: PlayerCharacter):
        self.player = player

    def roll_room_encounter(self):
        roll = randint(1, 5)
        if roll < 3:
            self.room_no_event()
        elif roll == 3:
            self.room_positive_event()
        elif roll == 4:
            self.room_negative_event()
        else:
            self.room_combat_encounter()

    def room_combat_encounter(self):
        CombatLoop()
        self.prompt_room_decision()

    def room_positive_event(self):
        if not randint(0, 5):
            RoomSpecialEvents(self.player)
        else:
            PositiveEvents()
        self.prompt_room_decision()

    def room_negative_event(self):
        if not randint(0, 5):
            RoomSpecialEvents(self.player)
        else:
            NegativeEvents()
        self.prompt_room_decision()

    def room_no_event(self):
        char_print("\nThe place is quiet, and you have a moment of respite.")
        self.prompt_room_decision()

    def prompt_room_decision(self):
        time_available = True
        while time_available:
            player_response = char_input(
                f"\nWhat would you like to do? (Open Inventory/Explore/Rest/View Stats/Keep Going): ",
                lower=True,
            )
            if player_response == "open inventory":
                InventoryLoop()
                continue
            elif player_response == "view stats":
                self.player.print_player_character_stats()
                continue
            else:
                if player_response == "explore":
                    possible_events = [
                        LootLoop,
                        CombatLoop,
                        ExploreSpecialEvents,
                        PositiveEvents,
                        NegativeEvents,
                    ]
                    choice(possible_events)()
                    time_available = False
                elif player_response == "rest":
                    RestLoop()
                    time_available = False
                else:
                    time_available = False
        char_print("\nTravelling to new room")
        sleep(1)
        print(".")
        sleep(1)
        print(".")
        sleep(1)
        print(".")

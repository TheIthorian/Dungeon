from database import Sector, PlayerCharacter, player_character, char_print, char_input
from random import randint, choice
from combat_loop import CombatLoop
from event_behaviours import PositiveEvents, NegativeEvents, RoomSpecialEvents, ExploreSpecialEvents, RestSpecialEvents
from inventory_loop import LootLoop, InventoryLoop
from constants import SECTOR_INTRODUCTION_TEXT
from time import sleep

sector_counter = 0

sector = Sector()


class ManageSector:

    def __init__(self):
        self.run_room_loop()
        global sector

    @staticmethod
    def roll_new_sector():
        previous_sector = sector.current_sector
        sector.roll_sector()
        while previous_sector == sector.current_sector:
            sector.roll_sector()
        if not previous_sector:
            char_print(f"\nThe daylight fades away behind you. You have entered the {sector.current_sector}.")
            if sector.current_sector == "caves":
                char_print(SECTOR_INTRODUCTION_TEXT.CAVES)
            elif sector.current_sector == "tombs":
                char_print(SECTOR_INTRODUCTION_TEXT.TOMBS)
            elif sector.current_sector == "dungeons":
                char_print(SECTOR_INTRODUCTION_TEXT.DUNGEONS)
            else:
                char_print(SECTOR_INTRODUCTION_TEXT.SEWERS)
        else:
            char_print(f"\nLeaving the {previous_sector} behind, you enter the {sector.current_sector}.")
            if sector.current_sector == "caves":
                char_print(SECTOR_INTRODUCTION_TEXT.CAVES)
            elif sector.current_sector == "tombs":
                char_print(SECTOR_INTRODUCTION_TEXT.TOMBS)
            elif sector.current_sector == "dungeons":
                char_print(SECTOR_INTRODUCTION_TEXT.DUNGEONS)
            else:
                char_print(SECTOR_INTRODUCTION_TEXT.SEWERS)

    @staticmethod
    def enter_room():
        global sector_counter
        sector_counter += 1
        char_print(f"\nYou enter ROOM {sector_counter} of the {sector.current_sector}.")

    def run_room_loop(self):
        if not sector.current_sector:
            self.roll_new_sector()
        global sector_counter
        if sector_counter > randint(10, 20):
            self.roll_new_sector()
            sector_counter = 0
        self.enter_room()
        RoomLoop()


class RoomLoop:

    def __init__(self):
        self.roll_room_encounter()

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
            RoomSpecialEvents()
        else:
            PositiveEvents()
        self.prompt_room_decision()

    def room_negative_event(self):
        if not randint(0, 5):
            RoomSpecialEvents()
        else:
            NegativeEvents()
        self.prompt_room_decision()

    def room_no_event(self):
        char_print("\nThe place is quiet, and you have a moment of respite.")
        self.prompt_room_decision()

    @staticmethod
    def prompt_room_decision(player: PlayerCharacter = player_character):
        time_available = True
        while time_available:
            player_response = char_input(f"\nWhat would you like to do? (Open Inventory/Explore/Rest/View Stats/Keep Going): ", lower=True)
            if player_response == 'open inventory':
                InventoryLoop()
                continue
            elif player_response == 'view stats':
                player.print_player_character_stats()
                continue
            else:
                if player_response == 'explore':
                    possible_events = [LootLoop, CombatLoop, ExploreSpecialEvents,
                                       PositiveEvents, NegativeEvents]
                    choice(possible_events)()
                    time_available = False
                elif player_response == 'rest':
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
        ManageSector()


class RestLoop:

    def __init__(self):
        self._roll_event()
        self._rest_health_gain()

    @staticmethod
    def _roll_event():
        if not randint(0, 5):
            RestSpecialEvents()

    @staticmethod
    def _rest_health_gain(player: PlayerCharacter = player_character):
        rest_heal_amount = randint(1, 8)
        player.health += rest_heal_amount
        player.cap_health_at_max()
        char_print(f"\nYou gain {rest_heal_amount} health from resting! You now have {player.health} out of a"
                   f" maximum of {player.max_health} health.")

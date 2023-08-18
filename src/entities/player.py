from dataclasses import dataclass
from random import randint

from display import char_input, char_print


@dataclass
class PlayerCharacter:
    name: str = ""
    max_health: int = 0
    health: int = 0
    atk: int = 0
    dmg: int = 0
    dfc: int = 0
    psd: int = 0

    def generate_player_character_name(self):
        self.name = char_input("What is your name?: ", title=True)

    def generate_player_character_stats(self):
        self.health += randint(7, 12)
        self.max_health = self.health
        self.atk += randint(0, 2)
        self.dmg += randint(0, 2)
        self.dfc += randint(0, 2)
        self.psd += randint(0, 2)

    def cap_health_at_max(self):
        if self.health > self.max_health:
            self.health = self.max_health

    def print_player_character_stats(self):
        char_print("\nYour current stats are:")
        char_print(
            f"Health: {self.health}/{self.max_health}"
            f"\nAttack: {self.atk}"
            f"\nDamage: {self.dmg}"
            f"\nDefence: {self.dfc}"
            f"\nPersuasion: {self.psd}"
        )

    def check_is_dead(self):
        if self.health < 1:
            self.run_death_sequence()
            exit()

    @staticmethod
    def run_death_sequence():
        char_print(
            "\nClutching at your chest, your hands come away soaked in blood. Blinking, you stagger backwards and"
            " keel over. Then, the world turns black."
        )
        char_input("\nYour story has ended. Enter anything to exit.")

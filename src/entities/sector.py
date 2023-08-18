from dataclasses import dataclass
from random import choice


SECTOR_WEIGHTS = {
    "caves": (15, 4, 1),
    "tombs": (1, 1, 18),
    "sewers": (9, 3, 8),
    "dungeons": (6, 7, 6),
}


@dataclass
class Sector:
    name: str = ""
    current_weights: tuple = (1, 1, 1)

    def roll_sector(self):
        self.name = choice(
            list(filter(lambda x: x != self.name, SECTOR_WEIGHTS.keys()))
        )
        self.current_weights = SECTOR_WEIGHTS[self.name]

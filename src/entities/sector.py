from dataclasses import dataclass
from random import choice

SECTOR_LIST = ["caves", "tombs", "sewers", "dungeons"]


class SECTOR_WEIGHTS:
    CAVES = (15, 4, 1)
    TOMBS = (1, 1, 18)
    SEWERS = (9, 3, 8)
    DUNGEONS = (6, 7, 6)


@dataclass
class Sector:
    name: str = ""
    current_weights: tuple = (1, 1, 1)

    @staticmethod
    def _get_weights_dict():
        return {
            "caves": SECTOR_WEIGHTS.CAVES,
            "tombs": SECTOR_WEIGHTS.TOMBS,
            "sewers": SECTOR_WEIGHTS.SEWERS,
            "dungeons": SECTOR_WEIGHTS.DUNGEONS,
        }

    def roll_sector(self):
        self.name = choice(list(filter(lambda x: x != self.name, SECTOR_LIST)))
        self.current_weights = self._get_weights_dict()[self.name]

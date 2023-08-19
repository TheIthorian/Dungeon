from dataclasses import dataclass
from random import choice
from constants import SECTOR_INTRODUCTION_TEXT


@dataclass
class Sector:
    name: str = ""
    weights: tuple = (1, 1, 1)
    introduction_text: str = ""


SECTOR_TYPES = {
    "caves": Sector(
        name="caves",
        weights=(15, 4, 1),
        introduction_text=SECTOR_INTRODUCTION_TEXT.CAVES,
    ),
    "tombs": Sector(
        name="tombs",
        weights=(1, 1, 18),
        introduction_text=SECTOR_INTRODUCTION_TEXT.TOMBS,
    ),
    "sewers": Sector(
        name="sewers",
        weights=(9, 3, 8),
        introduction_text=SECTOR_INTRODUCTION_TEXT.SEWERS,
    ),
    "dungeons": Sector(
        name="dungeons",
        weights=(6, 7, 6),
        introduction_text=SECTOR_INTRODUCTION_TEXT.DUNGEONS,
    ),
}


def get_random_sector(exclude: str = "") -> Sector:
    new_name = choice(list(filter(lambda x: x != exclude, SECTOR_TYPES.keys())))
    return Sector(name=new_name, current_weights=SECTOR_TYPES[new_name])

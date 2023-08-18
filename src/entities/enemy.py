from dataclasses import dataclass
from random import choices, choice, randint

from constants import ADJECTIVES
from entities.sector import Sector


class ENEMY_LISTS:
    SIZE_LIST = ["small", "medium", "large"]
    CATEGORY_LIST = ["animal", "humanoid", "undead"]
    RARITY_LIST = ["common", "rare", "boss"]


class ENEMY_NAMES:
    SMALL_ANIMAL = ["rat", "mosquito", "toad", "salamander", "spider"]
    MEDIUM_ANIMAL = ["hound", "panther", "wolf", "raptor"]
    LARGE_ANIMAL = ["bear", "crocodile", "lion", "bear", "scarab", "lizard"]
    SMALL_HUMANOID = ["goblin", "gnome", "halfling", "dwarf", "fairy"]
    MEDIUM_HUMANOID = ["human", "elf", "orc", "drow"]
    LARGE_HUMANOID = ["troll", "ogre", "golem", "minotaur", "giant", "centaur"]
    SMALL_UNDEAD = ["tomb-snake", "corpse-fly", "ghoul", "spirit"]
    MEDIUM_UNDEAD = ["zombie", "wraith", "skeleton", "wight", "draugr"]
    LARGE_UNDEAD = ["bone-giant", "flesh-golem"]


@dataclass
class Enemy:
    category: str = ""
    size: str = ""
    rarity: str = ""
    name: str = ""
    health: int = 0
    atk: int = 0
    dmg: int = 0

    def _assign_enemy_type(self):
        self.category = "".join(
            choices(ENEMY_LISTS.CATEGORY_LIST, weights=Sector.current_weights)
        )
        self.size = "".join(choices(ENEMY_LISTS.SIZE_LIST, weights=(3, 6, 1)))
        self.rarity = "".join(choices(ENEMY_LISTS.RARITY_LIST, weights=(16, 3, 1)))

    @staticmethod
    def _get_name_group_dict():
        return {
            "small animal": ENEMY_NAMES.SMALL_ANIMAL,
            "medium animal": ENEMY_NAMES.MEDIUM_ANIMAL,
            "large animal": ENEMY_NAMES.LARGE_ANIMAL,
            "small humanoid": ENEMY_NAMES.SMALL_HUMANOID,
            "medium humanoid": ENEMY_NAMES.MEDIUM_HUMANOID,
            "large humanoid": ENEMY_NAMES.LARGE_HUMANOID,
            "small undead": ENEMY_NAMES.SMALL_UNDEAD,
            "medium undead": ENEMY_NAMES.MEDIUM_UNDEAD,
            "large undead": ENEMY_NAMES.LARGE_UNDEAD,
        }

    def _assign_name_to_enemy(self):
        name_group = f"{self.size} {self.category}"
        self.name = choice(self._get_name_group_dict()[name_group])

    def _get_rarity_adjectives(self):
        if self.rarity == "rare":
            adjective: str = choice(ADJECTIVES.ENEMY_IS_RARE_ADJECTIVES[self.category])
            self.name = f"{adjective} {self.name}"
        if self.rarity == "boss":
            adjective: str = choice(ADJECTIVES.ENEMY_IS_BOSS_ADJECTIVES[self.category])
            self.name = f"{adjective} {self.name}"

    def get_name(self):
        return self.name

    def _generate_enemy_stats(self):
        stat_multiplier = 1
        if self.size == "medium":
            stat_multiplier = 2
        elif self.size == "large":
            stat_multiplier = 6
        if self.rarity == "rare":
            stat_multiplier += 2
        elif self.rarity == "boss":
            stat_multiplier += 6
        self.health = randint(1, 6) * stat_multiplier
        self.atk = int((randint(1, 6) * stat_multiplier) / 3)
        self.dmg = int((randint(1, 6) * stat_multiplier) / 3)

    def get_can_persuade(self):
        if self.rarity != "boss" and self.category == "humanoid":
            return True

    def generate_enemy(self):
        self._assign_enemy_type()
        self._assign_name_to_enemy()
        self._get_rarity_adjectives()
        self._generate_enemy_stats()

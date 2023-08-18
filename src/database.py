from dataclasses import dataclass
from random import choices, choice, randint
from constants import ENEMY_LISTS, SECTOR_LIST, SECTOR_WEIGHTS, ENEMY_NAMES, \
    ADJECTIVES, ITEM_NAMES, ITEM_TYPES_LIST, WEAPON_INSPECT, ATTIRE_INSPECT, CONSUMABLE_INSPECT
from time import sleep


def char_print(string):
    for character in string[:-1]:
        print(character, end='', flush=True)
        sleep(0.02)
    print(string[-1], flush=True)
    sleep(1)


def char_input(string, title=False, lower=False):
    for character in string:
        print(character, end='', flush=True)
        sleep(0.02)
    sleep(1)

    if title:
        return input().title()
    elif lower:
        return input().lower()
    else:
        return input()


@dataclass
class Sector:
    current_sector: str = ''
    current_weights: tuple = (1, 1, 1)

    @staticmethod
    def _get_weights_dict():
        return {
            "caves": SECTOR_WEIGHTS.CAVES,
            "tombs": SECTOR_WEIGHTS.TOMBS,
            "sewers": SECTOR_WEIGHTS.SEWERS,
            "dungeons": SECTOR_WEIGHTS.DUNGEONS
        }

    def roll_sector(self):
        self.current_sector = choice(SECTOR_LIST)
        self.current_weights = self._get_weights_dict()[self.current_sector]


sector = Sector()


@dataclass
class Enemy:
    category: str = ''
    size: str = ''
    rarity: str = ''
    name: str = ''
    health: int = 0
    atk: int = 0
    dmg: int = 0

    def _assign_enemy_type(self):
        self.category = ''.join(choices(ENEMY_LISTS.CATEGORY_LIST, weights=Sector.current_weights))
        self.size = ''.join(choices(ENEMY_LISTS.SIZE_LIST, weights=(3, 6, 1)))
        self.rarity = ''.join(choices(ENEMY_LISTS.RARITY_LIST, weights=(16, 3, 1)))

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
            "large undead": ENEMY_NAMES.LARGE_UNDEAD
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


@dataclass
class Item:
    name: str = ''
    type: str = ''
    health: int = 0
    atk: int = 0
    dmg: int = 0
    dfc: int = 0
    psd: int = 0
    is_equipped: bool = False

    def assign_item_type(self):
        self.type = ''.join(choices(ITEM_TYPES_LIST, weights=(1, 1, 2)))

    @staticmethod
    def _get_item_names_dict():
        return {
            "attire": ITEM_NAMES.ATTIRE_NAMES_LIST,
            "weapon": ITEM_NAMES.WEAPON_NAMES_LIST,
            "consumable": ITEM_NAMES.CONSUMABLE_NAMES_LIST
        }

    def assign_item_name(self):
        self.name = choice(self._get_item_names_dict()[self.type])

    def assign_item_adjective(self):
        adjective = ''
        if self.type == 'attire':
            adjective_dict = self._get_flavour_text_dictionaries()["attire_assign_adjective_dict"]
        elif self.type == 'weapon':
            adjective_dict = self._get_flavour_text_dictionaries()["weapon_assign_adjective_dict"]
        else:
            adjective_dict = self._get_flavour_text_dictionaries()["consumable_assign_adjective_dict"]

        for key in adjective_dict:
            if key == (True, True) or key == True:
                adjective_key = key
                adjective_list = adjective_dict[adjective_key]
                adjective = choice(adjective_list)
        if adjective:
            self.name = f"{adjective} {self.name}"

    def inspect_item(self):
        flavour_text = ''
        if self.type == 'attire':
            inspect_dict = self._get_flavour_text_dictionaries()["attire_inspect_flavour_text_dict"]
        elif self.type == 'weapon':
            inspect_dict = self._get_flavour_text_dictionaries()["weapon_inspect_flavour_text_dict"]
        else:
            inspect_dict = self._get_flavour_text_dictionaries()["consumable_inspect_flavour_text_dict"]

        for key in inspect_dict:
            if key == (True, True) or key == True:
                flavour_text_key = key
                flavour_text_list = inspect_dict[flavour_text_key]
                flavour_text = choice(flavour_text_list)
        char_print(flavour_text)

    def roll_item_stats(self):
        if self.type == "attire":
            self.dfc += randint(0, 5)
            self.psd += randint(0, 5)
        elif self.type == "weapon":
            self.atk += randint(0, 5)
            self.dmg += randint(0, 5)
        elif self.type == "consumable":
            self.health += randint(0, 8)

    def _get_flavour_text_dictionaries(self):
        low_value = range(2)
        med_value = range(2, 4)
        high_value = range(4, 11)
        dict_container: dict = {
            "weapon_inspect_flavour_text_dict": {
                (self.atk in low_value, self.dmg in low_value): WEAPON_INSPECT.LOW_ATTACK_LOW_DMG,
                (self.atk in low_value, self.dmg in med_value): WEAPON_INSPECT.LOW_ATTACK_MED_DMG,
                (self.atk in low_value, self.dmg in high_value): WEAPON_INSPECT.LOW_ATTACK_HIGH_DMG,
                (self.atk in med_value, self.dmg in low_value): WEAPON_INSPECT.MED_ATTACK_LOW_DMG,
                (self.atk in med_value, self.dmg in med_value): WEAPON_INSPECT.MED_ATTACK_MED_DMG,
                (self.atk in med_value, self.dmg in high_value): WEAPON_INSPECT.MED_ATTACK_HIGH_DMG,
                (self.atk in high_value, self.dmg in low_value): WEAPON_INSPECT.HIGH_ATTACK_LOW_DMG,
                (self.atk in high_value, self.dmg in med_value): WEAPON_INSPECT.HIGH_ATTACK_MED_DMG,
                (self.atk in high_value, self.dmg in high_value): WEAPON_INSPECT.HIGH_ATTACK_HIGH_DMG,
            },
            "attire_inspect_flavour_text_dict": {
                (self.dfc in low_value, self.psd in low_value): ATTIRE_INSPECT.LOW_DEFENCE_LOW_PERSUADE,
                (self.dfc in low_value, self.psd in med_value): ATTIRE_INSPECT.LOW_DEFENCE_MED_PERSUADE,
                (self.dfc in low_value, self.psd in high_value): ATTIRE_INSPECT.LOW_DEFENCE_HIGH_PERSUADE,
                (self.dfc in med_value, self.psd in low_value): ATTIRE_INSPECT.MED_DEFENCE_LOW_PERSUADE,
                (self.dfc in med_value, self.psd in med_value): ATTIRE_INSPECT.MED_DEFENCE_MED_PERSUADE,
                (self.dfc in med_value, self.psd in high_value): ATTIRE_INSPECT.MED_DEFENCE_HIGH_PERSUADE,
                (self.dfc in high_value, self.psd in low_value): ATTIRE_INSPECT.HIGH_DEFENCE_LOW_PERSUADE,
                (self.dfc in high_value, self.psd in med_value): ATTIRE_INSPECT.HIGH_DEFENCE_MED_PERSUADE,
                (self.dfc in high_value, self.psd in high_value): ATTIRE_INSPECT.HIGH_DEFENCE_HIGH_PERSUADE,
            },
            "consumable_inspect_flavour_text_dict": {
                (self.health in low_value): CONSUMABLE_INSPECT.LOW_HEALTH,
                (self.health in med_value): CONSUMABLE_INSPECT.MED_HEALTH,
                (self.health in high_value): CONSUMABLE_INSPECT.HIGH_HEALTH,
            },
            "attire_assign_adjective_dict": {
                (self.dfc in low_value, self.psd in low_value): ADJECTIVES.ATTIRE_ADJECTIVES["low_psd_low_dfc"],
                (self.dfc in low_value, self.psd in high_value): ADJECTIVES.ATTIRE_ADJECTIVES["high_psd_low_dfc"],
                (self.dfc in high_value, self.psd in low_value): ADJECTIVES.ATTIRE_ADJECTIVES["low_psd_high_dfc"],
                (self.dfc in high_value, self.psd in high_value): ADJECTIVES.ATTIRE_ADJECTIVES["high_psd_high_dfc"],
            },
            "weapon_assign_adjective_dict": {
                (self.atk in low_value, self.dmg in low_value): ADJECTIVES.WEAPON_ADJECTIVES["low_atk_low_dmg"],
                (self.atk in low_value, self.dmg in high_value): ADJECTIVES.WEAPON_ADJECTIVES["low_atk_high_dmg"],
                (self.atk in high_value, self.dmg in low_value): ADJECTIVES.WEAPON_ADJECTIVES["high_atk_low_dmg"],
                (self.atk in high_value, self.dmg in high_value): ADJECTIVES.WEAPON_ADJECTIVES["high_atk_high_dmg"],
            },
            "consumable_assign_adjective_dict": {
                (self.health in low_value): ADJECTIVES.CONSUMABLE_ADJECTIVES["low_health"],
                (self.health in high_value): ADJECTIVES.CONSUMABLE_ADJECTIVES["high_health"]
            }
        }
        return dict_container


@dataclass
class PlayerCharacter:
    name: str = ''
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
        char_print(f"Health: {self.health}/{self.max_health}"
                   f"\nAttack: {self.atk}"
                   f"\nDamage: {self.dmg}"
                   f"\nDefence: {self.dfc}"
                   f"\nPersuasion: {self.psd}")

    def check_is_dead(self):
        if self.health < 1:
            self.run_death_sequence()
            exit()

    @staticmethod
    def run_death_sequence():
        char_print(
            "\nClutching at your chest, your hands come away soaked in blood. Blinking, you stagger backwards and"
            " keel over. Then, the world turns black.")
        char_input("\nYour story has ended. Enter anything to exit.")


player_character = PlayerCharacter()


@dataclass
class PlayerInventory:
    current_equipment = {}

    def append_to_inventory(self, item: Item):
        self.current_equipment.update({item.name.title(): item})

    def remove_from_inventory(self, item: Item):
        del self.current_equipment[item.name.title()]

    def remove_random_item(self, player: PlayerCharacter = player_character):
        if self.current_equipment:
            to_discard = choice(list(self.current_equipment.values()))
            if to_discard.is_equipped:
                char_print("You've lost an equipped item!")
                to_discard.is_equipped = False
                if to_discard.type == "attire":
                    player.dfc -= to_discard.dfc
                    player.psd -= to_discard.psd
                elif to_discard.type == "weapon":
                    player.atk += to_discard.atk
                    player.dmg += to_discard.dmg
            del self.current_equipment[to_discard.name.title()]


player_inventory = PlayerInventory()

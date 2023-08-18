from dataclasses import dataclass
from random import choice
from random import choices, choice, randint

from display import char_print

from constants import (
    ADJECTIVES,
    ITEM_NAMES,
    ITEM_TYPES_LIST,
    WEAPON_INSPECT,
    ATTIRE_INSPECT,
    CONSUMABLE_INSPECT,
)


@dataclass
class Item:
    name: str = ""
    type: str = ""
    health: int = 0
    atk: int = 0
    dmg: int = 0
    dfc: int = 0
    psd: int = 0
    is_equipped: bool = False

    def assign_item_type(self):
        self.type = "".join(choices(ITEM_TYPES_LIST, weights=(1, 1, 2)))

    @staticmethod
    def _get_item_names_dict():
        return {
            "attire": ITEM_NAMES.ATTIRE_NAMES_LIST,
            "weapon": ITEM_NAMES.WEAPON_NAMES_LIST,
            "consumable": ITEM_NAMES.CONSUMABLE_NAMES_LIST,
        }

    def assign_item_name(self):
        self.name = choice(self._get_item_names_dict()[self.type])

    def assign_item_adjective(self):
        adjective = ""
        if self.type == "attire":
            adjective_dict = self._get_flavour_text_dictionaries()[
                "attire_assign_adjective_dict"
            ]
        elif self.type == "weapon":
            adjective_dict = self._get_flavour_text_dictionaries()[
                "weapon_assign_adjective_dict"
            ]
        else:
            adjective_dict = self._get_flavour_text_dictionaries()[
                "consumable_assign_adjective_dict"
            ]

        for key in adjective_dict:
            if key == (True, True) or key == True:
                adjective_key = key
                adjective_list = adjective_dict[adjective_key]
                adjective = choice(adjective_list)
        if adjective:
            self.name = f"{adjective} {self.name}"

    def inspect_item(self):
        flavour_text = ""
        if self.type == "attire":
            inspect_dict = self._get_flavour_text_dictionaries()[
                "attire_inspect_flavour_text_dict"
            ]
        elif self.type == "weapon":
            inspect_dict = self._get_flavour_text_dictionaries()[
                "weapon_inspect_flavour_text_dict"
            ]
        else:
            inspect_dict = self._get_flavour_text_dictionaries()[
                "consumable_inspect_flavour_text_dict"
            ]

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
                (
                    self.atk in low_value,
                    self.dmg in low_value,
                ): WEAPON_INSPECT.LOW_ATTACK_LOW_DMG,
                (
                    self.atk in low_value,
                    self.dmg in med_value,
                ): WEAPON_INSPECT.LOW_ATTACK_MED_DMG,
                (
                    self.atk in low_value,
                    self.dmg in high_value,
                ): WEAPON_INSPECT.LOW_ATTACK_HIGH_DMG,
                (
                    self.atk in med_value,
                    self.dmg in low_value,
                ): WEAPON_INSPECT.MED_ATTACK_LOW_DMG,
                (
                    self.atk in med_value,
                    self.dmg in med_value,
                ): WEAPON_INSPECT.MED_ATTACK_MED_DMG,
                (
                    self.atk in med_value,
                    self.dmg in high_value,
                ): WEAPON_INSPECT.MED_ATTACK_HIGH_DMG,
                (
                    self.atk in high_value,
                    self.dmg in low_value,
                ): WEAPON_INSPECT.HIGH_ATTACK_LOW_DMG,
                (
                    self.atk in high_value,
                    self.dmg in med_value,
                ): WEAPON_INSPECT.HIGH_ATTACK_MED_DMG,
                (
                    self.atk in high_value,
                    self.dmg in high_value,
                ): WEAPON_INSPECT.HIGH_ATTACK_HIGH_DMG,
            },
            "attire_inspect_flavour_text_dict": {
                (
                    self.dfc in low_value,
                    self.psd in low_value,
                ): ATTIRE_INSPECT.LOW_DEFENCE_LOW_PERSUADE,
                (
                    self.dfc in low_value,
                    self.psd in med_value,
                ): ATTIRE_INSPECT.LOW_DEFENCE_MED_PERSUADE,
                (
                    self.dfc in low_value,
                    self.psd in high_value,
                ): ATTIRE_INSPECT.LOW_DEFENCE_HIGH_PERSUADE,
                (
                    self.dfc in med_value,
                    self.psd in low_value,
                ): ATTIRE_INSPECT.MED_DEFENCE_LOW_PERSUADE,
                (
                    self.dfc in med_value,
                    self.psd in med_value,
                ): ATTIRE_INSPECT.MED_DEFENCE_MED_PERSUADE,
                (
                    self.dfc in med_value,
                    self.psd in high_value,
                ): ATTIRE_INSPECT.MED_DEFENCE_HIGH_PERSUADE,
                (
                    self.dfc in high_value,
                    self.psd in low_value,
                ): ATTIRE_INSPECT.HIGH_DEFENCE_LOW_PERSUADE,
                (
                    self.dfc in high_value,
                    self.psd in med_value,
                ): ATTIRE_INSPECT.HIGH_DEFENCE_MED_PERSUADE,
                (
                    self.dfc in high_value,
                    self.psd in high_value,
                ): ATTIRE_INSPECT.HIGH_DEFENCE_HIGH_PERSUADE,
            },
            "consumable_inspect_flavour_text_dict": {
                (self.health in low_value): CONSUMABLE_INSPECT.LOW_HEALTH,
                (self.health in med_value): CONSUMABLE_INSPECT.MED_HEALTH,
                (self.health in high_value): CONSUMABLE_INSPECT.HIGH_HEALTH,
            },
            "attire_assign_adjective_dict": {
                (
                    self.dfc in low_value,
                    self.psd in low_value,
                ): ADJECTIVES.ATTIRE_ADJECTIVES["low_psd_low_dfc"],
                (
                    self.dfc in low_value,
                    self.psd in high_value,
                ): ADJECTIVES.ATTIRE_ADJECTIVES["high_psd_low_dfc"],
                (
                    self.dfc in high_value,
                    self.psd in low_value,
                ): ADJECTIVES.ATTIRE_ADJECTIVES["low_psd_high_dfc"],
                (
                    self.dfc in high_value,
                    self.psd in high_value,
                ): ADJECTIVES.ATTIRE_ADJECTIVES["high_psd_high_dfc"],
            },
            "weapon_assign_adjective_dict": {
                (
                    self.atk in low_value,
                    self.dmg in low_value,
                ): ADJECTIVES.WEAPON_ADJECTIVES["low_atk_low_dmg"],
                (
                    self.atk in low_value,
                    self.dmg in high_value,
                ): ADJECTIVES.WEAPON_ADJECTIVES["low_atk_high_dmg"],
                (
                    self.atk in high_value,
                    self.dmg in low_value,
                ): ADJECTIVES.WEAPON_ADJECTIVES["high_atk_low_dmg"],
                (
                    self.atk in high_value,
                    self.dmg in high_value,
                ): ADJECTIVES.WEAPON_ADJECTIVES["high_atk_high_dmg"],
            },
            "consumable_assign_adjective_dict": {
                (self.health in low_value): ADJECTIVES.CONSUMABLE_ADJECTIVES[
                    "low_health"
                ],
                (self.health in high_value): ADJECTIVES.CONSUMABLE_ADJECTIVES[
                    "high_health"
                ],
            },
        }
        return dict_container

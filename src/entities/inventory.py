from dataclasses import dataclass
from random import choice

from .item import Item
from .player import PlayerCharacter
from display import char_print


@dataclass
class PlayerInventory:
    current_equipment = {}

    def append_to_inventory(self, item: Item):
        self.current_equipment.update({item.name.title(): item})

    def remove_from_inventory(self, item: Item):
        del self.current_equipment[item.name.title()]

    def remove_random_item(self, player: PlayerCharacter):
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

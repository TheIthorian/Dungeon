from entities import (
    PlayerCharacter,
    PlayerInventory,
    Item,
    player_character,
    player_inventory,
)

from display import char_input, char_print


class InventoryLoop:
    def __init__(self):
        self.open_inventory()

    def open_inventory(
        self,
        inventory: PlayerInventory = player_inventory,
        player: PlayerCharacter = player_character,
    ):
        inv_loop = True
        while inv_loop:
            if not inventory.current_equipment:
                char_print("\nYour inventory is empty.")
                inv_loop = False
                break
            char_print("\nYour inventory contains: ")
            for name, item in inventory.current_equipment.items():
                if item.is_equipped:
                    equip_status = " [Equipped] "
                else:
                    equip_status = " "
                if item.type == "attire":
                    item_stats = f"(Defence: {item.dfc}, Persuasion: {item.psd})"
                elif item.type == "weapon":
                    item_stats = f"(Attack: {item.atk}, Damage: {item.dmg})"
                else:
                    item_stats = f"(Healing: {item.health})"
                char_print(f"{name}{equip_status}{item_stats}")
            inv_response = char_input(
                "\nWhat would you like to do? (Equip, Unequip, Discard, View Stats, Go Back): ",
                lower=True,
            )
            if inv_response == "equip":
                self.prompt_equip_item()
            elif inv_response == "unequip":
                self.prompt_unequip_item()
            elif inv_response == "discard":
                self.prompt_discard_item()
            elif inv_response == "view stats":
                player.print_player_character_stats()
            else:
                char_print("\nYou close your backpack.")
                inv_loop = False

    def prompt_equip_item(self, inventory: PlayerInventory = player_inventory):
        to_equip_name = char_input("\nWhat item would you like to equip?: ", title=True)

        if to_equip_name in inventory.current_equipment:
            to_equip = inventory.current_equipment[to_equip_name]
            equipped_item_types = [
                item.type
                for item in inventory.current_equipment.values()
                if item.is_equipped
            ]

            def equip_item():
                if to_equip.is_equipped:
                    char_print(f"\nThe {to_equip_name} is already equipped.")
                elif to_equip.type in equipped_item_types:
                    char_print(
                        f"\nYou must unequip other items of the same type first."
                    )
                else:
                    to_equip.is_equipped = True
                    char_print(f"\nYou equip the {to_equip_name}.")
                    self._item_increase_stat(to_equip)
                    if to_equip.type == "consumable":
                        inventory.remove_from_inventory(to_equip)

            equip_item()

        else:
            char_print("\nItem not found.")

    def prompt_unequip_item(self, inventory: PlayerInventory = player_inventory):
        to_unequip_name = char_input(
            "\nWhat item would you like to unequip?: ", title=True
        )
        if to_unequip_name in inventory.current_equipment:
            to_unequip = inventory.current_equipment[to_unequip_name]

            def unequip_item():
                if not to_unequip.is_equipped:
                    char_print(f"\nThe {to_unequip_name} is already unequipped.")
                else:
                    to_unequip.is_equipped = False
                    char_print(f"\nYou unequip the {to_unequip_name}.")
                    self._item_decrease_stat(to_unequip)

            unequip_item()

        else:
            char_print("\nItem not found.")

    @staticmethod
    def prompt_discard_item(inventory: PlayerInventory = player_inventory):
        to_discard_name = char_input(
            "\nWhat item would you like to discard?: ", title=True
        )
        if to_discard_name in inventory.current_equipment:
            to_discard = inventory.current_equipment[to_discard_name]

            def discard_item():
                if to_discard.is_equipped:
                    char_print(f"\nYou must unequip the {to_discard_name} first.")
                else:
                    char_print(f"\nYou discard the {to_discard_name}.")
                    inventory.remove_from_inventory(to_discard)

            discard_item()

        else:
            char_print("\nItem not found.")

    @staticmethod
    def _item_increase_stat(item: Item, player: PlayerCharacter = player_character):
        if item.type == "attire":
            player.dfc += item.dfc
            player.psd += item.psd
        elif item.type == "weapon":
            player.atk += item.atk
            player.dmg += item.dmg
        elif item.type == "consumable":
            player.health += item.health
            player.cap_health_at_max()

    @staticmethod
    def _item_decrease_stat(item: Item, player: PlayerCharacter = player_character):
        if item.type == "attire":
            player.dfc -= item.dfc
            player.psd -= item.psd
        elif item.type == "weapon":
            player.atk -= item.atk
            player.dmg -= item.dmg


class LootLoop:
    def __init__(self):
        self.loot = Item()
        self.generate_loot()
        self.run_loot_loop()

    def generate_loot(self):
        self.loot.assign_item_type()
        self.loot.assign_item_name()
        self.loot.roll_item_stats()
        self.loot.assign_item_adjective()

    def take_loot(self, inventory: PlayerInventory = player_inventory):
        char_print(f"\nYou take the {self.loot.name}.")
        if self.loot.name in inventory.current_equipment:
            if " i" in self.loot.name:
                self.loot.name = self.loot.name + "i"
            else:
                self.loot.name = self.loot.name + " i"
        inventory.append_to_inventory(self.loot)

    def ignore_loot(self):
        char_print(f"\nYou ignore the {self.loot.name}.")

    def run_loot_loop(self):
        already_inspected = False
        in_loop = True
        counter = 0
        char_print(f"\nYou've found a {self.loot.name}!")
        while in_loop:
            if counter == 3:
                char_print("\nYou've lingered too long here.")
                self.take_loot()
                in_loop = False
                break
            loot_response = char_input(
                f"\nWhat would you like to do? (Take, Ignore, Inspect): "
            )
            if loot_response.lower() == "take":
                self.take_loot()
                in_loop = False
            elif loot_response.lower() == "ignore":
                self.ignore_loot()
                in_loop = False
            elif loot_response.lower() == "inspect":
                if not already_inspected:
                    self.loot.inspect_item()
                    already_inspected = True
                else:
                    char_print("\nYou've already inspected this item.")
            counter += 1
        if not in_loop:
            open_inventory = char_input(
                "\nWould you like to open your inventory? (Y/N): "
            ).lower()
            if open_inventory == "y":
                InventoryLoop()
            else:
                char_print("\nTime to get going then.")

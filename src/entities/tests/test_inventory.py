from entities.inventory import PlayerInventory
from entities.item import Item


class Test_append_to_inventory:
    def test_adds_equipment_to_inventory(self):
        # Given
        player_inventory = PlayerInventory()
        item = Item(
            name="item",
            type="weapon",
        )

        # When
        player_inventory.append_to_inventory("item")

        # Then
        assert player_inventory.current_equipment["Item"] == item


class Test_remove_random_item:
    def test_removes_equipment_from_inventory(self):
        # Given
        player_inventory = PlayerInventory()

        item1 = Item(
            name="item1",
            type="weapon",
        )

        item2 = Item(
            name="item2",
            type="weapon",
        )

        player_inventory.current_equipment = {
            "Item": item1,
            "Item2": item2,
        }

        player = PlayerCharacter(
            name="player",
            atk=10,
            dfc=10,
            dmg=10,
            psd=10,
        )

        # When
        player_inventory.remove_random_item(player)

        # Then
        assert player_inventory.current_equipment["Item1"] == None
        assert player_inventory.current_equipment["Item2"] == item2

    def test_unequips_item(self):
        # Given
        player_inventory = PlayerInventory()

        item1 = Item(
            name="item1",
            type="weapon",
            is_equipped=True,
        )

        player_inventory.current_equipment = {
            "Item": item1,
        }

        player = PlayerCharacter(
            name="player",
            atk=10,
            dfc=10,
            dmg=10,
            psd=10,
        )

        # When
        player_inventory.remove_random_item(player)

        # Then
        assert not item1.is_equipped

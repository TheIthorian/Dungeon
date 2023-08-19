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

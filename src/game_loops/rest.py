from random import randint
from entities import PlayerCharacter

from event_behaviours import RestSpecialEvents

from display import char_print


class RestLoop:
    def __init__(self):
        self._roll_event()
        self._rest_health_gain()

    @staticmethod
    def _roll_event():
        if not randint(0, 5):
            RestSpecialEvents()

    @staticmethod
    def _rest_health_gain(player: PlayerCharacter):
        rest_heal_amount = randint(1, 8)
        player.health += rest_heal_amount
        player.cap_health_at_max()
        char_print(
            f"\nYou gain {rest_heal_amount} health from resting! You now have {player.health} out of a"
            f" maximum of {player.max_health} health."
        )

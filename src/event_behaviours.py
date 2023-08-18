from constants import (
    POSITIVE_EVENTS,
    NEGATIVE_EVENTS,
    ROOM_SPECIAL_EVENTS,
    EXPLORE_SPECIAL_EVENTS,
    REST_SPECIAL_EVENTS,
)
from database import (
    PlayerCharacter,
    PlayerInventory,
    player_character,
    player_inventory,
    char_print,
    char_input,
)
from inventory_loop import LootLoop, InventoryLoop
from dataclasses import dataclass
from random import choice, randint
from combat_loop import CombatLoop


class PositiveEvents:
    def __init__(self):
        self.pos_events_dict = {
            POSITIVE_EVENTS.GAIN_ITEM: "gain_item_effect",
            POSITIVE_EVENTS.GAIN_HEALTH: "gain_health_effect",
            POSITIVE_EVENTS.GAIN_DMG: "gain_dmg_effect",
            POSITIVE_EVENTS.GAIN_MAX_HEALTH: "gain_max_health_effect",
            POSITIVE_EVENTS.GAIN_PSD: "gain_psd_effect",
            POSITIVE_EVENTS.NO_EFFECT: "no_effect",
        }
        self.run_event()

    def run_event(self):
        text, effect = choice(list(self.pos_events_dict.items()))
        char_print(text)

        def get_effect(player: PlayerCharacter = player_character):
            if effect == "gain_item_effect":
                LootLoop()
            elif effect == "gain_health_effect":
                heal_amount = randint(1, 3)
                player.health += heal_amount
                player.cap_health_at_max()
                char_print(
                    f"\nYou gain {heal_amount} health! You now have {player.health} health out of a"
                    f" maximum of {player.max_health}."
                )
            elif effect == "gain_dmg_effect":
                player.dmg += 1
                char_print(f"\nYou gain 1 damage! Your damage is now {player.dmg}.")
            elif effect == "gain_max_health_effect":
                raise_max_health_amount = randint(1, 2)
                player.max_health += raise_max_health_amount
                player.health += raise_max_health_amount
                char_print(
                    f"\nYou gain {raise_max_health_amount} maximum health! You have {player.health} health remaining out of a"
                    f" maximum of {player.max_health}."
                )
            elif effect == "gain_psd_effect":
                player.psd += 1
                char_print(
                    f"\nYou gain 1 persuasion! Your persuasion is now {player.psd}."
                )

            else:
                pass

        get_effect()


class NegativeEvents:
    def __init__(self):
        self.neg_events_dict = {
            NEGATIVE_EVENTS.LOSE_HEALTH: "lose_health_effect",
            NEGATIVE_EVENTS.LOSE_MAX_HEALTH: "lose_max_health_effect",
            NEGATIVE_EVENTS.LOSE_DMG: "lose_dmg_effect",
            NEGATIVE_EVENTS.NO_EFFECT: "no_effect",
        }
        self.run_event()

    def run_event(self):
        text, effect = choice(list(self.neg_events_dict.items()))
        char_print(text)

        def get_effect(player: PlayerCharacter = player_character):
            if effect == "lose_health_effect":
                lose_health_amount = randint(0, 2)
                player.health -= lose_health_amount
                char_print(
                    f"\nYou lose {lose_health_amount} health! You have {player.health} health remaining out of a"
                    f" maximum of {player.max_health}."
                )
            elif effect == "lose_max_health":
                lose_max_health_amount = randint(0, 1)
                player.health -= lose_max_health_amount
                player.cap_health_at_max()
                char_print(
                    f"\nYou lose {lose_max_health_amount} maximum health! You have {player.health} health remaining out of a"
                    f" maximum of {player.max_health}."
                )
            elif effect == "lose_dmg_effect":
                lose_dmg_amount = randint(0, 1)
                player.dmg -= lose_dmg_amount
                char_print(
                    f"\nYou lose {lose_dmg_amount} damage! Your damage is now {player.dmg}"
                )
            else:
                pass

        get_effect()


class RoomSpecialEvents:
    def __init__(self):
        self.special_events_dict = {
            ROOM_SPECIAL_EVENTS.AMBUSH: "ambush_effect",
            ROOM_SPECIAL_EVENTS.HERO: "hero_effect",
            ROOM_SPECIAL_EVENTS.GOBLIN: "goblin_effect",
            ROOM_SPECIAL_EVENTS.SKELETON: "skeleton_effect",
        }
        self.run_event()

    def run_event(self):
        text, effect = choice(list(self.special_events_dict.items()))
        char_print(text)

        def get_effect(player: PlayerCharacter = player_character):
            if effect == "ambush_effect":
                instant_damage = max(1, randint(3, 7) - player.dfc)
                player.health -= instant_damage
                char_print(
                    f"\nBefore your eyes can adjust, it has struck you! You take {instant_damage} damage! You have"
                    f" {player.health} out of {player.max_health} health remaining."
                )
                CombatLoop()
            elif effect == "hero_effect":
                player_response = char_input(
                    "\nWhat will you do? (Nod Along/Interrupt): ", lower=True
                )
                if player_response == "interrupt":
                    nested_response = char_input(
                        "\nYou smell a liar! What will you do? (Accuse/Let Continue): ",
                        lower=True,
                    )
                    if nested_response == "accuse":
                        if randint(0, 1):
                            player.psd -= 1
                            char_print(
                                "\nThe 'hero' shrinks away, embarrassed! Yeah! You showed him... I guess."
                                f" You lose 1 persuasion for being an asshole. You now have {player.psd} persuasion."
                            )
                        else:
                            gain_attack_value = randint(1, 2)
                            player.atk += gain_attack_value
                            char_print(
                                "\nYou're wrong! The hero proves his valour in a sparring match."
                                f" You learn a lot, and gain {gain_attack_value} attack! You now have {player.atk} attack!"
                            )
                    else:
                        char_print(
                            "\nYou decide it's not worth it. Good job on being the bigger person."
                        )
                else:
                    char_print(
                        "\nYou nod along to the story, enjoying the company whilst it lasts."
                    )
            elif effect == "goblin_effect":
                player_response = char_input(
                    "\nWhat will you do? (Attack/Disturb/Let Sleep): ", lower=True
                )
                if player_response == "attack":
                    char_print(
                        "\nYou kill the goblin in its sleep. What the hell?"
                        "You notice its holding something."
                    )
                    LootLoop()
                elif player_response == "disturb":
                    char_print("\nYou wake the goblin... ")
                    if randint(0, 1):
                        player.health -= 1
                        char_print(
                            "\nAnd it promptly bites you before scurrying away into the darkness."
                            f" You lose 1 health. You have {player.health} health remaining out of a"
                            f" maximum of {player.max_health}."
                        )
                    else:
                        char_print(
                            "\nAnd it smiles at you. It's weirdly cute! The two of you share a meal... "
                        )
                        if randint(0, 1):
                            player.health -= 1
                            char_print(
                                f"\nUnfortunately, you let the goblin cook. You feel queasy and lose 1 health."
                                f" You have {player.health} health remaining out of a"
                                f" maximum of {player.max_health}."
                            )
                        else:
                            heal_amount = randint(2, 8)
                            player.health += heal_amount
                            player.max_health += 1
                            char_print(
                                f"\nAnd you feel great! You gain {heal_amount} health and gain 1 maximum health!"
                            )
                else:
                    char_print("\nYou leave the goblin to sleep. That was nice of you.")
            elif effect == "skeleton_effect":
                player_response = char_input(
                    "\nWhat will you do? (Be Silent/Take): ", lower=True
                )
                if player_response == "take":
                    char_print("\nI'll be taking that one!")
                    LootLoop()
                else:
                    player.max_health += 1
                    player.health += 1
                    char_print(
                        "\nYou hold a moment of silence. How noble! You gain 1 maximum health! You now have"
                        f" {player.health} health out of a maximum of {player.max_health}!"
                    )

        get_effect()


@dataclass
class ExploreSpecialEvents:
    def __init__(self):
        self.special_events_dict = {
            EXPLORE_SPECIAL_EVENTS.DARKNESS: "darkness_effect",
            EXPLORE_SPECIAL_EVENTS.BUMP: "bump_effect",
            EXPLORE_SPECIAL_EVENTS.CLOISTER: "cloister_effect",
            EXPLORE_SPECIAL_EVENTS.STEW: "stew_effect",
        }
        self.run_event()

    def run_event(self):
        text, effect = choice(list(self.special_events_dict.items()))
        char_print(text)

        def get_effect(
            player: PlayerCharacter = player_character,
            inventory: PlayerInventory = player_inventory,
        ):
            if effect == "darkness_effect":
                player_response = char_input(
                    "\nWhat do you do? (Light Torch/Keep Going): ", lower=True
                )
                if player_response == "light torch":
                    char_print(
                        "\nYou light the torch, illuminating an enemy in the dark. Startled, it moves to attack."
                    )
                    CombatLoop()
                else:
                    char_print(
                        "\nYou shudder as something brushes against you in the dark, but are otherwise unharmed."
                    )
            elif effect == "bump_effect":
                inventory.remove_random_item()
            elif effect == "cloister_effect":
                player_response = char_input(
                    "\nWhat would you like to do? (Pray/Attack/Leave): ", lower=True
                )
                if player_response == "pray":
                    if randint(0, 1):
                        player.dfc += 1
                        char_print(
                            f"\nYou feel protected. You now have {player.dfc} defence."
                        )
                    else:
                        char_print("\nYou feel nothing.")
                elif player_response == "attack":
                    char_print(
                        "\nThere is an altar in the centre of the cloister. You break it."
                    )
                    if randint(1, 10) == 10:
                        char_print(
                            "\nA shiver runs down your spine. A dark presence has been sated."
                        )
                        max_health_gain = randint(2, 10)
                        damage_gain = randint(1, 5)
                        psd_loss = randint(1, 5)
                        player.max_health += max_health_gain
                        player.health += max_health_gain
                        player.dmg += damage_gain
                        player.psd -= psd_loss
                        char_print(
                            f"\nYou feel powerful. You gained {max_health_gain} maximum health and {damage_gain} "
                            f"damage. The dark pact makes you lose {psd_loss} persuasion."
                        )
                    elif randint(1, 10) == 1:
                        health_loss = randint(1, 10)
                        player.health -= health_loss
                        char_print(
                            f"\nA light strikes you, launching you across the room. You lose {health_loss} health."
                        )
                    else:
                        char_print("\nNothing happens.")
                else:
                    char_print("\nYou leave the cloister alone.")
            elif effect == "stew_effect":
                player_response = char_input(
                    "\nWill you eat the soup? (Y/N): ", lower=True
                )
                if player_response == "y":
                    char_print(
                        "\nYou're not sure what you are eating. Your constitution is tested."
                    )
                    if player.max_health > randint(0, 20):
                        heal_amount = randint(1, 3)
                        char_print(
                            f"\nYou feel nourished. You gain {heal_amount} health."
                        )
                        player.health += heal_amount
                        player.cap_health_at_max()
                    else:
                        char_print(
                            f"\nYou keel over. The orc is sure to tell the others of your weakness! You lose 1 persuasion."
                        )
                        player.psd -= 1
                else:
                    char_print("\nYou politely decline. The orc looks dejected.")

        get_effect()


@dataclass
class RestSpecialEvents:
    def __init__(self):
        self.special_events_dict = {
            REST_SPECIAL_EVENTS.VISITOR: "visitor_effect",
            REST_SPECIAL_EVENTS.BAD_SLEEP: "bad_sleep_effect",
            REST_SPECIAL_EVENTS.GOOD_SLEEP: "good_sleep_effect",
            REST_SPECIAL_EVENTS.BARD: "bard_effect",
            REST_SPECIAL_EVENTS.PIXIE: "pixie_effect",
            REST_SPECIAL_EVENTS.DOG: "dog_effect",
        }
        self.run_event()

    def run_event(self):
        text, effect = choice(list(self.special_events_dict.items()))
        char_print(text)

        def get_effect(
            player: PlayerCharacter = player_character,
            inventory: PlayerInventory = player_inventory,
        ):
            if effect == "visitor_effect":
                player_response = char_input(
                    "Do you take the apple? (Y/N): ", lower=True
                )
                if player_response == "y":
                    if randint(0, 1):
                        char_print(
                            "\nYou eat the apple! Good on you for not judging people on the shape of their nose."
                            "You gain 5 health!"
                        )
                        player.health += 5
                    else:
                        char_print(
                            "\nFoolishly, you eat the apple and fall asleep immediately. Didn't you see the shape of"
                            "her nose? She robs you in the night."
                        )
                        inventory.remove_random_item()
                else:
                    char_print(
                        "\nYou refuse the apple. The hunched figure shuffles away into the dark."
                    )
            elif effect == "bad_sleep_effect":
                bad_sleep_health_penalty = randint(1, 2)
                char_print(
                    f"\nYou have nightmares and lose {bad_sleep_health_penalty} health from poor sleep."
                )
                player.health -= bad_sleep_health_pentalty
            elif effect == "good_sleep_effect":
                good_sleep_health_bonus = randint(1, 4)
                char_print(
                    f"\nYou have good dreams that heal you for {good_sleep_health_bonus} health during the night."
                )
                player.health += good_sleep_health_bonus
            elif effect == "bard_effect":
                player_response = char_input(
                    "\nDo you try to calm him down? (Y/N): ", lower=True
                )
                if player_response == "y":
                    char_print(
                        "\nThe bard insists he is being chased by something! You try to calm him down and he has just"
                        "long enough to accuse you of gaslighting before his pursuer breaks through the door and"
                        "tears him to pieces."
                    )
                    CombatLoop()
                else:
                    nested_response = char_input(
                        "\nThe bard informs you he is being pursued! You pack up your belongings and "
                        "flee! You hear him cry for help behind you! Do you try to help? "
                        "(Y/N): ",
                        lower=True,
                    )
                    if nested_response == "y":
                        char_print(
                            "\nYou turn around but the bard is right behind you! He pushes you aside as he runs past."
                            "Looks like he was just trying to give his pursuer a distraction and now you're in for a"
                            "fight!"
                        )
                        CombatLoop()
                    else:
                        char_print(
                            "\nYou ignore his cry for help. You have a harder time ignoring his blood-curdling scream"
                            "that follows."
                        )
            elif effect == "pixie_effect":
                player_response = char_input(
                    "\nDo you swat the light? (Y/N): ", lower=True
                )
                if player_response == "y":
                    if randint(0, 1):
                        nested_response = char_input(
                            "\nYou swat the light. When you look at your hand, you see a crushed "
                            "pixie. What do you do? (Eat/Smear): ",
                            lower=True,
                        )
                        if nested_response == "eat":
                            char_print(
                                "\nWaste not want not! You gobble the little fellow up and gain 2 maximum health!"
                            )
                            player.max_health += 2
                            player.health += 2
                        else:
                            char_print("\nYou smear the pixie on the floor. Gross.")
                    else:
                        char_print(
                            "\nThe light dodges. You feel a sharp pain in your hand. What the hell? Did it bite you?"
                            "You lose 1 health."
                        )
                        player.health -= 1
                else:
                    if randint(0, 1):
                        char_print("\nA few minutes later, the light disappears.")
                    else:
                        char_print(
                            "\nThe light zips straight in front of your eye. It's like staring in to the sun! How"
                            "are you going to hit anything after being partially blinded? You lose 1 attack."
                        )
                        player.atk -= 1
            elif effect == "dog_effect":
                player_response = char_input(
                    "\nWhat do you do? (Feed/Eat/Kick): ", lower=True
                )
                if player_response == "eat":
                    char_print(
                        "\nWhat the hell is wrong with you? You lunge for the dog. It bites you, dealing 3 damage,"
                        " and scarpers."
                    )
                    player.health -= 3
                elif player_response == "kick":
                    if randint(0, 1):
                        char_print(
                            "\nYou're an asshole. You stub your toe on the dog and lose 1 damage!"
                        )
                        player.dmg -= 1
                    else:
                        char_print(
                            "\nYou're an asshole. An evil voice from the shadows congratulates you, and you gain 1"
                            "damage."
                        )
                        player.dmg += 1
                else:
                    health_gain = randint(5, 10)
                    char_print(
                        "\nYou feed the dog some crumbs and spend the evening petting it. The companionship makes you"
                        f"feel a lot better. You gain {health_gain} health and your maximum increases by 3!"
                    )
                    player.health += health_gain
                    player.max_health += 3
                    player.cap_health_at_max()

            get_effect()

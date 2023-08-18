from database import Enemy, PlayerCharacter, player_character, char_print, char_input
from inventory_loop import LootLoop
from random import randint
from constants import THREAT_RESPONSE, COMBAT_TEXT

enemy_instance = Enemy()


class CombatPrompts:

    def __init__(self):
        self.combat_phase = CombatPhase()

    @staticmethod
    def print_combat_intro():
        char_print(f"\nA {enemy_instance.name} has entered the chamber. You size it up.")
        threat_sum = enemy_instance.health + 3 * enemy_instance.dmg + 3 * enemy_instance.atk
        threat_margins = {threat_sum < 10: THREAT_RESPONSE.NO_THREAT,
                          10 <= threat_sum < 30: THREAT_RESPONSE.LITTLE_THREAT,
                          30 <= threat_sum < 70: THREAT_RESPONSE.SOME_THREAT,
                          70 <= threat_sum < 110: THREAT_RESPONSE.THREATENING,
                          threat_sum >= 110: THREAT_RESPONSE.SERIOUS_THREAT}
        for margin, response in threat_margins.items():
            if margin:
                char_print(response)

    def _prompt_persuade_attempt(self):
        if enemy_instance.get_can_persuade():
            how_to_persuade = char_input("\nHow will you convince them? (Intimidate/Persuade): ", lower=True)
            if how_to_persuade == 'persuade':
                NonCombatRolls.roll_persuade()
            if how_to_persuade == 'intimidate':
                NonCombatRolls.roll_intimidate()
        else:
            char_print("\nYou cannot persuade this enemy! They strike!")
            self.attack_phase()

    def initiate_combat(self):
        counter = 0
        while counter < 3:
            player_response = char_input("\nWhat will you do? (Attack/Persuade/Run): ")
            if player_response.lower() == 'attack':
                self.combat_phase.first_strike()
                self.check_enemy_dead()
                break
            elif player_response.lower() == 'persuade':
                self._prompt_persuade_attempt()
                break
            elif player_response.lower() == 'run':
                NonCombatRolls.roll_run()
                break
            else:
                char_print("\nYou hesitate.")
            counter += 1
        if counter == 3:
            char_print(f"You've hesitated too much! The {enemy_instance.name} makes its move!")
            self.attack_phase()

    @staticmethod
    def prompt_attack_location():
        attack_location_selected = False
        while not attack_location_selected:
            where_to_attack = char_input("\nWhere would you like to attack? (Head/Body/Limbs or Describe Effect): ",
                                         lower=True)
            if where_to_attack == 'describe effect':
                char_print(
                    "\nFor a successful hit, your attack needs to be higher than the opponent's 1d20 dodge roll."
                    "\n\nYour attack will be 1d20 + your attack stat."
                    "\nFor head attacks, subtract 1d10 from this total."
                    "\nFor limb attacks, subtract 1d4 from this total."
                    "\nIf you roll 20 it will be an automatic critical hit regardless of the dodge roll or attack stat."
                    "\n\nOn a successful hit, you deal damage. This subtracts from the enemy's health."
                    "\n\nThe damage you deal will be 1d4 + your damage stat."
                    "\nFor headshots, 4d4 is added to the damage dealt."
                    "\nOn critical hits, damage is doubled or 6 is added (whichever is higher)."
                    "\nFinally, when an enemy hits you, your defence stat subtracts from its damage.")
            else:
                attack_location_selected = True
                return where_to_attack

    def attack_phase(self, player: PlayerCharacter = player_character):
        char_print(f"\nThe {enemy_instance.name} attacks you! ")
        self.combat_phase.roll_enemy_attack()
        player.check_is_dead()
        prompt_run = char_input("\nWould you like to run? (Y/N): ")
        if prompt_run.lower() == 'y':
            NonCombatRolls.roll_run()
        else:
            char_print(f"\nYou attack the {enemy_instance.name}!")
            self.combat_phase.roll_player_attack()
            self.check_enemy_dead()

    def check_enemy_dead(self):
        if enemy_instance.health > 0:
            self.attack_phase()
        else:
            CombatEnds.run_enemy_death()


class CombatEnds:
    @staticmethod
    def end_combat_persuade(player: PlayerCharacter = player_character):
        global enemy_instance
        psd_heal = randint(1, 4)
        player.max_health += randint(0, 1)
        player.health += psd_heal
        player.cap_health_at_max()
        char_print(f"\nThe {enemy_instance.name} lets you stay at their camp. You share a hot meal in strange company."
                   f" You regain {psd_heal} health, bringing you to {player.health} out of a maximum {player.max_health}!")
        enemy_instance = Enemy()

    @staticmethod
    def end_combat_intimidate():
        global enemy_instance
        char_print(f"\nThe {enemy_instance.name} turns and runs, allowing you to loot their camp.")
        loot = char_input("\nWould you like to loot the area? (Y/N): ", lower=True)
        if loot == 'y':
            LootLoop()
        enemy_instance = Enemy()

    @staticmethod
    def run_enemy_death():
        global enemy_instance
        char_print(f"\nThe {enemy_instance.name} falls silent.")
        loot = char_input("\nWould you like to loot their body? (Y/N): ", lower=True)
        if loot == 'y':
            LootLoop()
        enemy_instance = Enemy()


class NonCombatRolls:

    @staticmethod
    def roll_run():
        global enemy_instance
        if randint(1, 2) == 2:
            char_print(COMBAT_TEXT.RUN_SUCCESS)
            enemy_instance = Enemy()
        else:
            char_print(COMBAT_TEXT.RUN_FAIL)
            CombatPrompts().attack_phase()

    @staticmethod
    def roll_persuade(player: PlayerCharacter = player_character):
        persuasion_roll = randint(0, 20)
        final_roll = player.psd + randint(0, 20)
        difficulty = randint(10, 20)
        char_print(f"\nYou rolled {persuasion_roll} + {player.psd}."
                   f" Enemy rolled {difficulty}.")
        if final_roll > difficulty:
            char_print("\nYou convince them.")
            CombatEnds.end_combat_persuade()
        else:
            char_print("\nThey are unconvinced and approach, undeterred.")
            CombatPrompts().attack_phase()

    @staticmethod
    def roll_intimidate(player: PlayerCharacter = player_character):
        player_intimidation = player.dmg + player.health + player.psd
        enemy_intimidation = enemy_instance.dmg + enemy_instance.health + randint(0, 10)
        char_print(f"\nYou have an intimidation score of (DMG: {player.dmg} + HEALTH: {player.health}"
                   f" + PERSUASION: {player.psd}) = {player_intimidation}."
                   f" The enemy has an intimidation score of {enemy_intimidation}.")
        if player_intimidation > enemy_intimidation:
            char_print("\nYou successfully intimidate them.")
            CombatEnds.end_combat_intimidate()
        else:
            char_print("\nThey laugh at you and approach, undeterred.")
            CombatPrompts().attack_phase()


class CombatPhase:

    def __init__(self):
        self.attack_modifier_dict: dict = {}

    def attack_location_modifier(self, where_to_attack='body'):
        if where_to_attack == 'head':
            (attack_location_modifier, damage_location_modifier) = (randint(-10, -1), randint(4, 16))
        elif where_to_attack == 'limbs':
            (attack_location_modifier, damage_location_modifier) = (randint(-4, -1), 0)
        else:
            (attack_location_modifier, damage_location_modifier) = (0, 0)
        self.attack_modifier_dict = {"attack": attack_location_modifier, "damage": damage_location_modifier,
                                     "disarm": where_to_attack == 'limbs', "critical": False}

    @staticmethod
    def disarm_enemy():
        enemy_damage_reduction = int(enemy_instance.dmg / 4)
        enemy_instance.dmg = enemy_damage_reduction
        if enemy_instance.dmg < 0:
            enemy_instance.dmg = 0
        char_print(
            f"\nYou strike at the {enemy_instance.name}'s limbs, reducing their damage by {enemy_damage_reduction}!"
            f" Their base damage is now {enemy_instance.dmg}!")

    def roll_player_attack(self, player: PlayerCharacter = player_character):
        location = CombatPrompts().prompt_attack_location()
        self.attack_location_modifier(where_to_attack=location)
        roll = randint(1, 20) + self.attack_modifier_dict["attack"]
        if roll < 1:
            roll = 1
        attack = roll + player.atk
        dodge = randint(5, 20)
        char_print(f"\nYou rolled an attack of {roll} + {player.atk} and they rolled a dodge roll of {dodge}.")
        if roll == 20:
            self.attack_modifier_dict["critical"] = True
            self.player_attack_hit()
        elif attack > dodge:
            self.player_attack_hit()
        else:
            char_print("\nMiss!")

    def player_attack_hit(self, player: PlayerCharacter = player_character):
        attack_flavour: str = ''
        if self.attack_modifier_dict["disarm"]:
            self.disarm_enemy()
        roll_damage = player.dmg + randint(1, 4) + self.attack_modifier_dict["damage"]
        if self.attack_modifier_dict["critical"]:
            roll_damage = max(2 * roll_damage, roll_damage + 6)
            attack_flavour = 'Critical hit! '
            self.attack_modifier_dict["critical"] = False
        elif roll_damage < 1:
            roll_damage = 1
            attack_flavour = 'Glancing blow! '
        else:
            attack_flavour = 'Hit! '
        char_print(f"\n{attack_flavour}You deal {roll_damage} damage!")
        enemy_instance.health -= roll_damage

    def roll_enemy_attack(self):
        roll = randint(1, 20)
        attack = roll + enemy_instance.atk
        dodge = randint(5, 20)
        char_print(f"\nYou rolled a dodge roll of {dodge} and they rolled an attack of {roll} + {enemy_instance.atk}.")
        if roll == 20:
            self.attack_modifier_dict["critical"] = True
            self.enemy_attack_hit()
        elif attack > dodge:
            self.attack_modifier_dict["critical"] = False
            self.enemy_attack_hit()
        else:
            char_print("\nMiss!")

    def enemy_attack_hit(self, player: PlayerCharacter = player_character):
        roll_damage = enemy_instance.dmg + randint(1, 4)
        attack_flavour: str = ''
        if self.attack_modifier_dict["critical"]:
            roll_damage = max(2 * roll_damage, roll_damage + 6)
            attack_flavour = 'Critical hit! '
            self.attack_modifier_dict["critical"] = False
        elif roll_damage < 1:
            roll_damage = 1
            attack_flavour = 'Glancing blow! '
        else:
            attack_flavour = 'Hit! '
        reduced_damage = max(roll_damage - player.dfc, 1)
        char_print(f"\n{attack_flavour}The {enemy_instance.name} deals {roll_damage} - {player.dfc} damage!")
        player.health -= reduced_damage
        char_print(f"\nYour health is {player.health} out of {player.max_health}.")

    def first_strike(self):
        char_print(f"\nYou attack the {enemy_instance.name} before it can get its bearings.")
        self.roll_player_attack()


class CombatLoop:

    def __init__(self):
        enemy_instance.generate_enemy()
        instance = CombatPrompts()
        instance.print_combat_intro()
        instance.initiate_combat()

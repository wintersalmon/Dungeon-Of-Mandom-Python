# Salmonjoon
# DungeonOfMandom
# 2016.06.01
#
# PhaseChallenge
#

from mandom.hero import Hero
from mandom.weapons.weapon_type import WeaponType


class PhaseChallenge(object):
    def __init__(self, phase_round):
        self.__phase_round = phase_round
        self.challenge_hero = Hero()

        self.monster_in_dungeon = None
        self.weapon_in_dungeon = None
        self.player_in_round = None
        self.hero_sword = None
        self.hero_sword_target = None
        self.challenge_player = None

        self.reset()

    def reset(self):
        self.monster_in_dungeon = self.__phase_round.monster_in_dungeon
        self.weapon_in_dungeon = self.__phase_round.weapon_in_dungeon
        self.player_in_round = self.__phase_round.player_in_round

        self.hero_sword = self.find_hero_sword()
        self.hero_sword_target = None
        self.challenge_player = self.player_in_round[0] if self.player_in_round else None
        self.challenge_hero.equip_weapon(self.weapon_in_dungeon)
        self.challenge_hero.reset_armor()

    def start(self):
        self.reset()
        return True

    def has_next_battle(self):
        # if armor > 0 and monsters > 0 continue
        armor = self.challenge_hero.armor()
        monsters = len(self.monster_in_dungeon)

        if armor > 0 and monsters > 0:
            return True
        else:
            return False

    def end(self):
        # hero has armor left   : player gain victorypoint
        # hero has no life left : player lose lifepoint
        if self.challenge_hero.armor() > 0:
            self.challenge_player.gain_victory_point()
        else:
            self.challenge_player.lose_life_point()

    def find_hero_sword(self):
        for weapon in self.weapon_in_dungeon:
            if weapon.code() == WeaponType.hero_sword:
                return weapon
        return None

    def has_hero_sword(self):
        return self.hero_sword is not None

    def hero_sword_has_target(self):
        return self.hero_sword_target is not None

    def declare_hero_sword(self, monster_code):
        self.hero_sword.declare_target_monster(monster_code)
        self.hero_sword_target = monster_code

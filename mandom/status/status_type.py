# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusType
#

from mandom.containers.auto_number_enum import AutoNumberEnum

class StatusType(AutoNumberEnum):
    none = ()
    
    game = ()
    game_start = ()
    game_next_round = ()
    game_end   = ()
    
    round = ()
    round_start = ()
    round_next_turn = ()
    round_challenge = ()
    round_end = ()
    
    turn = ()
    turn_start = ()
    turn_execute = ()
    turn_end = ()
    
    challenge = ()
    challenge_start = ()
    challenge_next_battle = ()
    challenge_end = ()
    
    battle = ()
    battle_start = ()
    battle_execute = ()
    battle_end = ()
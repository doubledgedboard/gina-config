# stdlib
# from enum import Enum

# class CharacterClass(Enum):
#     ENCHANTER     = "enchanter"      # noqa: E221
#     MAGICIAN      = "magician"       # noqa: E221
#     NECROMANCER   = "necromancer"    # noqa: E221
#     WIZARD        = "wizard"         # noqa: E221
#     CLERIC        = "cleric"         # noqa: E221
#     DRUID         = "druid"          # noqa: E221
#     SHAMAN        = "shaman"         # noqa: E221
#     BARD          = "bard"           # noqa: E221
#     MONK          = "monk"           # noqa: E221
#     RANGER        = "ranger"         # noqa: E221
#     ROGUE         = "rogue"          # noqa: E221
#     PALADIN       = "paladin"        # noqa: E221
#     SHADOW_KNIGHT = "shadow_knight"  # noqa: E221
#     WARRIOR       = "warrior"        # noqa: E221


# character
# name: str
# level: int
# character_class: str
# log_file_path: str

class Character:
    def __init__(self):
        self.name: str = ""
        self.level: int = 0
        self.character_class: str = ""
        self.log_file_path = ""


# trigger group
# name: str

class TriggerGroup:
    def __init__(self):
        self.name: str = ""


# trigger
# name: str
# cast_on_you: str
# cast_on_other: str
# wears_off: str

class Trigger:
    def __init__(self):
        self.name: str = ""
        self.cast_on_you: str = ""
        self.cast_on_other: str = ""
        self.wears_off: str = ""

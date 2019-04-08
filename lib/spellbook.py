from . import gina_config

_spells = []

# filter spells list to spells for the character (Class / Level)
# get_spells_for_characters (filter to enabled only)

# once spells are added to config, they'll be scaled appropriately ??
# or scale them on get ?


def _collect_spells_for_character(character, spells) -> list:
    character_spells = []
    spell_extractor = (
        spell
        for spell
        in spells
        if character['class'] in spell['classes']
        and spell['classes'][character['class']] <= character['level'])
    for spell in spell_extractor:
        character_spells.append(spell)
    return character_spells


def _collect_spells_for_characters(characters, spells) -> list:
    character_and_spells_pairs = []
    for character in characters:
        character_and_spells_pairs.append((
            character,
            _collect_spells_for_character(character, spells)
        ))
    return character_and_spells_pairs


def _add_trigger_groups_for_characters(character_and_spells_pairs) -> None:
    for character_and_spells_pair in character_and_spells_pairs:
        character = character_and_spells_pair[0]
        character_spells = character_and_spells_pair[1]


def _add_buff_to_trigger_groups() -> None:
    pass


def add_trigger_groups_for_characters(characters, spells):
    character_and_spells_pairs = _collect_spells_for_characters(characters, spells)
    _add_trigger_groups_for_characters(character_and_spells_pairs)

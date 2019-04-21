from . import gina_config


# filter spells list to spells for the character (Class / Level)
# get_spells_for_characters (filter to enabled only)

# once spells are added to config, they'll be scaled appropriately ??
# or scale them on get ?


# def _collect_spells_for_characters(characters, spells) -> list:
#     character_and_spells_pairs = []
#     for character in characters:
#         character_and_spells_pairs.append((
#             character,
#             _collect_spells_for_character(character, spells)
#         ))
#     return character_and_spells_pairs


# def _add_trigger_groups_for_characters(character_and_spells_pairs) -> None:
#     for character_and_spells_pair in character_and_spells_pairs:
#         character = character_and_spells_pair[0]
#         character_spells = character_and_spells_pair[1]
#         for spell in character_spells:
#             _add_character_spell_to_trigger_groups(character_spell)


# def add_trigger_groups_for_characters(characters, spells):
#     character_and_spells_pairs = (
#         _collect_spells_for_characters(characters, spells))
#     _scale_spells_for_characters(character_and_spells_pairs)
#     _add_trigger_groups_for_characters(character_and_spells_pairs)


# ============================================================================

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


def add_character_levels_to_spells(characters, spells):
    for character in characters:
        character_spells = _collect_spells_for_character(character, spells)
        for spell in character_spells:
            if 'levels' not in spell:
                spell['levels'] = set()
            spell['levels'].add(character['level'])


# ============================================================================

def _create_parent_trigger_group_for_spell(spell) -> dict:
    spell_trigger_group_id = gina_config.get_next_available_group_id()
    spell_trigger_group = (
        gina_config.generate_trigger_group(
            spell_trigger_group_id,
            spell['name']))
    spell_trigger_group['TriggerGroups'] = []
    return spell_trigger_group


def _add_spell_to_trigger_groups(spell) -> None:
    if spell['type'] == 'Beneficial':
        # attempt to get the current parent spell trigger group
        parent_spell_trigger_group = (
            gina_config.get_buff_trigger_group_by_name(spell['name']))
        # if missing, create the parent spell trigger group
        if not parent_spell_trigger_group:
            parent_spell_trigger_group = (
                _create_parent_trigger_group_for_spell(spell))
            gina_config.add_buff_trigger_group(parent_spell_trigger_group)
        # get a list of spell levels from the current spell trigger group
        current_spell_levels = (
            gina_config.get_trigger_group_names(
                parent_spell_trigger_group['TriggerGroups']))
        # iterate through each spell level
        for spell_level in spell['levels']:
            if spell_level not in current_spell_levels:
                # create trigger group for spell level
                pass


def add_spells_to_trigger_groups(spells):
    for spell in spells:
        _add_spell_to_trigger_groups(spell)

# ============================================================================

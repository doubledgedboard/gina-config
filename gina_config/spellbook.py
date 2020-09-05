# local
import gina_config.trigger_groups
import gina_config.triggers
import gina_config.categories

'''
abstraction over trigger groups and triggers

- each spell added to the book is either
  a beneficial or detrimental

- each spell has a list of associated spell levels

- each spell level has a trigger for "self" vs "others"

- each spell trigger is scaled to the duration for that spell level

- a special trigger for "worn off" is spell level 0
'''

spells: list = []

spellbook_trigger_group = None


def add_spells(spells_to_add):
    spells.extend(spells_to_add)


def spell_is_a_class_spell(spell, class_name) -> bool:
    return class_name in spell['classes']


def character_level_is_high_enough(spell_level, character_level) -> bool:
    return character_level >= spell_level


def get_spells_for_character_class(
        class_name,
        character_level=0):
    return [spell
            for spell
            in spells
            if spell_is_a_class_spell(spell, class_name)
            and character_level_is_high_enough(
                spell['classes'][class_name], character_level)]


def create_worn_off_self_trigger(spell):
    trigger = gina_config.triggers.create_trigger(spell['name'])
    trigger['Category'] = gina_config.categories.ABSORB_BUFFS_CATEGORY


def create_cast_on_self_trigger():
    pass


def create_cast_on_others_trigger():
    pass


def add_worn_off_self_trigger_to_spell(spell, trigger):
    spell['worn_off_self_trigger'] = trigger


def get_worn_off_self_trigger(spell):
    return spell['worn_off_self_trigger']


def spell_has_worn_off_self_trigger(spell) -> bool:
    return 'worn_off_self_trigger' in spell


def ensure_spell_has_worn_off_self_trigger(spell):
    if not spell_has_worn_off_self_trigger:
        add_worn_off_self_trigger_to_spell(
            spell,
            create_worn_off_self_trigger(spell))


def get_spell_trigger_group(spell):
    return gina_config.trigger_groups.find_trigger_group_by_name(
        spell['name'],
        spellbook_trigger_group[])


def add_trigger_for_spell_level(
        spell_trigger_group,
        spell,
        trigger,
        spell_level):
    


def update_trigger_groups_for_spell(spell):
    spell_trigger_group = get_spell_trigger_group(spell)
    if not spell_trigger_group:
        spell_trigger_group = gina_config.trigger_groups.create_trigger_group(
            spell['name'])
    if spell_has_worn_off_self_trigger(spell):
        add_trigger_for_spell_level(
            spell_trigger_group,
            spell,
            get_worn_off_self_trigger(spell),
            0)


def add_spell_triggers_for_character_level(spell, character_level):
    pass


def initialize_spellbook():
    # create root spellbook trigger group
    spellbook_trigger_group = (
        gina_config.trigger_groups.create_trigger_group('Spell Book'))
    # convert to parent
    gina_config.trigger_groups.ensure_trigger_group_is_parent(
        spellbook_trigger_group)
    # add root trigger group
    gina_config.trigger_groups.add_root_trigger_group(spellbook_trigger_group)


# main

initialize_spellbook()

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


# # ============================================================================

# def _collect_spells_for_character(character, spells) -> list:
#     character_spells = []
#     spell_extractor = (
#         spell
#         for spell
#         in spells
#         if character['class'] in spell['classes']
#         and spell['classes'][character['class']] <= character['level'])
#     for spell in spell_extractor:
#         character_spells.append(spell)
#     return character_spells


# def add_character_levels_to_spells(characters, spells):
#     for character in characters:
#         character_spells = _collect_spells_for_character(character, spells)
#         for spell in character_spells:
#             if 'levels' not in spell:
#                 spell['levels'] = set()
#             spell['levels'].add(character['level'])


# # ============================================================================

# def _create_parent_trigger_group_for_spell(spell) -> dict:
#     spell_trigger_group_id = gina_config.get_next_available_group_id()
#     spell_trigger_group = (
#         gina_config.generate_trigger_group(
#             spell_trigger_group_id,
#             spell['name']))
#     spell_trigger_group['TriggerGroups'] = []
#     return spell_trigger_group


# def _add_spell_to_trigger_groups(spell) -> None:
#     if spell['type'] == 'Beneficial':
#         # attempt to get the current parent spell trigger group
#         parent_spell_trigger_group = (
#             gina_config.get_buff_trigger_group_by_name(spell['name']))
#         # if missing, create the parent spell trigger group
#         if not parent_spell_trigger_group:
#             parent_spell_trigger_group = (
#                 _create_parent_trigger_group_for_spell(spell))
#             gina_config.add_buff_trigger_group(parent_spell_trigger_group)
#         # get a list of spell levels from the current spell trigger group
#         current_spell_levels = (
#             gina_config.get_trigger_group_names(
#                 parent_spell_trigger_group['TriggerGroups']))
#         # iterate through each spell level
#         for spell_level in spell['levels']:
#             if spell_level not in current_spell_levels:
#                 # create trigger group for spell level
#                 pass


# def add_spells_to_trigger_groups(spells):
#     for spell in spells:
#         _add_spell_to_trigger_groups(spell)

# # ============================================================================
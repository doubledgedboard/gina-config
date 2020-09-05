import gina_config.spellbook


characters = []


def add_character(character):
    characters.append(character)


def add_spells_to_character(character, spells):
    character['spells'] = spells


def _create_triggers_for_character_spells(character):
    if 'spells' in character:
        for spell in character['spells']:
            gina_config.spellbook.ensure_spell_has_worn_off_self_trigger(spell)
            # gina_config.spellbook.add_spell_triggers_for_character_level(
            #     spell, character['level'])


def update_trigger_groups():
    # generate and add triggers / trigger groups
    # for each spell in each character's
    # list of beneficial / detrimental spells
    for character in characters:
        _create_triggers_for_character_spells(character)


# def get_character(characters: list, character_name: str) -> Character:
#     character = [character
#                  for character
#                  in characters
#                  if character['name'] == character_name][0]
#     return Character(
#         character['name'],
#         character['class'],
#         character['enabled'],
#         character['level'],
#         character['log_file_path'])


# def dump_character(characters: list, character_name: str) -> None:
#     character = get_character(characters, character_name)
#     print('Character')
#     print(f'  Name: {character.name}')
#     print(f'  Class: {character.class_name}')
#     print(f'  Enabled: {character.enabled}')
#     print(f'  Level: {character.level}')
#     print(f'  Log File Path: {character.log_file_path}')

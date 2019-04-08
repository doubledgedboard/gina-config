from typing import NamedTuple


class Character(NamedTuple):
    name: str
    class_name: str
    enabled: bool
    level: int
    log_file_path: str


def get_character(characters: list, character_name: str) -> Character:
    character = [character
                 for character
                 in characters
                 if character['name'] == character_name][0]
    return Character(
        character['name'],
        character['class'],
        character['enabled'],
        character['level'],
        character['log_file_path'])


def dump_character(characters: list, character_name: str) -> None:
    character = get_character(characters, character_name)
    print('Character')
    print(f'  Name: {character.name}')
    print(f'  Class: {character.class_name}')
    print(f'  Enabled: {character.enabled}')
    print(f'  Level: {character.level}')
    print(f'  Log File Path: {character.log_file_path}')
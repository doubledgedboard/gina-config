import json
from typing import NamedTuple, Union

from lib import xml_converter, gina_config


class Character(NamedTuple):
    name: str
    class_name: str
    enabled: bool
    level: int
    log_file_path: str


def action_step(description):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{description}... ', end='')
            func_return_value = func(*args, **kwargs)
            print('done')
            return func_return_value
        return wrapper
    return decorator


def output_step(description):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{description}... ')
            func_return_value = func(*args, **kwargs)
            print('done')
            return func_return_value
        return wrapper
    return decorator


def load_json_file_from_disk(json_file_path: str) -> Union[dict, list]:
    with open(json_file_path, 'r') as json_file:
        json_file_contents = json.load(json_file)
    return json_file_contents


@action_step('loading config file')
def load_config() -> dict:
    return load_json_file_from_disk('data/config.json')


@action_step('loading spells file')
def load_spells() -> list:
    return load_json_file_from_disk('data/spells.json')


@action_step('updating gina config settings')
def update_gina_config_settings(settings) -> None:
    # update gina config settings
    gina_config.settings['EverquestFolder'] = settings['everquest_folder']
    gina_config.settings['ImportedMediaFileFolder'] = (
        settings['imported_media_file_folder'])
    gina_config.settings['LogArchiveFolder'] = settings['log_archive_folder']


def _set_behavior_group_font_size_and_position(
        behavior_group_and_overlay_pair) -> None:
    gina_config.set_behavior_group_font_size(
        behavior_group_and_overlay_pair[0],
        behavior_group_and_overlay_pair[1]['font_size'])
    gina_config.set_behavior_group_position(
        behavior_group_and_overlay_pair[0],
        behavior_group_and_overlay_pair[1]['position'])


def _set_behavior_groups_font_size_and_position(
        behavior_group_and_overlay_pairs) -> None:
    for behavior_group_and_overlay_pair in behavior_group_and_overlay_pairs:
        _set_behavior_group_font_size_and_position(
            behavior_group_and_overlay_pair)


def _collect_behavior_groups_for_overlays(overlays) -> list:
    behavior_group_and_overlay_pairs = []
    for text_overlay in overlays['text']:
        behavior_group_and_overlay_pairs.append((
                gina_config.get_text_behavior_group_by_name(
                    text_overlay['name']),
                text_overlay))
    for timer_overlay in overlays['timer']:
        behavior_group_and_overlay_pairs.append((
                gina_config.get_timer_behavior_group_by_name(
                    timer_overlay['name']),
                timer_overlay))
    return behavior_group_and_overlay_pairs


@action_step('updating gina config behavior groups')
def update_gina_config_behavior_groups(overlays) -> None:
    behavior_group_and_overlay_pairs = (
        _collect_behavior_groups_for_overlays(overlays))
    _set_behavior_groups_font_size_and_position(
        behavior_group_and_overlay_pairs)


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


@action_step('assembling gina config')
def assemble_gina_config(gina_settings) -> dict:
    return {
        'Settings': gina_settings,
        'BehaviorGroups': None,
        'Categories': None,
        'TriggerGroups': None,
        'Characters': None
    }


@output_step('dumping gina config to output')
def dump_gina_config() -> None:
    print(
        xml_converter.export_to_string(
            gina_config.configuration))


@action_step('exporting gina config to file')
def save_gina_config(file_path) -> None:
    xml_converter.export_to_file(
        gina_config.configuration,
        file_path)


@output_step('launching gina')
def launch_gina(gina_path) -> None:
    import os
    os.execvp('rundll32.exe', [
        'rundll32.exe',
        'dfshim.dll,ShOpenVerbShortcut',
        gina_path
    ])


def main():
    # load data files
    config = load_config()
    spells = load_spells()

    update_gina_config_settings(config['settings'])
    update_gina_config_behavior_groups(config['overlays'])
    # dump_gina_config()

    save_gina_config(config['settings']['config_file_path'])

    launch_gina(config['settings']['gina_file_path'])

    # gina_settings = generate_gina_settings(settings)
    # gina_behavior_groups = generate_gina_behavior_groups(settings)
    # gina_config = assemble_gina_config(gina_settings)
    # xml_config = export_gina_config_to_string(gina_config)
    # dump_character(settings['characters'], 'Xarslik')


if __name__ == "__main__":
    main()

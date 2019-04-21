import json
from typing import Union

from lib import gina_config, overlays, settings, spellbook


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


def _load_json_file_from_disk(json_file_path: str) -> Union[dict, list]:
    with open(json_file_path, 'r') as json_file:
        json_file_contents = json.load(json_file)
    return json_file_contents


@action_step('loading config file')
def load_config() -> dict:
    return _load_json_file_from_disk('data/config.json')


@action_step('loading spells file')
def load_spells() -> list:
    return _load_json_file_from_disk('data/spells.json')


@action_step('updating settings')
def update_settings(config) -> None:
    settings.update_settings(config['settings'])


@action_step('updating behavior groups')
def update_behavior_groups(config) -> None:
    overlays.update_behavior_groups(config['overlays'])


@action_step('updating trigger groups')
def update_trigger_groups(config, spells) -> None:
    spellbook.add_character_levels_to_spells(config['characters'], spells)
    spellbook.add_spells_to_trigger_groups(spells)


@output_step('dumping gina config to output')
def dump_gina_config() -> None:
    print(gina_config.export_to_string())


@action_step('exporting gina config to file')
def save_gina_config(config) -> None:
    gina_config.save_to_file(config['settings']['config_file_path'])


@output_step('launching gina')
def launch_gina(config) -> None:
    import os
    os.execvp('rundll32.exe', [
        'rundll32.exe',
        'dfshim.dll,ShOpenVerbShortcut',
        config['settings']['gina_file_path']
    ])


def main():
    # load data files
    config = load_config()
    spells = load_spells()

    update_settings(config)
    update_behavior_groups(config)
    update_trigger_groups(config, spells)

    # print('foo')

    save_gina_config(config)

    launch_gina(config)


if __name__ == "__main__":
    main()

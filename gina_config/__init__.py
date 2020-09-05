# stdlib
from typing import Union
import json

# local
import gina_config.characters
import gina_config.overlays
import gina_config.settings
import gina_config.spellbook
import gina_config.xml_converter


# decorators
# ============================================================================

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


# functions
# ============================================================================

def _load_json_file_from_disk(json_file_path: str) -> Union[dict, list]:
    with open(json_file_path, 'r') as json_file:
        json_file_contents = json.load(json_file)
    return json_file_contents


@action_step('loading config file')
def load_config_file() -> dict:
    return _load_json_file_from_disk('data/config.json')


@action_step('loading spells file')
def load_spells_file() -> list:
    return _load_json_file_from_disk('data/spells.json')


@action_step('updating settings')
def update_settings(config) -> None:
    gina_config.settings.set_everquest_folder_path(
        config['settings']['everquest_folder_path'])
    gina_config.settings.set_imported_media_file_folder_path(
        config['settings']['gina_imported_media_file_folder_path'])
    gina_config.settings.set_log_archive_folder_path(
        config['settings']['everquest_log_archive_folder_path'])


def _update_overlay_font_size_and_position(
        overlay,
        overlay_settings):
    gina_config.overlays.set_overlay_font_size(
        overlay_settings['font_size'],
        overlay)
    gina_config.overlays.set_overlay_bottom_position(
        overlay_settings['bottom_position'],
        overlay)
    gina_config.overlays.set_overlay_left_position(
        overlay_settings['left_position'],
        overlay)
    gina_config.overlays.set_overlay_right_position(
        overlay_settings['right_position'],
        overlay)
    gina_config.overlays.set_overlay_top_position(
        overlay_settings['top_position'],
        overlay)


@action_step('updating overlays')
def update_overlays(config) -> None:
    for overlay_name, overlay_settings in (
            config['overlays']['text'].items()):
        overlay = gina_config.overlays.get_text_overlay(overlay_name)
        _update_overlay_font_size_and_position(
            overlay, overlay_settings)
    for overlay_name, overlay_settings in (
            config['overlays']['timer'].items()):
        overlay = gina_config.overlays.get_timer_overlay(overlay_name)
        _update_overlay_font_size_and_position(
            overlay, overlay_settings)


@action_step('updating spellbook')
def update_spellbook(spells) -> None:
    gina_config.spellbook.add_spells(spells)


@action_step('updating characters')
def update_characters(config) -> None:
    for character in config['characters']:
        character_spells = gina_config.spellbook.get_spells_for_character_class(
            character['class'], character_level=character['level']
        )
        gina_config.characters.add_spells_to_character(
            character,
            character_spells)
        gina_config.characters.add_character(character)


@action_step('updating trigger groups')
def update_trigger_groups() -> None:
    gina_config.characters.update_trigger_groups()
    # add triggers for each spell level
    # spellbook.add_character_levels_to_spells(config['characters'], spells)
    # spellbook.add_spells_to_trigger_groups(spells)


@output_step('dumping gina config to output')
def dump_gina_config() -> None:
    print(gina_config.xml_converter.export_to_string())


@action_step('exporting gina config to file')
def save_gina_config(config) -> None:
    gina_config.xml_converter.export_to_file(
        config['settings']['gina_config_file_path'])


@output_step('launching gina')
def launch_gina(config) -> None:
    import os
    os.execvp('rundll32.exe', [
        'rundll32.exe',
        'dfshim.dll,ShOpenVerbShortcut',
        config['settings']['gina_application_file_path']
    ])


# main
# ============================================================================

def main():
    # load data files
    config = load_config_file()
    spells = load_spells_file()

    update_settings(config)
    update_overlays(config)
    # TODO:
    # add all spells to the spellbook
    # add characters
    # use characters to update trigger groups using spellbook ?
    update_spellbook(spells)
    update_characters(config)
    update_trigger_groups()

    # print('foo')

    # dump_gina_config()
    save_gina_config(config)

    launch_gina(config)

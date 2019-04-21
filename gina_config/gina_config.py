# stdlib
from typing import Optional

# local
from . import xml_converter
import config_data


# what am I thinking?

# in each config section (settings, behavior_groups, etc) have utils that can manage the underlying data type as an abstraction
# e.g. adding trigger groups or triggers

# then at the parent level, have the domain level stuff that orchestrates the underlying config

# trigger_groups = [
#     {
#         'Comments': '',
#         'EnableByDefault': False,
#         'GroupId': 3,
#         'Name': 'Class',
#         'SelfCommented': False,
#         'TriggerGroups': [
#             {
#                 'Comments': '',
#                 'EnableByDefault': False,
#                 'GroupId': 6,
#                 'Name': 'Enchanter',
#                 'SelfCommented': False,
#                 'TriggerGroups': [
#                     {
#                         'Comments': '',
#                         'EnableByDefault': False,
#                         'GroupId': 9,
#                         'Name': 'Buffs',
#                         'SelfCommented': False,
#                         'Triggers': [
#                             {
#                                 'Category': 'Right // HP/AC Buffs',
#                                 'ClipboardText': '',
#                                 'Comments': '',
#                                 'CopyToClipboard': False,
#                                 'CounterResetDuration': 0,
#                                 'DisplayText': '',
#                                 'EnableRegex': True,
#                                 'InterruptSpeech': False,
#                                 'Modified': '2017-11-24T12:47:39',
#                                 'Name': 'Armor of Faith - Other',
#                                 'PlayMediaFile': False,
#                                 'RestartBasedOnTimerName': True,
#                                 'TextToVoiceText': '',
#                                 'TimerDuration': 3780,
#                                 'TimerEarlyEnders': [
#                                     {
#                                         'EarlyEndText': '^{c} lets go of external concerns\.$',
#                                         'EnableRegex': True
#                                     },
#                                     {
#                                         'EarlyEndText': '^{c} lets go of {s}\'s concerns\.$',
#                                         'EnableRegex': True
#                                     }
#                                 ],
#                                 'TimerEndingTime': 300,
#                                 'TimerEndedTrigger': {
#                                     'DisplayText': 'Armor of Faith wore off on {s}',
#                                     'InterruptSpeech': False,
#                                     'PlayMediaFile': False,
#                                     'TextToVoiceText': 'Armor of Faith wore off on {s}',
#                                     'UseText': True,
#                                     'UseTextToVoice': True
#                                 },
#                                 'TimerEndingTrigger': {
#                                     'DisplayText': '5 min left on Armor of Faith - {s}',
#                                     'InterruptSpeech': False,
#                                     'PlayMediaFile': False,
#                                     'TextToVoiceText': '5 min left on Armor of Faith - {s}',
#                                     'UseText': True,
#                                     'UseTextToVoice': True
#                                 },
#                                 'TimerMillisecondDuration': 3780000,
#                                 'TimerName': 'Armor of Faith - {s}',
#                                 'TimerStartBehavior': 'RestartTimer',
#                                 'TimerType': 'Timer',
#                                 'TimerVisibleDuration': 0,
#                                 'TriggerText': '^{s} feels the favor of the gods upon them\.$',
#                                 'UseCounterResetTimer': False,
#                                 'UseFastCheck': False,
#                                 'UseText': False,
#                                 'UseTextToVoice': False,
#                                 'UseTimerEnded': True,
#                                 'UseTimerEnding': True,
#                             }
#                         ]
#                     }
#                 ]
#             }
#         ]
#     }
# ]

characters = []

# characters = [
#     {
#         'AutoMonitor': True,
#         'DisplayName': 'Freckie (project)',
#         'LastArchiveDate': '0001-01-01T00:00:00',
#         'LogFilePath': 'D:\\GAMES\\EverQuest\\Logs\\eqlog_Freckie_project1999.txt',
#         'Name': 'Freckie',
#         'TextStyle': {
#             'FontColor': '#FFFFFF00',
#             'ShadowColor': '#FF000000',
#             'ShadowDepth': 5,
#             'TimerBarColor': '#FF800000',
#         },
#         'TimerStyle': {
#             'FontColor': '#FFFFFF00',
#             'ShadowColor': '#FF000000',
#             'ShadowDepth': 5,
#             'TimerBarColor': '#FF800000',
#         },
#         'TriggerGroups': [
#             9
#         ],
#         'VoiceName': 'Microsoft Zira Desktop',
#         'VoiceSpeed': 0,
#         'Volume': 48
#     }
# ]

configuration = {
    'Settings': config_data.settings,
    'BehaviorGroups': config_data.behavior_groups,
    'Categories': config_data.categories,
    'TriggerGroups': config_data.trigger_groups,
    # 'Characters': characters
}


def _get_behavior_group_by_name_and_type(
        behavior_group_name,
        behavior_group_type) -> dict:
    return next(behavior_group
                for behavior_group
                in behavior_groups
                if behavior_group['Name'] == behavior_group_name and
                behavior_group['BehaviorType'] == behavior_group_type)


def get_text_behavior_group_by_name(behavior_group_name) -> dict:
    return _get_behavior_group_by_name_and_type(behavior_group_name, 'Text')


def get_timer_behavior_group_by_name(behavior_group_name) -> dict:
    return _get_behavior_group_by_name_and_type(behavior_group_name, 'Timer')


def set_behavior_group_font_size(behavior_group, font_size) -> None:
    behavior_group['FontSize'] = font_size


def set_behavior_group_position(behavior_group, position) -> None:
    behavior_group['WindowLayout'][0]['normalPosition']['Bottom'] = (
        position['bottom'])
    behavior_group['WindowLayout'][0]['normalPosition']['Left'] = (
        position['left'])
    behavior_group['WindowLayout'][0]['normalPosition']['Right'] = (
        position['right'])
    behavior_group['WindowLayout'][0]['normalPosition']['Top'] = (
        position['top'])


def export_to_string() -> str:
    return xml_converter.export_to_string(
        configuration)


def save_to_file(file_path) -> None:
    xml_converter.export_to_file(
        configuration,
        file_path)


def _find_trigger_group_by_name(name, trigger_groups) -> Optional[dict]:
    return next((trigger_group
                for trigger_group
                in trigger_groups
                if 'GroupId' in trigger_group
                and trigger_group['Name'] == name), None)


def _find_trigger_group_by_id(id, trigger_groups) -> Optional[dict]:
    return next((trigger_group
                for trigger_group
                in trigger_groups
                if 'GroupId' in trigger_group
                and trigger_group['GroupId'] == id), None)


def _recursive_find_trigger_group_by_name(
        name,
        trigger_groups) -> Optional[dict]:
    for trigger_group in trigger_groups:
        if 'GroupId' in trigger_group:
            if trigger_group['Name'] == name:
                return trigger_group
            if 'TriggerGroups' in trigger_group:
                _trigger_group = _recursive_find_trigger_group_by_name(
                    name,
                    trigger_group['TriggerGroups'])
                if _trigger_group is not None:
                    return _trigger_group
    return None


def _recursive_find_trigger_group_by_id(
        id,
        trigger_groups) -> Optional[dict]:
    for trigger_group in trigger_groups:
        if 'GroupId' in trigger_group:
            if trigger_group['GroupId'] == id:
                return trigger_group
            if 'TriggerGroups' in trigger_group:
                _trigger_group = _recursive_find_trigger_group_by_id(
                    id,
                    trigger_group['TriggerGroups'])
                if _trigger_group is not None:
                    return _trigger_group
    return None


def _recursive_get_trigger_group_ids(trigger_groups) -> list:
    trigger_group_ids = []
    for trigger_group in trigger_groups:
        if 'GroupId' in trigger_group:
            trigger_group_ids.append(trigger_group['GroupId'])
            if 'TriggerGroups' in trigger_group:
                _trigger_group_ids = (
                    _recursive_get_trigger_group_ids(
                        trigger_group['TriggerGroups']))
                trigger_group_ids.extend(_trigger_group_ids)
    return trigger_group_ids


def get_trigger_group_by_name(name) -> Optional[dict]:
    return _recursive_find_trigger_group_by_name(name, trigger_groups)


def get_trigger_group_by_id(id) -> Optional[dict]:
    return _recursive_find_trigger_group_by_id(id, trigger_groups)


def get_buffs_trigger_group() -> dict:
    return get_trigger_group_by_id(BUFFS_GROUP_ID)


def get_debuffs_trigger_group() -> dict:
    return get_trigger_group_by_id(DEBUFFS_GROUP_ID)


def get_trigger_group_names(trigger_groups) -> list:
    trigger_group_names = [
        trigger_group['Name']
        for trigger_group
        in trigger_groups
    ]
    return trigger_group_names


def get_buff_trigger_group_by_name(name) -> Optional[dict]:
    return _find_trigger_group_by_name(
        name,
        get_buffs_trigger_group()['TriggerGroups'])


def get_debuff_trigger_group_by_name(name) -> Optional[dict]:
    return _find_trigger_group_by_name(
        name,
        get_debuffs_trigger_group()['TriggerGroups'])


def _get_next_available_group_id(trigger_group_ids: list) -> int:
    _trigger_group_ids = trigger_group_ids.copy()
    _trigger_group_ids.sort()
    for trigger_group_id in _trigger_group_ids:
        if trigger_group_id + 1 not in _trigger_group_ids:
            return trigger_group_id + 1
    return 1


def get_next_available_group_id() -> int:
    return _get_next_available_group_id(
        _recursive_get_trigger_group_ids(trigger_groups))


def generate_trigger_group(group_id, name) -> dict:
    return {
        'Comments': '',
        'EnableByDefault': False,
        'GroupId': group_id,
        'Name': name,
        'SelfCommented': False,
    }


def generate_trigger(name) -> dict:
    return {
        'Category': 'Right // HP/AC Buffs',
        'ClipboardText': '',
        'Comments': '',
        'CopyToClipboard': False,
        'CounterResetDuration': 0,
        'DisplayText': '',
        'EnableRegex': True,
        'InterruptSpeech': False,
        'Modified': '2017-11-24T12:47:39',
        'Name': 'Armor of Faith - Other',
        'PlayMediaFile': False,
        'RestartBasedOnTimerName': True,
        'TextToVoiceText': '',
        'TimerDuration': 3780,
        'TimerEarlyEnders': [
            {
                'EarlyEndText': '^{c} lets go of external concerns\.$',
                'EnableRegex': True
            },
            {
                'EarlyEndText': '^{c} lets go of {s}\'s concerns\.$',
                'EnableRegex': True
            }
        ],
        'TimerEndingTime': 300,
        'TimerEndedTrigger': {
            'DisplayText': 'Armor of Faith wore off on {s}',
            'InterruptSpeech': False,
            'PlayMediaFile': False,
            'TextToVoiceText': 'Armor of Faith wore off on {s}',
            'UseText': True,
            'UseTextToVoice': True
        },
        'TimerEndingTrigger': {
            'DisplayText': '5 min left on Armor of Faith - {s}',
            'InterruptSpeech': False,
            'PlayMediaFile': False,
            'TextToVoiceText': '5 min left on Armor of Faith - {s}',
            'UseText': True,
            'UseTextToVoice': True
        },
        'TimerMillisecondDuration': 3780000,
        'TimerName': 'Armor of Faith - {s}',
        'TimerStartBehavior': 'RestartTimer',
        'TimerType': 'Timer',
        'TimerVisibleDuration': 0,
        'TriggerText': '^{s} feels the favor of the gods upon them\.$',
        'UseCounterResetTimer': False,
        'UseFastCheck': False,
        'UseText': False,
        'UseTextToVoice': False,
        'UseTimerEnded': True,
        'UseTimerEnding': True
    }


def add_buff_trigger_group(trigger_group) -> None:
    get_buffs_trigger_group()['TriggerGroups'].append(trigger_group)


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


# def generate_trigger_group(group_id, name) -> dict:
#     return {
#         'Comments': '',
#         'EnableByDefault': False,
#         'GroupId': group_id,
#         'Name': name,
#         'SelfCommented': False,
#     }


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



from data import trigger_groups, TRIGGER_GROUPS_KEY_NAME


# constants
# ============================================================================




# public api
# ============================================================================

def next_available_id() -> int:
    '''returns next available trigger group id'''
    pass


def generate_empty() -> dict:
    '''returns an empty trigger group'''
    return {
        'Comments': '',
        'EnableByDefault': False,
        'GroupId': None,
        'Name': None,
        'SelfCommented': False,
    }


def convert_to_parent(group):
    '''allows a group to have children'''
    trigger_groups[TRIGGER_GROUPS_KEY_NAME] = []


def add_group_to_parent(parent, group):
    '''adds a trigger group to a parent group'''
    trigger_groups[TRIGGER_GROUPS_KEY_NAME].append(group)

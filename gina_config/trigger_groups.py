
TRIGGER_GROUPS_KEY_NAME = 'TriggerGroups'
TRIGGERS_KEY_NAME = 'Triggers'


trigger_groups = []
trigger_group_ids = []


# public api
# ============================================================================

def next_available_id() -> int:
    '''returns next available trigger group id'''
    if trigger_group_ids:
        trigger_group_ids.sort()
        return trigger_group_ids[-1] + 1
    else:
        return 1


def create_trigger_group() -> dict:
    '''returns an empty trigger group'''
    return {
        'Comments': '',
        'EnableByDefault': False,
        'GroupId': None,
        'Name': None,
        'SelfCommented': False,
    }


def add_trigger_group(trigger_group):
    '''
    adds a trigger group to the list of trigger groups
    and records the trigger group id in the list of trigger group ids
    '''
    trigger_groups.append(trigger_group)
    trigger_group_ids.append(trigger_group['GroupId'])


def add_child_to_group(parent_trigger_group, child_trigger_group):
    '''adds a child trigger group to a parent trigger group'''
    if TRIGGER_GROUPS_KEY_NAME not in parent_trigger_group:
        parent_trigger_group[TRIGGER_GROUPS_KEY_NAME] = []
    parent_trigger_group[TRIGGER_GROUPS_KEY_NAME].append(child_trigger_group)


def add_trigger_to_group(trigger_group, trigger):
    '''adds a trigger to a trigger group'''


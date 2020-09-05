
TRIGGER_GROUPS_KEY_NAME = 'TriggerGroups'
TRIGGERS_KEY_NAME = 'Triggers'


trigger_groups = []
_next_available_id = 1


# private api
# ============================================================================

def _generate_trigger_group_id() -> int:
    '''
    returns next available trigger group id
    '''
    global _next_available_id
    _generated_id = _next_available_id
    _next_available_id = _next_available_id + 1
    return _generated_id


# public api
# ============================================================================


def trigger_group_has_children(trigger_group):
    return TRIGGER_GROUPS_KEY_NAME in trigger_group


def get_child_trigger_groups(trigger_group):
    return trigger_group[TRIGGER_GROUPS_KEY_NAME]


def ensure_trigger_group_is_parent(trigger_group):
    if TRIGGER_GROUPS_KEY_NAME not in trigger_group:
        trigger_group[TRIGGER_GROUPS_KEY_NAME] = []


def find_trigger_group_by_name(name, trigger_groups):
    return next((trigger_group
                for trigger_group
                in trigger_groups
                if trigger_group['Name'] == name), None)


def create_trigger_group(name, comments='') -> dict:
    '''returns an empty trigger group'''
    return {
        'Comments': comments,
        'EnableByDefault': False,
        'GroupId': _generate_trigger_group_id(),
        'Name': name,
        'SelfCommented': False,
    }


def add_root_trigger_group(trigger_group):
    '''
    adds a root trigger group to the list of trigger groups
    '''
    trigger_groups.append(trigger_group)


def add_child_to_group(parent_trigger_group, child_trigger_group):
    '''adds a child trigger group to a parent trigger group'''
    parent_trigger_group[TRIGGER_GROUPS_KEY_NAME].append(child_trigger_group)


def add_trigger_to_group(trigger_group, trigger):
    '''adds a trigger to a trigger group'''
    pass

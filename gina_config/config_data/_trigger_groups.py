
SPELLS_GROUP_ID = 1
BUFFS_GROUP_ID = 2
DEBUFFS_GROUP_ID = 3

TRIGGER_GROUPS_KEY_NAME = 'TriggerGroups'

trigger_groups = [
    {
        'Comments': '',
        'EnableByDefault': False,
        'GroupId': SPELLS_GROUP_ID,
        'Name': 'Spells',
        'SelfCommented': False,
        TRIGGER_GROUPS_KEY_NAME: [
            {
                'Comments': '',
                'EnableByDefault': False,
                'GroupId': BUFFS_GROUP_ID,
                'Name': 'Buffs',
                'SelfCommented': False,
                TRIGGER_GROUPS_KEY_NAME: []
            },
            {
                'Comments': '',
                'EnableByDefault': False,
                'GroupId': DEBUFFS_GROUP_ID,
                'Name': 'Debuffs',
                'SelfCommented': False,
                TRIGGER_GROUPS_KEY_NAME: []
            }
        ]
    }
]


SPELLS_GROUP_ID = 1
BUFFS_GROUP_ID = 2
DEBUFFS_GROUP_ID = 3

trigger_groups = [
    {
        'Comments': '',
        'EnableByDefault': False,
        'GroupId': SPELLS_GROUP_ID,
        'Name': 'Spells',
        'SelfCommented': False,
        'TriggerGroups': [
            {
                'Comments': '',
                'EnableByDefault': False,
                'GroupId': BUFFS_GROUP_ID,
                'Name': 'Buffs',
                'SelfCommented': False,
                'TriggerGroups': []
            },
            {
                'Comments': '',
                'EnableByDefault': False,
                'GroupId': DEBUFFS_GROUP_ID,
                'Name': 'Debuffs',
                'SelfCommented': False,
                'TriggerGroups': []
            }
        ]
    }
]

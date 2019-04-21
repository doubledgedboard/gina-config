# local
from names.overlays import \
    CRITICAL_ALERTS_OVERLAY, \
    DEBUFFS_OVERLAY, \
    DEFAULT_OVERLAY, \
    OTHER_BUFFS_OVERLAY, \
    SELF_BUFFS_OVERLAY, \
    SHORT_DURATION_BUFFS_OVERLAY, \
    SHORT_DURATION_DEBUFFS_OVERLAY
from fonts import \
    OVERLAY_FONT_NAME


behavior_groups = [
    {
        'BackgroundColor': '#00FFFFFF',
        'BackgroundFadedColor': '#00FFFFFF',
        'BehaviorType': 'Text',
        'EmptyBarColor': '#C4000000',
        'FontName': OVERLAY_FONT_NAME,
        'FontSize': None,  # 30
        'GroupByCharacter': False,
        'Name': CRITICAL_ALERTS_OVERLAY,
        'ShowTimerBar': True,
        'SortMethod': 'OrderTriggered',
        'StandardizeTimerBars': False,
        'TextFadeTime': 10,
        'WindowLayout': [
            {
                'length': 44,
                'flags': 0,
                'showCmd': 1,
                'minPosition': {
                    'X': -1,
                    'Y': -1
                },
                'maxPosition': {
                    'X': -1,
                    'Y': -1
                },
                'normalPosition': {
                    'Bottom': None,
                    'Left': None,
                    'Right': None,
                    'Top': None
                }
            }
        ]
    },
    {
        'BackgroundColor': '#00000000',
        'BackgroundFadedColor': '#00000000',
        'BehaviorType': 'Text',
        'EmptyBarColor': '#D0000000',
        'FontName': OVERLAY_FONT_NAME,
        'FontSize': None,  # 22
        'GroupByCharacter': True,
        'Name': DEFAULT_OVERLAY,
        'ShowTimerBar': True,
        'SortMethod': 'OrderTriggered',
        'StandardizeTimerBars': False,
        'TextFadeTime': 10,
        'WindowLayout': [
            {
                'length': 44,
                'flags': 0,
                'showCmd': 1,
                'minPosition': {
                    'X': -1,
                    'Y': -1
                },
                'maxPosition': {
                    'X': -1,
                    'Y': -1
                },
                'normalPosition': {
                    'Bottom': None,
                    'Left': None,
                    'Right': None,
                    'Top': None
                }
            }
        ]
    },
    {
        'BackgroundColor': '#00000000',
        'BackgroundFadedColor': '#00000000',
        'BehaviorType': 'Timer',
        'EmptyBarColor': '#C4000000',
        'FontName': OVERLAY_FONT_NAME,
        'FontSize': None,  # 14
        'GroupByCharacter': False,
        'Name': DEBUFFS_OVERLAY,
        'ShowTimerBar': True,
        'SortMethod': 'TimeRemaining',
        'StandardizeTimerBars': False,
        'TextFadeTime': 10,
        'WindowLayout': [
            {
                'length': 44,
                'flags': 0,
                'showCmd': 1,
                'minPosition': {
                    'X': -1,
                    'Y': -1
                },
                'maxPosition': {
                    'X': -1,
                    'Y': -1
                },
                'normalPosition': {
                    'Bottom': None,
                    'Left': None,
                    'Right': None,
                    'Top': None
                }
            }
        ]
    },
    {
        'BackgroundColor': '#00000000',
        'BackgroundFadedColor': '#00000000',
        'BehaviorType': 'Timer',
        'EmptyBarColor': '#C4000000',
        'FontName': OVERLAY_FONT_NAME,
        'FontSize': None,  # 13
        'GroupByCharacter': False,
        'Name': OTHER_BUFFS_OVERLAY,
        'ShowTimerBar': True,
        'SortMethod': 'TimeRemaining',
        'StandardizeTimerBars': False,
        'TextFadeTime': 10,
        'WindowLayout': [
            {
                'length': 44,
                'flags': 0,
                'showCmd': 1,
                'minPosition': {
                    'X': -1,
                    'Y': -1
                },
                'maxPosition': {
                    'X': -1,
                    'Y': -1
                },
                'normalPosition': {
                    'Bottom': None,
                    'Left': None,
                    'Right': None,
                    'Top': None
                }
            }
        ]
    },
    {
        'BackgroundColor': '#00000000',
        'BackgroundFadedColor': '#00000000',
        'BehaviorType': 'Timer',
        'EmptyBarColor': '#C4000000',
        'FontName': OVERLAY_FONT_NAME,
        'FontSize': None,  # 13
        'GroupByCharacter': False,
        'Name': SELF_BUFFS_OVERLAY,
        'ShowTimerBar': True,
        'SortMethod': 'TimeRemaining',
        'StandardizeTimerBars': False,
        'TextFadeTime': 10,
        'WindowLayout': [
            {
                'length': 44,
                'flags': 0,
                'showCmd': 1,
                'minPosition': {
                    'X': -1,
                    'Y': -1
                },
                'maxPosition': {
                    'X': -1,
                    'Y': -1
                },
                'normalPosition': {
                    'Bottom': None,
                    'Left': None,
                    'Right': None,
                    'Top': None
                }
            }
        ]
    },
    {
        'BackgroundColor': '#00000000',
        'BackgroundFadedColor': '#00FFFFFF',
        'BehaviorType': 'Timer',
        'EmptyBarColor': '#C4000000',
        'FontName': OVERLAY_FONT_NAME,
        'FontSize': None,  # 18
        'GroupByCharacter': False,
        'Name': SHORT_DURATION_BUFFS_OVERLAY,
        'ShowTimerBar': True,
        'SortMethod': 'OrderTriggered',
        'StandardizeTimerBars': False,
        'TextFadeTime': 10,
        'WindowLayout': [
            {
                'length': 44,
                'flags': 0,
                'showCmd': 1,
                'minPosition': {
                    'X': -1,
                    'Y': -1
                },
                'maxPosition': {
                    'X': -1,
                    'Y': -1
                },
                'normalPosition': {
                    'Bottom': None,
                    'Left': None,
                    'Right': None,
                    'Top': None
                }
            }
        ]
    },
    {
        'BackgroundColor': '#00000000',
        'BackgroundFadedColor': '#00000000',
        'BehaviorType': 'Timer',
        'EmptyBarColor': '#C4000000',
        'FontName': OVERLAY_FONT_NAME,
        'FontSize': None,  # 17
        'GroupByCharacter': False,
        'Name': SHORT_DURATION_DEBUFFS_OVERLAY,
        'ShowTimerBar': True,
        'SortMethod': 'OrderTriggered',
        'StandardizeTimerBars': False,
        'TextFadeTime': 10,
        'WindowLayout': [
            {
                'length': 44,
                'flags': 0,
                'showCmd': 1,
                'minPosition': {
                    'X': -1,
                    'Y': -1
                },
                'maxPosition': {
                    'X': -1,
                    'Y': -1
                },
                'normalPosition': {
                    'Bottom': None,
                    'Left': None,
                    'Right': None,
                    'Top': None
                }
            }
        ]
    }
]

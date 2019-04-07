from enum import Enum


class ColorPalette(Enum):
    BRIGHT_YELLOW = '#FFFFFF00'
    BRIGHT_RED = '#FFFF0000'
    BRIGHT_BLUE = '#FF0000FF'
    DARK_AQUA = '#FF008AA5'
    DARK_PINK = '#FFE20085'
    DARK_PURPLE = '#FF990099'
    DARK_BROWN = '#FF874219'
    DARK_BLUE = '#FF0048AF'
    DARK_RED = '#FF800002'
    DARK_ORANGE = '#FFC17003'
    DARK_GREEN = '#FF006D00'
    DARK_GREY = '#FF7A7A7A'
    DARK_YELLOW = '#FFB5A809'
    LIGHT_BLUE = '#FF697CC1'

    def __str__(self):
        return self.value


DEFAULT_ALERT_COLOR = ColorPalette.BRIGHT_YELLOW
CRITICAL_ALERT_COLOR = ColorPalette.BRIGHT_RED

CHARM_EFFECT_COLOR = ColorPalette.DARK_AQUA
REGEN_EFFECT_COLOR = ColorPalette.DARK_AQUA
MEZ_EFFECT_COLOR = ColorPalette.DARK_PINK
ILLUSION_EFFECT_COLOR = ColorPalette.DARK_PINK
SNARE_EFFECT_COLOR = ColorPalette.DARK_PURPLE
SLOW_EFFECT_COLOR = ColorPalette.DARK_PURPLE
MOVEMENT_SPEED_EFFECT_COLOR = ColorPalette.DARK_PURPLE
ROOT_EFFECT_COLOR = ColorPalette.DARK_BROWN
DAMAGE_SHIELD_EFFECT_COLOR = ColorPalette.DARK_BROWN
ABSORB_EFFECT_COLOR = ColorPalette.DARK_BROWN
MANA_EFFECT_COLOR = ColorPalette.DARK_BLUE
LULL_EFFECT_COLOR = ColorPalette.DARK_BLUE
HEAL_EFFECT_COLOR = ColorPalette.LIGHT_BLUE
DETRIMENTAL_EFFECT_COLOR = ColorPalette.DARK_RED
DOT_EFFECT_COLOR = ColorPalette.DARK_ORANGE
STAT_EFFECT_COLOR = ColorPalette.DARK_ORANGE
HASTE_EFFECT_COLOR = ColorPalette.DARK_GREEN
RESIST_EFFECT_COLOR = ColorPalette.DARK_RED
VISION_EFFECT_COLOR = ColorPalette.DARK_GREY
HC_AC_EFFECT_COLOR = ColorPalette.DARK_YELLOW

EFFECT_WORN_OFF_COLOR = ColorPalette.BRIGHT_BLUE
EFFECT_COOLDOWN_COLOR = ColorPalette.BRIGHT_BLUE


OVERLAY_FONT_NAME = 'Arial Black'

settings = {
    'AcceptShareLevel': 'Anybody',
    'AllowGamTextTriggerShares': True,
    'AllowSharedPackages': True,
    'ArchiveLogs': True,
    'ArchivePurgeDaysToKeep': 365,
    'AutoMergeShareLevel': 'Nobody',
    'AutoUpdate': False,
    'CheckLibraryAtStartup': False,
    'CompressArchivedLogs': True,
    'CTagClipboardReplacement': '{C}',
    'DisplayMatches': True,
    'EnableDebugLog': False,
    'EnableSound': True,
    'EnableText': True,
    'EnableTimers': True,
    'EverquestFolder': None,  # 'D:\\GAMES\\EverQuest',
    'ImportedMediaFileFolder': None,  # 'C:\\Users\\foo\\AppData\\Local\\GimaSoft\\GINA\\ImportedMediaFiles',
    'LogArchiveFolder': 'D:\\GAMES\\EverQuest\\Logs\\Archive',
    'LogArchiveMethod': 'BySize',
    'LogArchiveSchedule': 'Monthly',
    'LogArchiveThresholdSize': 1024000,
    'LogMatchesToFile': False,
    'MasterVolume': 100,
    'MatchDisplayLimit': 100,
    'MatchLogFileName': '',
    'MinimizeToSystemTray': False,
    'PhoneticTransforms': [],
    # 'PhoneticTransforms': [
    #     {
    #         'ActualWord': 'Foo',
    #         'PhoneticWord': 'Foo'
    #     },
    #     {
    #         'ActualWord': 'Bar',
    #         'PhoneticWord': 'Bar'
    #     }
    # ]
    'ProcessorAffinity': 4095,
    'ProfilerRefreshInterval': 30,
    'PurgeArchivedLogs': False,
    'ReferenceToSelf': 'You',
    'RepositoryLastViewed': '1/15/2018 10:50:08 PM -06:00',
    'ShareServiceUri': 'https://eq.gimasoft.com/GINAServices/Package.svc',
    'ShareWhiteList': [],
    'StopSearchingAfterFirstMatch': False
}

behavior_groups = [
    {
        'BackgroundColor': '#00FFFFFF',
        'BackgroundFadedColor': '#00FFFFFF',
        'BehaviorType': 'Text',
        'EmptyBarColor': '#C4000000',
        'FontName': OVERLAY_FONT_NAME,
        'FontSize': None,  # 30
        'GroupByCharacter': False,
        'Name': 'Critical Alerts',
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
        'Name': 'Default',
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
        'Name': 'Debuffs',
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
        'Name': 'Other Buffs',
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
        'Name': 'Self Buffs',
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
        'Name': 'Short Duration Buffs',
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
        'Name': 'Short Duration Debuffs',
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

categories = [
    # Default
    {
        'IsDefault': True,
        'Name': 'Default',
        'TextOverlay': 'Default',
        'TextStyle': {
            'FontColor': DEFAULT_ALERT_COLOR,
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': DEFAULT_ALERT_COLOR,
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
    # Critical Alerts
    {
        'IsDefault': False,
        'Name': 'Critical Alerts',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': CRITICAL_ALERT_COLOR,
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': CRITICAL_ALERT_COLOR,
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
    # Right // Blue (Cooldown)
    {
        'IsDefault': False,
        'Name': 'Right // Blue (Cooldown)',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': EFFECT_COOLDOWN_COLOR,
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': EFFECT_COOLDOWN_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Detrimental Effect
    {
        'IsDefault': False,
        'Name': 'Left // Detrimental Effect',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': DETRIMENTAL_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Worn Off Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self Worn Off Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': EFFECT_WORN_OFF_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Mana Buffs
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Mana Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': MANA_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Debuffs
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Debuffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': DETRIMENTAL_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Travel Buffs
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Travel Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': MOVEMENT_SPEED_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Regen Buffs
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Regen Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': REGEN_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Haste Buffs
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Haste Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': HASTE_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Slow
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Slow',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Debuffs',
        'TimerStyle': {
            'FontColor': '#FFDBDBDB',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': SLOW_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Snare
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Snare',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Debuffs',
        'TimerStyle': {
            'FontColor': '#FFDBDBDB',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': SNARE_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Charm
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Charm',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': CHARM_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration DoT AoE
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration DoT AoE',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': DOT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Resist Buffs
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Resist Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': RESIST_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Stat Buffs
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Stat Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': STAT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Charm Effect
    {
        'IsDefault': False,
        'Name': 'Left // Charm Effect',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': CHARM_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Mez Effect
    {
        'IsDefault': False,
        'Name': 'Left // Mez Effect',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': MEZ_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Haste Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self Haste Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': HASTE_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Mana Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self Mana Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': MANA_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Haste Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Haste Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': HASTE_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Regen Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self Regen Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': REGEN_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Regen Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Regen Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': REGEN_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Stat Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self Stat Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': STAT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self HP/AC Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self HP/AC Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': HC_AC_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Resist Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self Resist Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': RESIST_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Travel Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self Travel Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': MOVEMENT_SPEED_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Vision Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self Vision Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': VISION_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Illusion Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self Illusion Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': ILLUSION_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // HP/AC Buffs
    {
        'IsDefault': False,
        'Name': 'Right // HP/AC Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': HC_AC_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Illusion Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Illusion Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': ILLUSION_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Mana Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Mana Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': MANA_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Resist Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Resist Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': RESIST_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Stat Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Stat Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': STAT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Travel Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Travel Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': MOVEMENT_SPEED_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Vision Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Vision Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': VISION_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Mez
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Mez',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': MEZ_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self DS Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self DS Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': DAMAGE_SHIELD_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Absorb Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self Absorb Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': ABSORB_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // DS Buffs
    {
        'IsDefault': False,
        'Name': 'Right // DS Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': DAMAGE_SHIELD_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Absorb Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Absorb Buffs',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': ABSORB_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // DoT Effect
    {
        'IsDefault': False,
        'Name': 'Left // DoT Effect',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': DOT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Slow Effect
    {
        'IsDefault': False,
        'Name': 'Left // Slow Effect',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': SLOW_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Snare Effect
    {
        'IsDefault': False,
        'Name': 'Left // Snare Effect',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': SNARE_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Root Effect
    {
        'IsDefault': False,
        'Name': 'Left // Root Effect',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': ROOT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Lull Effect
    {
        'IsDefault': False,
        'Name': 'Left // Lull Effect',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': LULL_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # # Highlighted Default (Bright Green)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (Bright Green)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': '#FF21FF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Bright Orange)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (Bright Orange)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': '#FFFFA500',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Bright Red)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (Bright Red)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': '#FFFF0000',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Aqua)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (Aqua)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': ColorPalette.DARK_AQUA,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Root)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (Root)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': ROOT_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (DS)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (DS)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': DAMAGE_SHIELD_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Absorb)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (Absorb)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': ABSORB_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Mez)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (Mez)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': MEZ_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Heal)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (Heal)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': HEAL_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Slow)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (Slow)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': SLOW_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Snare)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (Snare)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': SNARE_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Debuff)
    # {
    #     'IsDefault': False,
    #     'Name': 'Highlighted Default (Debuff)',
    #     'TextOverlay': 'Default',
    #     'TextStyle': {
    #         'FontColor': DETRIMENTAL_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': 'Self Buffs',
    #     'TimerStyle': {
    #         'FontColor': '#FFFFFF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # Middle // Short Duration Lull
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Lull',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Short Duration Debuffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': LULL_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    }
]

trigger_groups = []

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
    'Settings': settings,
    'BehaviorGroups': behavior_groups,
    'Categories': categories,
    # 'TriggerGroups': trigger_groups,
    # 'Characters': characters
}

# print(xml.serialize_to_string(settings_processor, settings, indent='    '))
# print(xml.serialize_to_string(behavior_groups_processor, behavior_groups, indent='    '))
# print(xml.serialize_to_string(configuration_processor, configuration, indent='    '))
# xml.serialize_to_file(configuration_processor, configuration, xml_file_path='GINA.xml', indent='    ')


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

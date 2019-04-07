OVERLAY_FONT_NAME = 'Arial Black'

settings = {
    'AcceptShareLevel': 'Anybody',
    'AllowGamTextTriggerShares': True,
    'AllowSharedPackages': True,
    'ArchiveLogs': True,
    'ArchivePurgeDaysToKeep': 365,
    'AutoMergeShareLevel': 'Nobody',
    'AutoUpdate': True,
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
    # Default (Yellow)
    {
        'IsDefault': True,
        'Name': 'Default (Yellow)',
        'TextOverlay': 'Default',
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
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
    # Right // Green (Beneficial Effect)
    {
        'IsDefault': False,
        'Name': 'Right // Green (Beneficial Effect)',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FF008000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': 'Other Buffs',
        'TimerStyle': {
            'FontColor': '#FFDDDDDD',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF006800'
        },
        'TimerStyleSource': 'None'
    },
    # Right // Blue (Cooldown)
    {
        'IsDefault': False,
        'Name': 'Right // Blue (Cooldown)',
        'TextOverlay': 'Critical Alerts',
        'TextStyle': {
            'FontColor': '#FF0000FF',
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
            'TimerBarColor': '#FF0000FF'
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
            'TimerBarColor': '#FF800002'
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
            'TimerBarColor': '#FF0000FF'
        },
        'TimerStyleSource': 'None'
    },
    # Right // Blue (Self Beneficial Effect)
    {
        'IsDefault': False,
        'Name': 'Right // Blue (Self Beneficial Effect)',
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
            'FontColor': '#FFB5B5B5',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF0000C9'
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
            'TimerBarColor': '#FF0048AF'
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
        'TimerOverlay': 'Short Duration Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF680001'
        },
        'TimerStyleSource': 'None'
    },
    # Highlighted Default (Bright Green)
    {
        'IsDefault': False,
        'Name': 'Highlighted Default (Bright Green)',
        'TextOverlay': 'Default',
        'TextStyle': {
            'FontColor': '#FF21FF00',
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
            'TimerBarColor': '#FF800000'
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
            'TimerBarColor': '#FF990099'
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
            'TimerBarColor': '#FF008AA5'
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
            'TimerBarColor': '#FF006D00'
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Slow / Snare
    {
        'IsDefault': False,
        'Name': 'Middle // Short Duration Slow / Snare',
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
            'TimerBarColor': '#FF990099'
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
            'TimerBarColor': '#FF008AA5'
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
            'TimerBarColor': '#FFC17003'
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
            'TimerBarColor': '#FF8C1600'
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
            'TimerBarColor': '#FFC17003'
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
            'TimerBarColor': '#FF008AA5'
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
            'TimerBarColor': '#FFE20085'
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
            'TimerBarColor': '#FF006D00'
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
            'TimerBarColor': '#FF0048AF'
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
            'TimerBarColor': '#FF006D00'
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Regen Buffs
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
        'TimerOverlay': 'Self Buffs',
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF008AA5'
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
            'TimerBarColor': '#FF008AA5'
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
            'TimerBarColor': '#FFC17003'
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
            'TimerBarColor': '#FFB5A809'
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
            'TimerBarColor': '#FF8C1600'
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
            'TimerBarColor': '#FF990099'
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
            'TimerBarColor': '#FF7A7A7A'
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
            'TimerBarColor': '#FFE20085'
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
            'TimerBarColor': '#FFB5A809'
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
            'TimerBarColor': '#FFE20085'
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
            'TimerBarColor': '#FF0048AF'
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
            'TimerBarColor': '#FF8C1600'
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
            'TimerBarColor': '#FFC17003'
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
            'TimerBarColor': '#FF990099'
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
            'TimerBarColor': '#FF7A7A7A'
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
            'TimerBarColor': '#FFE20085'
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self DS / Absorb Buffs
    {
        'IsDefault': False,
        'Name': 'Right // Self DS / Absorb Buffs',
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
            'TimerBarColor': '#FF874219'
        },
        'TimerStyleSource': 'None'
    },
    # Right // DS / Absorb Buffs
    {
        'IsDefault': False,
        'Name': 'Right // DS / Absorb Buffs',
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
            'TimerBarColor': '#FF874219'
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
            'TimerBarColor': '#FFC17003'
        },
        'TimerStyleSource': 'None'
    },
    # Left // Slow / Snare Effect
    {
        'IsDefault': False,
        'Name': 'Left // Slow / Snare Effect',
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
            'TimerBarColor': '#FF990099'
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
            'TimerBarColor': '#FF874219'
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
            'TimerBarColor': '#FF0048AF'
        },
        'TimerStyleSource': 'None'
    },
    # Highlighted Default (Bright Orange)
    {
        'IsDefault': False,
        'Name': 'Highlighted Default (Bright Orange)',
        'TextOverlay': 'Default',
        'TextStyle': {
            'FontColor': '#FFFFA500',
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
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
    # Highlighted Default (Bright Red)
    {
        'IsDefault': False,
        'Name': 'Highlighted Default (Bright Red)',
        'TextOverlay': 'Default',
        'TextStyle': {
            'FontColor': '#FFFF0000',
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
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
    # Highlighted Default (Aqua)
    {
        'IsDefault': False,
        'Name': 'Highlighted Default (Aqua)',
        'TextOverlay': 'Default',
        'TextStyle': {
            'FontColor': '#FF008AA5',
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
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
    # Highlighted Default (Brown)
    {
        'IsDefault': False,
        'Name': 'Highlighted Default (Brown)',
        'TextOverlay': 'Default',
        'TextStyle': {
            'FontColor': '#FF874219',
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
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
    # Highlighted Default (Pink)
    {
        'IsDefault': False,
        'Name': 'Highlighted Default (Pink)',
        'TextOverlay': 'Default',
        'TextStyle': {
            'FontColor': '#FFE20085',
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
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
    # Highlighted Default (Blue)
    {
        'IsDefault': False,
        'Name': 'Highlighted Default (Blue)',
        'TextOverlay': 'Default',
        'TextStyle': {
            'FontColor': '#FF697CC1',
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
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
    # Highlighted Default (Purple)
    {
        'IsDefault': False,
        'Name': 'Highlighted Default (Purple)',
        'TextOverlay': 'Default',
        'TextStyle': {
            'FontColor': '#FF990099',
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
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
    # Highlighted Default (Red)
    {
        'IsDefault': False,
        'Name': 'Highlighted Default (Red)',
        'TextOverlay': 'Default',
        'TextStyle': {
            'FontColor': '#FF680001',
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
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
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
            'TimerBarColor': '#FF0048AF'
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
    # 'Categories': categories,
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

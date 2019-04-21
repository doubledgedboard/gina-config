from gina_config.names.settings import \
    EVERQUEST_FOLDER_SETTING, \
    IMPORTED_MEDIA_FILE_FOLDER_SETTING, \
    LOG_ARCHIVE_FOLDER_SETTING


# constants
# ============================================================================

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
    EVERQUEST_FOLDER_SETTING: None,  # 'D:\\GAMES\\EverQuest',
    IMPORTED_MEDIA_FILE_FOLDER_SETTING: None,  # 'C:\\Users\\foo\\AppData\\Local\\GimaSoft\\GINA\\ImportedMediaFiles',
    LOG_ARCHIVE_FOLDER_SETTING: 'D:\\GAMES\\EverQuest\\Logs\\Archive',
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

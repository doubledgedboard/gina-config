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
    'LogArchiveFolder': None,
    'LogArchiveMethod': 'BySize',
    'LogArchiveSchedule': 'Monthly',
    'LogArchiveThresholdSize': 1024000,
    'LogMatchesToFile': False,
    'MasterVolume': 100,
    'MatchDisplayLimit': 100,
    'MatchLogFileName': '',
    'MinimizeToSystemTray': False,
    'PhoneticTransforms': [],
    'ProcessorAffinity': 4095,
    'ProfilerRefreshInterval': 30,
    'PurgeArchivedLogs': False,
    'ReferenceToSelf': 'You',
    'RepositoryLastViewed': '1/15/2018 10:50:08 PM -06:00',
    'ShareServiceUri': 'https://eq.gimasoft.com/GINAServices/Package.svc',
    'ShareWhiteList': [],
    'StopSearchingAfterFirstMatch': False
}


def add_phonetic_transform(self, actual_word, phonetic_word):
    self._settings['PhoneticTransforms'].append({
        'ActualWord': actual_word,
        'PhoneticWord': phonetic_word
    })


def set_everquest_folder_path(path):
    settings['EverquestFolder'] = path


def set_imported_media_file_folder_path(path):
    settings['ImportedMediaFileFolder'] = path


def set_log_archive_folder_path(path):
    settings['LogArchiveFolder'] = path

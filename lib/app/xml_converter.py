import declxml as xml

#   <Settings>
#     <AcceptShareLevel>Anybody</AcceptShareLevel>
#     <AllowGamTextTriggerShares>True</AllowGamTextTriggerShares>
#     <AllowSharedPackages>True</AllowSharedPackages>
#     <ArchiveLogs>True</ArchiveLogs>
#     <ArchivePurgeDaysToKeep>365</ArchivePurgeDaysToKeep>
#     <AutoMergeShareLevel>Nobody</AutoMergeShareLevel>
#     <AutoUpdate>True</AutoUpdate>
#     <CheckLibraryAtStartup>False</CheckLibraryAtStartup>
#     <CompressArchivedLogs>True</CompressArchivedLogs>
#     <CTagClipboardReplacement>{C}</CTagClipboardReplacement>
#     <DisplayMatches>True</DisplayMatches>
#     <EnableDebugLog>False</EnableDebugLog>
#     <EnableSound>True</EnableSound>
#     <EnableText>True</EnableText>
#     <EnableTimers>True</EnableTimers>
#     <EverquestFolder>D:\GAMES\EverQuest</EverquestFolder>
#     <ImportedMediaFileFolder>C:\Users\foo\AppData\Local\GimaSoft\GINA\ImportedMediaFiles</ImportedMediaFileFolder>
#     <LogArchiveFolder>D:\GAMES\EverQuest\Logs\Archive</LogArchiveFolder>
#     <LogArchiveMethod>BySize</LogArchiveMethod>
#     <LogArchiveSchedule>Monthly</LogArchiveSchedule>
#     <LogArchiveThresholdSize>104857600</LogArchiveThresholdSize>
#     <LogMatchesToFile>False</LogMatchesToFile>
#     <MasterVolume>100</MasterVolume>
#     <MatchDisplayLimit>100</MatchDisplayLimit>
#     <MatchLogFileName></MatchLogFileName>
#     <MinimizeToSystemTray>False</MinimizeToSystemTray>
#     <PhoneticTransforms>
#       <Transform>
#         <ActualWord>Foo</ActualWord>
#         <PhoneticWord>Foo</PhoneticWord>
#       </Transform>
#       <Transform>
#         <ActualWord>Bar</ActualWord>
#         <PhoneticWord>Bar</PhoneticWord>
#       </Transform>
#     </PhoneticTransforms>
#     <ProcessorAffinity>4095</ProcessorAffinity>
#     <ProfilerRefreshInterval>30</ProfilerRefreshInterval>
#     <PurgeArchivedLogs>False</PurgeArchivedLogs>
#     <ReferenceToSelf>You</ReferenceToSelf>
#     <RepositoryLastViewed>1/15/2018 10:50:08 PM -06:00</RepositoryLastViewed>
#     <ShareServiceUri>https://eq.gimasoft.com/GINAServices/Package.svc</ShareServiceUri>
#     <ShareWhiteList />
#     <StopSearchingAfterFirstMatch>False</StopSearchingAfterFirstMatch>
#   </Settings>

settings_processor = xml.dictionary('Settings', [
    xml.string('AcceptShareLevel'),
    xml.boolean('AllowGamTextTriggerShares'),
    xml.boolean('AllowSharedPackages'),
    xml.boolean('ArchiveLogs'),
    xml.integer('ArchivePurgeDaysToKeep'),
    xml.string('AutoMergeShareLevel'),
    xml.boolean('AutoUpdate'),
    xml.boolean('CheckLibraryAtStartup'),
    xml.boolean('CompressArchivedLogs'),
    xml.string('CTagClipboardReplacement'),
    xml.boolean('DisplayMatches'),
    xml.boolean('EnableDebugLog'),
    xml.boolean('EnableSound'),
    xml.boolean('EnableText'),
    xml.boolean('EnableTimers'),
    xml.string('EverquestFolder'),
    xml.string('ImportedMediaFileFolder'),
    xml.string('LogArchiveFolder'),
    xml.string('LogArchiveMethod'),
    xml.string('LogArchiveSchedule'),
    xml.integer('LogArchiveThresholdSize'),
    xml.boolean('LogMatchesToFile'),
    xml.integer('MasterVolume'),
    xml.integer('MatchDisplayLimit'),
    xml.string('MatchLogFileName'),
    xml.boolean('MinimizeToSystemTray'),
    xml.array(xml.dictionary('Transform', [
        xml.string('ActualWord'),
        xml.string('PhoneticWord')
    ]), nested='PhoneticTransforms'),
    xml.integer('ProcessorAffinity'),
    xml.integer('ProfilerRefreshInterval'),
    xml.boolean('PurgeArchivedLogs'),
    xml.string('ReferenceToSelf'),
    xml.string('RepositoryLastViewed'),
    xml.string('ShareServiceUri'),
    xml.array(xml.string('Character', required=False),
              nested='ShareWhiteList'),
    xml.boolean('StopSearchingAfterFirstMatch')])

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
    'EverquestFolder': 'D:\\GAMES\\EverQuest',
    'ImportedMediaFileFolder':
        'C:\\Users\\foo\\AppData\\Local\\GimaSoft\\GINA\\ImportedMediaFiles',
    'LogArchiveFolder': 'D:\\GAMES\\EverQuest\\Logs\\Archive',
    'LogArchiveMethod': 'BySize',
    'LogArchiveSchedule': 'Monthly',
    'LogArchiveThresholdSize': 104857600,
    'LogMatchesToFile': False,
    'MasterVolume': 100,
    'MatchDisplayLimit': 100,
    'MatchLogFileName': '',
    'MinimizeToSystemTray': False,
    'PhoneticTransforms': [
        {
            'ActualWord': 'Foo',
            'PhoneticWord': 'Foo'
        },
        {
            'ActualWord': 'Bar',
            'PhoneticWord': 'Bar'
        }
    ],
    'ProcessorAffinity': 4095,
    'ProfilerRefreshInterval': 30,
    'PurgeArchivedLogs': False,
    'ReferenceToSelf': 'You',
    'RepositoryLastViewed': '1/15/2018 10:50:08 PM -06:00',
    'ShareServiceUri': 'https://eq.gimasoft.com/GINAServices/Package.svc',
    'ShareWhiteList': [],
    'StopSearchingAfterFirstMatch': False
}

print(xml.serialize_to_string(settings_processor, settings, indent='    '))

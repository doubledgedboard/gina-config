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

# <BehaviorGroups>
#     <Behavior>
#         <BehaviorType>Text</BehaviorType>
#         <Name>Default</Name>
#         <FontName>Arial Black</FontName>
#         <FontSize>22</FontSize>
#         <GroupByCharacter>True</GroupByCharacter>
#         <SortMethod>OrderTriggered</SortMethod>
#         <TextFadeTime>10</TextFadeTime>
#         <ShowTimerBar>True</ShowTimerBar>
#         <EmptyBarColor>#D0000000</EmptyBarColor>
#         <StandardizeTimerBars>False</StandardizeTimerBars>
#         <BackgroundColor>#00000000</BackgroundColor>
#         <BackgroundFadedColor>#00000000</BackgroundFadedColor>
#         <WindowLayout>
#             <WINDOWPLACEMENT>
#                 <length>44</length>
#                 <flags>0</flags>
#                 <showCmd>1</showCmd>
#                 <minPosition>
#                     <X>-1</X>
#                     <Y>-1</Y>
#                 </minPosition>
#                 <maxPosition>
#                     <X>-1</X>
#                     <Y>-1</Y>
#                 </maxPosition>
#                 <normalPosition>
#                     <Left>980</Left>
#                     <Top>371</Top>
#                     <Right>1745</Right>
#                     <Bottom>737</Bottom>
#                 </normalPosition>
#             </WINDOWPLACEMENT>
#         </WindowLayout>
#     </Behavior>
# </BehaviorGroups>

behavior_groups_processor = xml.array(
    xml.dictionary('Behavior', [
        xml.string('BackgroundColor'),
        xml.string('BackgroundFadedColor'),
        xml.string('BehaviorType'),
        xml.string('EmptyBarColor'),
        xml.string('FontName'),
        xml.integer('FontSize'),
        xml.boolean('GroupByCharacter'),
        xml.string('Name'),
        xml.boolean('ShowTimerBar'),
        xml.string('SortMethod'),
        xml.boolean('StandardizeTimerBars'),
        xml.integer('TextFadeTime'),
        xml.array(
            xml.dictionary('WINDOWPLACEMENT', [
                xml.integer('flags'),
                xml.integer('length'),
                xml.dictionary('maxPosition', [
                    xml.integer('X'),
                    xml.integer('Y')
                ]),
                xml.dictionary('minPosition', [
                    xml.integer('X'),
                    xml.integer('Y')
                ]),
                xml.dictionary('normalPosition', [
                    xml.integer('Left'),
                    xml.integer('Top'),
                    xml.integer('Right'),
                    xml.integer('Bottom')
                ]),
                xml.integer('showCmd')
            ]),
            nested='WindowLayout')
    ]),
    nested='BehaviorGroups')

#   <Categories>
#     <Category>
#       <IsDefault>True</IsDefault>
#       <Name>Default (Yellow)</Name>
#       <TextOverlay>Default</TextOverlay>
#       <TextStyle>
#         <FontColor>#FFFFFF00</FontColor>
#         <ShadowColor>#FF000000</ShadowColor>
#         <ShadowDepth>5</ShadowDepth>
#         <TimerBarColor>#FF800000</TimerBarColor>
#       </TextStyle>
#       <TextStyleSource>None</TextStyleSource>
#       <TimerOverlay>Self Buffs</TimerOverlay>
#       <TimerStyle>
#         <FontColor>#FFFFFF00</FontColor>
#         <ShadowColor>#FF000000</ShadowColor>
#         <ShadowDepth>5</ShadowDepth>
#         <TimerBarColor>#FF800000</TimerBarColor>
#       </TimerStyle>
#       <TimerStyleSource>None</TimerStyleSource>
#     </Category>

_category_style = [
    xml.string('FontColor'),
    xml.string('ShadowColor'),
    xml.integer('ShadowDepth'),
    xml.string('TimerBarColor')
]

categories_processor = xml.array(
    xml.dictionary('Category', [
        xml.boolean('IsDefault'),
        xml.string('Name'),
        xml.string('TextOverlay'),
        xml.dictionary('TextStyle', _category_style),
        xml.string('TextStyleSource'),
        xml.string('TimerOverlay'),
        xml.dictionary('TimerStyle', _category_style),
        xml.string('TimerStyleSource')
    ]),
    nested='Categories')

# <Configuration>
#   <Settings/>
#   <BehaviorGroups/>
#   <Categories/>
# </Configuration>

configuration_processor = xml.dictionary('Configuration', [
    settings_processor,
    behavior_groups_processor,
    categories_processor
])

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

behavior_groups = [
    {
        'BackgroundColor': '#00000000',
        'BackgroundFadedColor': '#00000000',
        'BehaviorType': 'Text',
        'EmptyBarColor': '#D0000000',
        'FontName': 'Arial Black',
        'FontSize': 22,
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
                    'Left': 980,
                    'Top': 371,
                    'Right': 1745,
                    'Bottom': 737
                }
            }
        ]
    }
]

categories = [
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
    }
]

configuration = {
    'Settings': settings,
    'BehaviorGroups': behavior_groups,
    'Categories': categories
}

# print(xml.serialize_to_string(settings_processor, settings, indent='    '))
# print(xml.serialize_to_string(behavior_groups_processor, behavior_groups, indent='    '))
print(xml.serialize_to_string(configuration_processor, configuration, indent='    '))

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

settings_processor = xml.dictionary(
    'Settings',
    [
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
        xml.array(xml.dictionary(
            'Transform',
            [
                xml.string('ActualWord'),
                xml.string('PhoneticWord')
            ],
            required=False),
            nested='PhoneticTransforms'),
        xml.integer('ProcessorAffinity'),
        xml.integer('ProfilerRefreshInterval'),
        xml.boolean('PurgeArchivedLogs'),
        xml.string('ReferenceToSelf'),
        xml.string('RepositoryLastViewed'),
        xml.string('ShareServiceUri'),
        xml.array(xml.string(
                'Character',
                required=False),
                nested='ShareWhiteList'),
        xml.boolean('StopSearchingAfterFirstMatch')
    ])

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
    xml.dictionary(
        'Behavior',
        [
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
                xml.dictionary(
                    'WINDOWPLACEMENT',
                    [
                        xml.integer('flags'),
                        xml.integer('length'),
                        xml.dictionary('maxPosition', [
                            xml.integer('X'),
                            xml.integer('Y')
                        ]),
                        xml.dictionary(
                            'minPosition',
                            [
                                xml.integer('X'),
                                xml.integer('Y')
                            ]),
                        xml.dictionary(
                            'normalPosition',
                            [
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
    xml.dictionary('Category',
        [
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

# <TriggerGroups>
#     <TriggerGroup>
#         <Comments></Comments>
#         <EnableByDefault>False</EnableByDefault>
#         <GroupId>3</GroupId>
#         <Name>Class</Name>
#         <SelfCommented>False</SelfCommented>
#         <Triggers>
#             <Trigger>
#                 <Category>Right // HP/AC Buffs</Category>
#                 <ClipboardText></ClipboardText>
#                 <Comments></Comments>
#                 <CopyToClipboard>False</CopyToClipboard>
#                 <CounterResetDuration>0</CounterResetDuration>
#                 <DisplayText></DisplayText>
#                 <EnableRegex>True</EnableRegex>
#                 <InterruptSpeech>False</InterruptSpeech>
#                 <Modified>2017-11-24T12:47:39</Modified>
#                 <Name>Armor of Faith - Other</Name>
#                 <PlayMediaFile>False</PlayMediaFile>
#                 <RestartBasedOnTimerName>True</RestartBasedOnTimerName>
#                 <TextToVoiceText></TextToVoiceText>
#                 <TimerDuration>3780</TimerDuration>
#                 <TimerEarlyEnders>
#                 <EarlyEnder>
#                     <EarlyEndText>^{c} lets go of external concerns\.$</EarlyEndText>
#                     <EnableRegex>True</EnableRegex>
#                 </EarlyEnder>
#                 <EarlyEnder>
#                     <EarlyEndText>^{c} lets go of {s}'s concerns\.$</EarlyEndText>
#                     <EnableRegex>True</EnableRegex>
#                 </EarlyEnder>
#                 </TimerEarlyEnders>
#                 <TimerEndingTime>300</TimerEndingTime>
#                 <TimerEndedTrigger>
#                 <DisplayText>Armor of Faith wore off on {s}</DisplayText>
#                 <InterruptSpeech>False</InterruptSpeech>
#                 <PlayMediaFile>False</PlayMediaFile>
#                 <TextToVoiceText>Armor of Faith wore off on {s}</TextToVoiceText>
#                 <UseText>True</UseText>
#                 <UseTextToVoice>True</UseTextToVoice>
#                 </TimerEndedTrigger>
#                 <TimerEndingTrigger>
#                 <DisplayText>5 min left on Armor of Faith - {s}</DisplayText>
#                 <InterruptSpeech>False</InterruptSpeech>
#                 <PlayMediaFile>False</PlayMediaFile>
#                 <TextToVoiceText>5 min left on Armor of Faith - {s}</TextToVoiceText>
#                 <UseText>True</UseText>
#                 <UseTextToVoice>True</UseTextToVoice>
#                 </TimerEndingTrigger>
#                 <TimerMillisecondDuration>3780000</TimerMillisecondDuration>
#                 <TimerName>Armor of Faith - {s}</TimerName>
#                 <TimerStartBehavior>RestartTimer</TimerStartBehavior>
#                 <TimerType>Timer</TimerType>
#                 <TimerVisibleDuration>0</TimerVisibleDuration>
#                 <TriggerText>^{s} feels the favor of the gods upon them\.$</TriggerText>
#                 <UseCounterResetTimer>False</UseCounterResetTimer>
#                 <UseFastCheck>False</UseFastCheck>
#                 <UseText>False</UseText>
#                 <UseTextToVoice>False</UseTextToVoice>
#                 <UseTimerEnded>True</UseTimerEnded>
#                 <UseTimerEnding>True</UseTimerEnding>
#             </Trigger>
#         </Triggers>
#         <TriggerGroups/>
#     </TriggerGroup>
# <TriggerGroups>

_timer_early_ender = xml.dictionary(
    'EarlyEnder',
    [
        xml.string('EarlyEndText'),
        xml.boolean('EnableRegex')
    ])

_timer_trigger_elements = [
    xml.string('DisplayText'),
    xml.boolean('InterruptSpeech'),
    xml.boolean('PlayMediaFile'),
    xml.string('TextToVoiceText'),
    xml.boolean('UseText'),
    xml.boolean('UseTextToVoice')
]

_trigger = xml.dictionary(
    'Trigger',
    [
        xml.string('Category'),
        xml.string('ClipboardText'),
        xml.string('Comments'),
        xml.boolean('CopyToClipboard'),
        xml.integer('CounterResetDuration'),
        xml.string('DisplayText'),
        xml.boolean('EnableRegex'),
        xml.boolean('InterruptSpeech'),
        xml.string('Modified'),
        xml.string('Name'),
        xml.boolean('PlayMediaFile'),
        xml.boolean('RestartBasedOnTimerName'),
        xml.string('TextToVoiceText'),
        xml.integer('TimerDuration'),
        xml.array(_timer_early_ender, nested='TimerEarlyEnders'),
        xml.integer('TimerEndingTime'),
        xml.dictionary('TimerEndedTrigger', _timer_trigger_elements),
        xml.dictionary('TimerEndingTrigger', _timer_trigger_elements),
        xml.integer('TimerMillisecondDuration'),
        xml.string('TimerName'),
        xml.string('TimerStartBehavior'),
        xml.string('TimerType'),
        xml.integer('TimerVisibleDuration'),
        xml.string('TriggerText'),
        xml.boolean('UseCounterResetTimer'),
        xml.boolean('UseFastCheck'),
        xml.boolean('UseText'),
        xml.boolean('UseTextToVoice'),
        xml.boolean('UseTimerEnded'),
        xml.boolean('UseTimerEnding')
    ],
    required=False)

_trigger_group_common = [
    xml.string('Comments'),
    xml.boolean('EnableByDefault'),
    xml.integer('GroupId'),
    xml.string('Name'),
    xml.string('SelfCommented'),
    xml.array(_trigger,
              nested='Triggers',
              omit_empty=True)
]

_trigger_group_five = xml.dictionary('TriggerGroup', [
    *_trigger_group_common],
    required=False)

_trigger_group_four = xml.dictionary('TriggerGroup', [
    *_trigger_group_common,
    xml.array(_trigger_group_five,
              nested='TriggerGroups',
              omit_empty=True)],
    required=False)

_trigger_group_three = xml.dictionary('TriggerGroup', [
    *_trigger_group_common,
    xml.array(_trigger_group_four,
              nested='TriggerGroups',
              omit_empty=True)],
    required=False)

_trigger_group_two = xml.dictionary('TriggerGroup', [
    *_trigger_group_common,
    xml.array(_trigger_group_three,
              nested='TriggerGroups',
              omit_empty=True)],
    required=False)

_trigger_group_one = xml.dictionary('TriggerGroup', [
    *_trigger_group_common,
    xml.array(_trigger_group_two,
              nested='TriggerGroups',
              omit_empty=True)],
    required=False)

_trigger_group_zero = xml.dictionary('TriggerGroup', [
    *_trigger_group_common,
    xml.array(_trigger_group_one,
              nested='TriggerGroups',
              omit_empty=True)
])

trigger_groups_processor = xml.array(_trigger_group_zero,
                                     nested='TriggerGroups')

# <Characters>
#     <Character>
#         <AutoMonitor>True</AutoMonitor>
#         <DisplayName>Freckie (project)</DisplayName>
#         <LastArchiveDate>0001-01-01T00:00:00</LastArchiveDate>
#         <LogFilePath>D:\GAMES\EverQuest\Logs\eqlog_Freckie_project1999.txt</LogFilePath>
#         <Name>Freckie</Name>
#         <TextStyle>
#             <FontColor>#FFFFFF00</FontColor>
#             <ShadowColor>#FF000000</ShadowColor>
#             <ShadowDepth>5</ShadowDepth>
#             <TimerBarColor>#FF800000</TimerBarColor>
#         </TextStyle>
#         <TimerStyle>
#             <FontColor>#FFFFFF00</FontColor>
#             <ShadowColor>#FF000000</ShadowColor>
#             <ShadowDepth>5</ShadowDepth>
#             <TimerBarColor>#FF800000</TimerBarColor>
#         </TimerStyle>
#         <TriggerGroups>
#             <TriggerGroup GroupId="5" />
#         </TriggerGroups>
#         <VoiceName>Microsoft Zira Desktop</VoiceName>
#         <VoiceSpeed>0</VoiceSpeed>
#         <Volume>48</Volume>
#     </Character>
# </Characters>

_character_style_options = [
    xml.string('FontColor'),
    xml.string('ShadowColor'),
    xml.integer('ShadowDepth'),
    xml.string('TimerBarColor')
]

characters_processor = xml.array(
    xml.dictionary(
        'Character',
        [
            xml.boolean('AutoMonitor'),
            xml.string('DisplayName'),
            xml.string('LastArchiveDate'),
            xml.string('LogFilePath'),
            xml.string('Name'),
            xml.dictionary('TextStyle', _character_style_options),
            xml.dictionary('TimerStyle', _character_style_options),
            xml.array(
                xml.integer('TriggerGroup', attribute='GroupId'),
                nested='TriggerGroups'),
            xml.string('VoiceName'),
            xml.integer('VoiceSpeed'),
            xml.integer('Volume')
        ],
        required=False),
    nested='Characters'
)

# <Configuration>
#   <Settings/>
#   <BehaviorGroups/>
#   <Categories/>
#   <TriggerGroups/>
#   <Characters/>
# </Configuration>

configuration_processor = xml.dictionary(
    'Configuration',
    [
        settings_processor,
        behavior_groups_processor,
        categories_processor,
        # trigger_groups_processor,
        # characters_processor
    ])


def export_to_string(gina_config) -> str:
    return xml.serialize_to_string(
        configuration_processor,
        gina_config,
        indent='  ')


def export_to_file(gina_config, file_path) -> None:
    return xml.serialize_to_file(
        configuration_processor,
        gina_config,
        xml_file_path=file_path,
        indent='  ')

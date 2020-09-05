
triggers = []


# public api
# ============================================================================

def create_trigger(name) -> dict:
    return {
        'Category': None,
        'ClipboardText': '',
        'Comments': '',
        'CopyToClipboard': False,
        'CounterResetDuration': 0,
        'DisplayText': '',
        'EnableRegex': True,
        'InterruptSpeech': False,
        'Modified': '2017-11-24T12:47:39',
        'Name': name,
        'PlayMediaFile': False,
        'RestartBasedOnTimerName': True,
        'TextToVoiceText': '',
        'TimerDuration': 3780,
        'TimerEarlyEnders': [
            {
                'EarlyEndText': '^{c} lets go of external concerns\.$',
                'EnableRegex': True
            },
            {
                'EarlyEndText': '^{c} lets go of {s}\'s concerns\.$',
                'EnableRegex': True
            }
        ],
        'TimerEndingTime': 300,
        'TimerEndedTrigger': {
            'DisplayText': 'Armor of Faith wore off on {s}',
            'InterruptSpeech': False,
            'PlayMediaFile': False,
            'TextToVoiceText': 'Armor of Faith wore off on {s}',
            'UseText': True,
            'UseTextToVoice': True
        },
        'TimerEndingTrigger': {
            'DisplayText': '5 min left on Armor of Faith - {s}',
            'InterruptSpeech': False,
            'PlayMediaFile': False,
            'TextToVoiceText': '5 min left on Armor of Faith - {s}',
            'UseText': True,
            'UseTextToVoice': True
        },
        'TimerMillisecondDuration': 3780000,
        'TimerName': 'Armor of Faith - {s}',
        'TimerStartBehavior': 'RestartTimer',
        'TimerType': 'Timer',
        'TimerVisibleDuration': 0,
        'TriggerText': '^{s} feels the favor of the gods upon them\.$',
        'UseCounterResetTimer': False,
        'UseFastCheck': False,
        'UseText': False,
        'UseTextToVoice': False,
        'UseTimerEnded': True,
        'UseTimerEnding': True
    }


def add_trigger(trigger) -> None:
    triggers.append(trigger)

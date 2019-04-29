# local
from gina_config.fonts import \
    OVERLAY_FONT_NAME
from gina_config.colors import ColorPalette

# text overlays
CRITICAL_ALERTS_TEXT_OVERLAY = 'Critical Alerts'
DEFAULT_TEXT_OVERLAY = 'Default'
# timer overlays
DEBUFFS_TIMER_OVERLAY = 'Debuffs'
OTHER_BUFFS_TIMER_OVERLAY = 'Other Buffs'
SELF_BUFFS_TIMER_OVERLAY = 'Self Buffs'
SHORT_DURATION_BUFFS_TIMER_OVERLAY = 'Short Duration Buffs'
SHORT_DURATION_DEBUFFS_TIMER_OVERLAY = 'Short Duration Debuffs'

text_overlays = []
timer_overlays = []


def _create_overlay(name, **kwargs):
    new_overlay = {
        'BackgroundColor': ColorPalette.FULLY_TRANSPARENT,
        'BackgroundFadedColor': ColorPalette.FULLY_TRANSPARENT,
        'BehaviorType': 'Text',
        'EmptyBarColor': ColorPalette.TRANSPARENT_BLACK,
        'FontName': OVERLAY_FONT_NAME,
        'FontSize': None,  # 30
        'GroupByCharacter': False,
        'Name': name,
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
    new_overlay.update(**kwargs)
    return new_overlay


def create_text_overlay(name, **kwargs):
    new_overlay = _create_overlay(
        name,
        BehaviorType='Text',
        SortMethod='OrderTriggered')
    new_overlay.update(**kwargs)
    text_overlays.append(new_overlay)


def create_timer_overlay(name, **kwargs):
    new_overlay = _create_overlay(
        name,
        BehaviorType='Timer',
        SortMethod='TimeRemaining')
    new_overlay.update(**kwargs)
    timer_overlays.append(new_overlay)


def _get_overlay(name, overlays) -> dict:
    return next(overlay
                for overlay
                in overlays
                if overlay['Name'] == name)


def get_text_overlay(name) -> dict:
    return _get_overlay(name, text_overlays)


def get_timer_overlay(name) -> dict:
    return _get_overlay(name, timer_overlays)


def set_overlay_font_size(font_size, overlay):
    overlay['FontSize'] = font_size


def set_overlay_bottom_position(position, overlay):
    overlay['WindowLayout'][0]['normalPosition']['Bottom'] = position


def set_overlay_left_position(position, overlay):
    overlay['WindowLayout'][0]['normalPosition']['Left'] = position


def set_overlay_right_position(position, overlay):
    overlay['WindowLayout'][0]['normalPosition']['Right'] = position


def set_overlay_top_position(position, overlay):
    overlay['WindowLayout'][0]['normalPosition']['Top'] = position


# text overlays
create_text_overlay(CRITICAL_ALERTS_TEXT_OVERLAY)
create_text_overlay(
    DEFAULT_TEXT_OVERLAY,
    GroupByCharacter=True)

# timer overlays
create_timer_overlay(DEBUFFS_TIMER_OVERLAY)
create_timer_overlay(OTHER_BUFFS_TIMER_OVERLAY)
create_timer_overlay(SELF_BUFFS_TIMER_OVERLAY)
create_timer_overlay(
    SHORT_DURATION_BUFFS_TIMER_OVERLAY,
    SortMethod='OrderTriggered')
create_timer_overlay(
    SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
    SortMethod='OrderTriggered')

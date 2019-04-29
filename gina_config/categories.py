# local
from gina_config.overlays import \
    CRITICAL_ALERTS_TEXT_OVERLAY, \
    DEFAULT_TEXT_OVERLAY, \
    DEBUFFS_TIMER_OVERLAY, \
    OTHER_BUFFS_TIMER_OVERLAY, \
    SELF_BUFFS_TIMER_OVERLAY, \
    SHORT_DURATION_BUFFS_TIMER_OVERLAY, \
    SHORT_DURATION_DEBUFFS_TIMER_OVERLAY
from gina_config.colors import \
    ColorPalette, \
    CRITICAL_ALERT_COLOR, \
    DEFAULT_ALERT_COLOR, \
    ABSORB_EFFECT_COLOR, \
    CHARM_EFFECT_COLOR, \
    DAMAGE_SHIELD_EFFECT_COLOR, \
    DETRIMENTAL_EFFECT_COLOR, \
    DOT_EFFECT_COLOR, \
    HASTE_EFFECT_COLOR, \
    HC_AC_EFFECT_COLOR, \
    HEAL_EFFECT_COLOR, \
    ILLUSION_EFFECT_COLOR, \
    LULL_EFFECT_COLOR, \
    MANA_EFFECT_COLOR, \
    MEZ_EFFECT_COLOR, \
    MOVEMENT_SPEED_EFFECT_COLOR, \
    REGEN_EFFECT_COLOR, \
    RESIST_EFFECT_COLOR, \
    ROOT_EFFECT_COLOR, \
    SLOW_EFFECT_COLOR, \
    SNARE_EFFECT_COLOR, \
    STAT_EFFECT_COLOR, \
    VISION_EFFECT_COLOR, \
    EFFECT_WORN_OFF_COLOR


# basic alerts
CRITICAL_ALERTS_CATEGORY = 'Critical Alerts'
DEFAULT_ALERTS_CATEGORY = 'Default'

# color alerts
AQUA_ALERTS_CATEGORY = 'Highlighted Default (Aqua)'
GREEN_ALERTS_CATEGORY = 'Highlighted Default (Bright Green)'
ORANGE_ALERTS_CATEGORY = 'Highlighted Default (Bright Orange)'
RED_ALERTS_CATEGORY = 'Highlighted Default (Bright Red)'

# effect alerts
ABSORB_ALERTS_CATEGORY = 'Highlighted Default (Absorb)'
DEBUFF_ALERTS_CATEGORY = 'Highlighted Default (Debuff)'
DS_ALERTS_CATEGORY = 'Highlighted Default (DS)'
HEAL_ALERTS_CATEGORY = 'Highlighted Default (Heal)'
MEZ_ALERTS_CATEGORY = 'Highlighted Default (Mez)'
ROOT_ALERTS_CATEGORY = 'Highlighted Default (Root)'
SLOW_ALERTS_CATEGORY = 'Highlighted Default (Slow)'
SNARE_ALERTS_CATEGORY = 'Highlighted Default (Snare)'

# effects
CHARM_EFFECT_CATEGORY = 'Left // Charm Effect'
DETRIMENTAL_EFFECT_CATEGORY = 'Left // Detrimental Effect'
DOT_EFFECT_CATEGORY = 'Left // DoT Effect'
LULL_EFFECT_CATEGORY = 'Left // Lull Effect'
MEZ_EFFECT_CATEGORY = 'Left // Mez Effect'
ROOT_EFFECT_CATEGORY = 'Left // Root Effect'
SLOW_EFFECT_CATEGORY = 'Left // Slow Effect'
SNARE_EFFECT_CATEGORY = 'Left // Snare Effect'

# buffs
ABSORB_BUFFS_CATEGORY = 'Right // Absorb Buffs'
DS_BUFFS_CATEGORY = 'Right // DS Buffs'
HASTE_BUFFS_CATEGORY = 'Right // Haste Buffs'
HP_AC_BUFFS_CATEGORY = 'Right // HP/AC Buffs'
ILLUSION_BUFFS_CATEGORY = 'Right // Illusion Buffs'
MANA_BUFFS_CATEGORY = 'Right // Mana Buffs'
REGEN_BUFFS_CATEGORY = 'Right // Regen Buffs'
RESIST_BUFFS_CATEGORY = 'Right // Resist Buffs'
STAT_BUFFS_CATEGORY = 'Right // Stat Buffs'
TRAVEL_BUFFS_CATEGORY = 'Right // Travel Buffs'
VISION_BUFFS_CATEGORY = 'Right // Vision Buffs'

# self buffs
SELF_ABSORB_BUFFS_CATEGORY = 'Right // Self Absorb Buffs'
SELF_DS_BUFFS_CATEGORY = 'Right // Self DS Buffs'
SELF_HASTE_BUFFS_CATEGORY = 'Right // Self Haste Buffs'
SELF_HP_AC_BUFFS_CATEGORY = 'Right // Self HP/AC Buffs'
SELF_ILLUSION_BUFFS_CATEGORY = 'Right // Self Illusion Buffs'
SELF_MANA_BUFFS_CATEGORY = 'Right // Self Mana Buffs'
SELF_REGEN_BUFFS_CATEGORY = 'Right // Self Regen Buffs'
SELF_RESIST_BUFFS_CATEGORY = 'Right // Self Resist Buffs'
SELF_STAT_BUFFS_CATEGORY = 'Right // Self Stat Buffs'
SELF_TRAVEL_BUFFS_CATEGORY = 'Right // Self Travel Buffs'
SELF_VISION_BUFFS_CATEGORY = 'Right // Self Vision Buffs'
SELF_WORN_OFF_BUFFS_CATEGORY = 'Right // Self Worn Off Buffs'

# short duration effects
SHORT_DURATION_CHARM_CATEGORY = 'Middle // Short Duration Charm'
SHORT_DURATION_DEBUFFS_CATEGORY = 'Middle // Short Duration Debuffs'
SHORT_DURATION_DOT_AOE_CATEGORY = 'Middle // Short Duration DoT AoE'
SHORT_DURATION_LULL_CATEGORY = 'Middle // Short Duration Lull'
SHORT_DURATION_MEZ_CATEGORY = 'Middle // Short Duration Mez'
SHORT_DURATION_SLOW_CATEGORY = 'Middle // Short Duration Slow'
SHORT_DURATION_SNARE_CATEGORY = 'Middle // Short Duration Snare'

# short duration buffs
SHORT_DURATION_HASTE_BUFFS_CATEGORY = 'Middle // Short Duration Haste Buffs'
SHORT_DURATION_MANA_BUFFS_CATEGORY = 'Middle // Short Duration Mana Buffs'
SHORT_DURATION_REGEN_BUFFS_CATEGORY = 'Middle // Short Duration Regen Buffs'
SHORT_DURATION_RESIST_BUFFS_CATEGORY = 'Middle // Short Duration Resist Buffs'
SHORT_DURATION_STAT_BUFFS_CATEGORY = 'Middle // Short Duration Stat Buffs'
SHORT_DURATION_TRAVEL_BUFFS_CATEGORY = 'Middle // Short Duration Travel Buffs'


categories = []


def create_category(
        name,
        is_default=False,
        text_overlay=CRITICAL_ALERTS_TEXT_OVERLAY,
        text_font_color=DEFAULT_ALERT_COLOR,
        text_timer_bar_color=ColorPalette.DARK_RED,
        timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
        timer_font_color=DEFAULT_ALERT_COLOR,
        timer_timer_bar_color=ColorPalette.DARK_RED):
    new_category = {
        'IsDefault': is_default,
        'Name': name,
        'TextOverlay': text_overlay,
        'TextStyle': {
            'FontColor': text_font_color,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': text_timer_bar_color
        },
        'TextStyleSource': 'None',
        'TimerOverlay': timer_overlay,
        'TimerStyle': {
            'FontColor': timer_font_color,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': timer_timer_bar_color
        },
        'TimerStyleSource': 'None'
    }
    categories.append(new_category)


# Default
create_category(
    DEFAULT_ALERTS_CATEGORY,
    is_default=True,
    text_overlay=DEFAULT_TEXT_OVERLAY)
# Critical Alerts
create_category(
    CRITICAL_ALERTS_CATEGORY,
    text_font_color=CRITICAL_ALERT_COLOR,
    timer_font_color=CRITICAL_ALERT_COLOR)
# Left // Detrimental Effect
create_category(
    DETRIMENTAL_EFFECT_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_RED,
    timer_overlay=DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=DETRIMENTAL_EFFECT_COLOR)
# Right // Self Worn Off Buffs
create_category(
    SELF_WORN_OFF_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_timer_bar_color=EFFECT_WORN_OFF_COLOR)
# Middle // Short Duration Mana Buffs
create_category(
    SHORT_DURATION_MANA_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=MANA_EFFECT_COLOR)
# Middle // Short Duration Debuffs
create_category(
    SHORT_DURATION_DEBUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=DETRIMENTAL_EFFECT_COLOR)
# Middle // Short Duration Travel Buffs
create_category(
    SHORT_DURATION_TRAVEL_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=MOVEMENT_SPEED_EFFECT_COLOR)
# Middle // Short Duration Regen Buffs
create_category(
    SHORT_DURATION_REGEN_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=REGEN_EFFECT_COLOR)
# Middle // Short Duration Haste Buffs
create_category(
    SHORT_DURATION_HASTE_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=HASTE_EFFECT_COLOR)
# Middle // Short Duration Slow
create_category(
    SHORT_DURATION_SLOW_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.LIGHT_GREY,
    timer_timer_bar_color=SLOW_EFFECT_COLOR)
# Middle // Short Duration Snare
create_category(
    SHORT_DURATION_SNARE_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.LIGHT_GREY,
    timer_timer_bar_color=SNARE_EFFECT_COLOR)
# Middle // Short Duration Charm
create_category(
    SHORT_DURATION_CHARM_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=CHARM_EFFECT_COLOR)
# Middle // Short Duration DoT AoE
create_category(
    SHORT_DURATION_DOT_AOE_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=DOT_EFFECT_COLOR)
# Middle // Short Duration Resist Buffs
create_category(
    SHORT_DURATION_RESIST_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=RESIST_EFFECT_COLOR)
# Middle // Short Duration Stat Buffs
create_category(
    SHORT_DURATION_STAT_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=STAT_EFFECT_COLOR)
# Left // Charm Effect
create_category(
    CHARM_EFFECT_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_RED,
    timer_overlay=DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=CHARM_EFFECT_COLOR)
# Left // Mez Effect
create_category(
    MEZ_EFFECT_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_RED,
    timer_overlay=DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=MEZ_EFFECT_COLOR)
# Right // Self Haste Buffs
create_category(
    SELF_HASTE_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=HASTE_EFFECT_COLOR)
# Right // Self Mana Buffs
create_category(
    SELF_MANA_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=MANA_EFFECT_COLOR)
# Right // Haste Buffs
create_category(
    HASTE_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=OTHER_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=HASTE_EFFECT_COLOR)
# Right // Self Regen Buffs
create_category(
    SELF_REGEN_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=REGEN_EFFECT_COLOR)
# Right // Regen Buffs
create_category(
    REGEN_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=OTHER_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=REGEN_EFFECT_COLOR)
# Right // Self Stat Buffs
create_category(
    SELF_STAT_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=STAT_EFFECT_COLOR)
# Right // Self HP/AC Buffs
create_category(
    SELF_HP_AC_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=HC_AC_EFFECT_COLOR)
# Right // Self Resist Buffs
create_category(
    SELF_RESIST_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=RESIST_EFFECT_COLOR)
# Right // Self Travel Buffs
create_category(
    SELF_TRAVEL_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=MOVEMENT_SPEED_EFFECT_COLOR)
# Right // Self Vision Buffs
create_category(
    SELF_VISION_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=VISION_EFFECT_COLOR)
# Right // Self Illusion Buffs
create_category(
    SELF_ILLUSION_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=ILLUSION_EFFECT_COLOR)
# Right // HP/AC Buffs
create_category(
    HP_AC_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=OTHER_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=HC_AC_EFFECT_COLOR)
# Right // Illusion Buffs
create_category(
    ILLUSION_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=OTHER_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=ILLUSION_EFFECT_COLOR)
# Right // Mana Buffs
create_category(
    MANA_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=OTHER_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=MANA_EFFECT_COLOR)
# Right // Resist Buffs
create_category(
    RESIST_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=OTHER_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=RESIST_EFFECT_COLOR)
# Right // Stat Buffs
create_category(
    STAT_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=OTHER_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=STAT_EFFECT_COLOR)
# Right // Travel Buffs
create_category(
    TRAVEL_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=OTHER_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=MOVEMENT_SPEED_EFFECT_COLOR)
# Right // Vision Buffs
create_category(
    VISION_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=OTHER_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=VISION_EFFECT_COLOR)
# Middle // Short Duration Mez
create_category(
    SHORT_DURATION_MEZ_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=MEZ_EFFECT_COLOR)
# Right // Self DS Buffs
create_category(
    SELF_DS_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=DAMAGE_SHIELD_EFFECT_COLOR)
# Right // Self Absorb Buffs
create_category(
    SELF_ABSORB_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SELF_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=ABSORB_EFFECT_COLOR)
# Right // DS Buffs
create_category(
    DS_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=OTHER_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=DAMAGE_SHIELD_EFFECT_COLOR)
# Right // Absorb Buffs
create_category(
    ABSORB_BUFFS_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=OTHER_BUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=ABSORB_EFFECT_COLOR)
# Left // DoT Effect
create_category(
    DOT_EFFECT_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_RED,
    timer_overlay=DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=DOT_EFFECT_COLOR)
# Left // Slow Effect
create_category(
    SLOW_EFFECT_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_RED,
    timer_overlay=DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=SLOW_EFFECT_COLOR)
# Left // Snare Effect
create_category(
    SNARE_EFFECT_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_RED,
    timer_overlay=DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=SNARE_EFFECT_COLOR)
# Left // Root Effect
create_category(
    ROOT_EFFECT_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_RED,
    timer_overlay=DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=ROOT_EFFECT_COLOR)
# Left // Lull Effect
create_category(
    LULL_EFFECT_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_RED,
    timer_overlay=DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=LULL_EFFECT_COLOR)
# Middle // Short Duration Lull
create_category(
    SHORT_DURATION_LULL_CATEGORY,
    text_font_color=ColorPalette.BRIGHT_YELLOW,
    timer_overlay=SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
    timer_font_color=ColorPalette.WHITE,
    timer_timer_bar_color=LULL_EFFECT_COLOR)



    # # Highlighted Default (Bright Green)
    # {
    #     'IsDefault': False,
    #     'Name': GREEN_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': '#FF21FF00',
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Bright Orange)
    # {
    #     'IsDefault': False,
    #     'Name': ORANGE_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': '#FFFFA500',
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Bright Red)
    # {
    #     'IsDefault': False,
    #     'Name': RED_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': ColorPalette.BRIGHT_RED,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Aqua)
    # {
    #     'IsDefault': False,
    #     'Name': AQUA_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': ColorPalette.DARK_AQUA,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Root)
    # {
    #     'IsDefault': False,
    #     'Name': ROOT_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': ROOT_EFFECT_COLOR,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (DS)
    # {
    #     'IsDefault': False,
    #     'Name': DS_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': DAMAGE_SHIELD_EFFECT_COLOR,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Absorb)
    # {
    #     'IsDefault': False,
    #     'Name': ABSORB_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': ABSORB_EFFECT_COLOR,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Mez)
    # {
    #     'IsDefault': False,
    #     'Name': MEZ_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': MEZ_EFFECT_COLOR,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Heal)
    # {
    #     'IsDefault': False,
    #     'Name': HEAL_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': HEAL_EFFECT_COLOR,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Slow)
    # {
    #     'IsDefault': False,
    #     'Name': SLOW_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': SLOW_EFFECT_COLOR,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Snare)
    # {
    #     'IsDefault': False,
    #     'Name': SNARE_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': SNARE_EFFECT_COLOR,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # },
    # # Highlighted Default (Debuff)
    # {
    #     'IsDefault': False,
    #     'Name': DEBUFF_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_TEXT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': DETRIMENTAL_EFFECT_COLOR,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
    #     'TimerStyle': {
    #         'FontColor': ColorPalette.BRIGHT_YELLOW,
    #         'ShadowColor': ColorPalette.BLACK,
    #         'ShadowDepth': 5,
    #         'TimerBarColor': ColorPalette.DARK_RED
    #     },
    #     'TimerStyleSource': 'None'
    # }

old_categories = [
    # Default
    {
        'IsDefault': True,
        'Name': DEFAULT_ALERTS_CATEGORY,
        'TextOverlay': DEFAULT_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': DEFAULT_ALERT_COLOR,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': DEFAULT_ALERT_COLOR,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TimerStyleSource': 'None'
    },
    # Critical Alerts
    {
        'IsDefault': False,
        'Name': CRITICAL_ALERTS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': CRITICAL_ALERT_COLOR,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': CRITICAL_ALERT_COLOR,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TimerStyleSource': 'None'
    },
    # Left // Detrimental Effect
    {
        'IsDefault': False,
        'Name': DETRIMENTAL_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_RED,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': DETRIMENTAL_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Worn Off Buffs
    {
        'IsDefault': False,
        'Name': SELF_WORN_OFF_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': EFFECT_WORN_OFF_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Mana Buffs
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_MANA_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': MANA_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Debuffs
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_DEBUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': DETRIMENTAL_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Travel Buffs
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_TRAVEL_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': MOVEMENT_SPEED_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Regen Buffs
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_REGEN_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': REGEN_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Haste Buffs
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_HASTE_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': HASTE_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Slow
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_SLOW_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.LIGHT_GREY,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': SLOW_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Snare
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_SNARE_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.LIGHT_GREY,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': SNARE_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Charm
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_CHARM_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': CHARM_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration DoT AoE
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_DOT_AOE_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': DOT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Resist Buffs
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_RESIST_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': RESIST_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Stat Buffs
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_STAT_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': STAT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Charm Effect
    {
        'IsDefault': False,
        'Name': CHARM_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_RED,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': CHARM_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Mez Effect
    {
        'IsDefault': False,
        'Name': MEZ_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_RED,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': MEZ_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Haste Buffs
    {
        'IsDefault': False,
        'Name': SELF_HASTE_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': HASTE_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Mana Buffs
    {
        'IsDefault': False,
        'Name': SELF_MANA_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': MANA_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Haste Buffs
    {
        'IsDefault': False,
        'Name': HASTE_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': HASTE_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Regen Buffs
    {
        'IsDefault': False,
        'Name': SELF_REGEN_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': REGEN_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Regen Buffs
    {
        'IsDefault': False,
        'Name': REGEN_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': REGEN_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Stat Buffs
    {
        'IsDefault': False,
        'Name': SELF_STAT_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': STAT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self HP/AC Buffs
    {
        'IsDefault': False,
        'Name': SELF_HP_AC_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': HC_AC_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Resist Buffs
    {
        'IsDefault': False,
        'Name': SELF_RESIST_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': RESIST_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Travel Buffs
    {
        'IsDefault': False,
        'Name': SELF_TRAVEL_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': MOVEMENT_SPEED_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Vision Buffs
    {
        'IsDefault': False,
        'Name': SELF_VISION_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': VISION_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Illusion Buffs
    {
        'IsDefault': False,
        'Name': SELF_ILLUSION_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ILLUSION_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // HP/AC Buffs
    {
        'IsDefault': False,
        'Name': HP_AC_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': HC_AC_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Illusion Buffs
    {
        'IsDefault': False,
        'Name': ILLUSION_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ILLUSION_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Mana Buffs
    {
        'IsDefault': False,
        'Name': MANA_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': MANA_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Resist Buffs
    {
        'IsDefault': False,
        'Name': RESIST_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': RESIST_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Stat Buffs
    {
        'IsDefault': False,
        'Name': STAT_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': STAT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Travel Buffs
    {
        'IsDefault': False,
        'Name': TRAVEL_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': MOVEMENT_SPEED_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Vision Buffs
    {
        'IsDefault': False,
        'Name': VISION_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': VISION_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Mez
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_MEZ_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': MEZ_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self DS Buffs
    {
        'IsDefault': False,
        'Name': SELF_DS_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': DAMAGE_SHIELD_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Self Absorb Buffs
    {
        'IsDefault': False,
        'Name': SELF_ABSORB_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ABSORB_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // DS Buffs
    {
        'IsDefault': False,
        'Name': DS_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': DAMAGE_SHIELD_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Right // Absorb Buffs
    {
        'IsDefault': False,
        'Name': ABSORB_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ABSORB_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // DoT Effect
    {
        'IsDefault': False,
        'Name': DOT_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_RED,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': DOT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Slow Effect
    {
        'IsDefault': False,
        'Name': SLOW_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_RED,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': SLOW_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Snare Effect
    {
        'IsDefault': False,
        'Name': SNARE_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_RED,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': SNARE_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Root Effect
    {
        'IsDefault': False,
        'Name': ROOT_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_RED,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ROOT_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Left // Lull Effect
    {
        'IsDefault': False,
        'Name': LULL_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_RED,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': LULL_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    },
    # Middle // Short Duration Lull
    {
        'IsDefault': False,
        'Name': SHORT_DURATION_LULL_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_TEXT_OVERLAY,
        'TextStyle': {
            'FontColor': ColorPalette.BRIGHT_YELLOW,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': ColorPalette.DARK_RED
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_TIMER_OVERLAY,
        'TimerStyle': {
            'FontColor': ColorPalette.WHITE,
            'ShadowColor': ColorPalette.BLACK,
            'ShadowDepth': 5,
            'TimerBarColor': LULL_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    }
]

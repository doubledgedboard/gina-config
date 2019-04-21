# local
from names.categories import \
    CRITICAL_ALERTS_CATEGORY, \
    DEFAULT_ALERTS_CATEGORY, \
    AQUA_ALERTS_CATEGORY, \
    GREEN_ALERTS_CATEGORY, \
    ORANGE_ALERTS_CATEGORY, \
    RED_ALERTS_CATEGORY, \
    ABSORB_ALERTS_CATEGORY, \
    DEBUFF_ALERTS_CATEGORY, \
    DS_ALERTS_CATEGORY, \
    HEAL_ALERTS_CATEGORY, \
    MEZ_ALERTS_CATEGORY, \
    ROOT_ALERTS_CATEGORY, \
    SLOW_ALERTS_CATEGORY, \
    SNARE_ALERTS_CATEGORY, \
    CHARM_EFFECT_CATEGORY, \
    DETRIMENTAL_EFFECT_CATEGORY, \
    DOT_EFFECT_CATEGORY, \
    LULL_EFFECT_CATEGORY, \
    MEZ_EFFECT_CATEGORY, \
    ROOT_EFFECT_CATEGORY, \
    SLOW_EFFECT_CATEGORY, \
    SNARE_EFFECT_CATEGORY, \
    ABSORB_BUFFS_CATEGORY, \
    DS_BUFFS_CATEGORY, \
    HASTE_BUFFS_CATEGORY, \
    HP_AC_BUFFS_CATEGORY, \
    ILLUSION_BUFFS_CATEGORY, \
    MANA_BUFFS_CATEGORY, \
    REGEN_BUFFS_CATEGORY, \
    RESIST_BUFFS_CATEGORY, \
    STAT_BUFFS_CATEGORY, \
    TRAVEL_BUFFS_CATEGORY, \
    VISION_BUFFS_CATEGORY, \
    SELF_ABSORB_BUFFS_CATEGORY, \
    SELF_DS_BUFFS_CATEGORY, \
    SELF_HASTE_BUFFS_CATEGORY, \
    SELF_HP_AC_BUFFS_CATEGORY, \
    SELF_ILLUSION_BUFFS_CATEGORY, \
    SELF_MANA_BUFFS_CATEGORY, \
    SELF_REGEN_BUFFS_CATEGORY, \
    SELF_RESIST_BUFFS_CATEGORY, \
    SELF_STAT_BUFFS_CATEGORY, \
    SELF_TRAVEL_BUFFS_CATEGORY, \
    SELF_VISION_BUFFS_CATEGORY, \
    SELF_WORN_OFF_BUFFS_CATEGORY, \
    SHORT_DURATION_CHARM_CATEGORY, \
    SHORT_DURATION_DEBUFFS_CATEGORY, \
    SHORT_DURATION_DOT_AOE_CATEGORY, \
    SHORT_DURATION_LULL_CATEGORY, \
    SHORT_DURATION_MEZ_CATEGORY, \
    SHORT_DURATION_SLOW_CATEGORY, \
    SHORT_DURATION_SNARE_CATEGORY, \
    SHORT_DURATION_HASTE_BUFFS_CATEGORY, \
    SHORT_DURATION_MANA_BUFFS_CATEGORY, \
    SHORT_DURATION_REGEN_BUFFS_CATEGORY, \
    SHORT_DURATION_RESIST_BUFFS_CATEGORY, \
    SHORT_DURATION_STAT_BUFFS_CATEGORY, \
    SHORT_DURATION_TRAVEL_BUFFS_CATEGORY
from names.overlays import \
    CRITICAL_ALERTS_OVERLAY, \
    DEBUFFS_OVERLAY, \
    DEFAULT_OVERLAY, \
    OTHER_BUFFS_OVERLAY, \
    SELF_BUFFS_OVERLAY, \
    SHORT_DURATION_BUFFS_OVERLAY, \
    SHORT_DURATION_DEBUFFS_OVERLAY
from colors import \
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


categories = [
    # Default
    {
        'IsDefault': True,
        'Name': DEFAULT_ALERTS_CATEGORY,
        'TextOverlay': DEFAULT_OVERLAY,
        'TextStyle': {
            'FontColor': DEFAULT_ALERT_COLOR,
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': CRITICAL_ALERTS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': CRITICAL_ALERT_COLOR,
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
        'TimerStyle': {
            'FontColor': CRITICAL_ALERT_COLOR,
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TimerStyleSource': 'None'
    },
    # Left // Detrimental Effect
    {
        'IsDefault': False,
        'Name': DETRIMENTAL_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_OVERLAY,
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
        'Name': SELF_WORN_OFF_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_MANA_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_DEBUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_TRAVEL_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_REGEN_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_HASTE_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_SLOW_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_SNARE_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_CHARM_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_DOT_AOE_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_RESIST_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_STAT_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_BUFFS_OVERLAY,
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
        'Name': CHARM_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_OVERLAY,
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
        'Name': MEZ_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_OVERLAY,
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
        'Name': SELF_HASTE_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': SELF_MANA_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': HASTE_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_OVERLAY,
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
        'Name': SELF_REGEN_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': REGEN_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_OVERLAY,
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
        'Name': SELF_STAT_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': SELF_HP_AC_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': SELF_RESIST_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': SELF_TRAVEL_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': SELF_VISION_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': SELF_ILLUSION_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': HP_AC_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_OVERLAY,
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
        'Name': ILLUSION_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_OVERLAY,
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
        'Name': MANA_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_OVERLAY,
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
        'Name': RESIST_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_OVERLAY,
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
        'Name': STAT_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_OVERLAY,
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
        'Name': TRAVEL_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_OVERLAY,
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
        'Name': VISION_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_MEZ_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_OVERLAY,
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
        'Name': SELF_DS_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': SELF_ABSORB_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': DS_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_OVERLAY,
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
        'Name': ABSORB_BUFFS_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': OTHER_BUFFS_OVERLAY,
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
        'Name': DOT_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_OVERLAY,
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
        'Name': SLOW_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_OVERLAY,
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
        'Name': SNARE_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_OVERLAY,
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
        'Name': ROOT_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_OVERLAY,
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
        'Name': LULL_EFFECT_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFF0000',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': DEBUFFS_OVERLAY,
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
    #     'Name': GREEN_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': '#FF21FF00',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
    #     'Name': ORANGE_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': '#FFFFA500',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
    #     'Name': RED_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': '#FFFF0000',
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
    #     'Name': AQUA_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': ColorPalette.DARK_AQUA,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
    #     'Name': ROOT_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': ROOT_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
    #     'Name': DS_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': DAMAGE_SHIELD_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
    #     'Name': ABSORB_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': ABSORB_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
    #     'Name': MEZ_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': MEZ_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
    #     'Name': HEAL_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': HEAL_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
    #     'Name': SLOW_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': SLOW_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
    #     'Name': SNARE_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': SNARE_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
    #     'Name': DEBUFF_ALERTS_CATEGORY,
    #     'TextOverlay': DEFAULT_OVERLAY,
    #     'TextStyle': {
    #         'FontColor': DETRIMENTAL_EFFECT_COLOR,
    #         'ShadowColor': '#FF000000',
    #         'ShadowDepth': 5,
    #         'TimerBarColor': '#FF800000'
    #     },
    #     'TextStyleSource': 'None',
    #     'TimerOverlay': SELF_BUFFS_OVERLAY,
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
        'Name': SHORT_DURATION_LULL_CATEGORY,
        'TextOverlay': CRITICAL_ALERTS_OVERLAY,
        'TextStyle': {
            'FontColor': '#FFFFFF00',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': '#FF800000'
        },
        'TextStyleSource': 'None',
        'TimerOverlay': SHORT_DURATION_DEBUFFS_OVERLAY,
        'TimerStyle': {
            'FontColor': '#FFFFFFFF',
            'ShadowColor': '#FF000000',
            'ShadowDepth': 5,
            'TimerBarColor': LULL_EFFECT_COLOR
        },
        'TimerStyleSource': 'None'
    }
]
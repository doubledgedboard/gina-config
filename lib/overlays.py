from . import gina_config


def _set_behavior_group_font_size_and_position(
        behavior_group_and_overlay_pair) -> None:
    gina_config.set_behavior_group_font_size(
        behavior_group_and_overlay_pair[0],
        behavior_group_and_overlay_pair[1]['font_size'])
    gina_config.set_behavior_group_position(
        behavior_group_and_overlay_pair[0],
        behavior_group_and_overlay_pair[1]['position'])


def _set_behavior_groups_font_size_and_position(
        behavior_group_and_overlay_pairs) -> None:
    for behavior_group_and_overlay_pair in behavior_group_and_overlay_pairs:
        _set_behavior_group_font_size_and_position(
            behavior_group_and_overlay_pair)


def _collect_behavior_groups_for_overlays(overlays) -> list:
    behavior_group_and_overlay_pairs = []
    for text_overlay in overlays['text']:
        behavior_group_and_overlay_pairs.append((
                gina_config.get_text_behavior_group_by_name(
                    text_overlay['name']),
                text_overlay))
    for timer_overlay in overlays['timer']:
        behavior_group_and_overlay_pairs.append((
                gina_config.get_timer_behavior_group_by_name(
                    timer_overlay['name']),
                timer_overlay))
    return behavior_group_and_overlay_pairs


def update_behavior_groups(overlays) -> None:
    behavior_group_and_overlay_pairs = (
        _collect_behavior_groups_for_overlays(overlays))
    _set_behavior_groups_font_size_and_position(
        behavior_group_and_overlay_pairs)

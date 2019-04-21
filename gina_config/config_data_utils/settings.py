from gina_config.config_data import settings


# public api
# ============================================================================

def set_setting(setting_name, setting_value):
    settings['setting_name'] = setting_value

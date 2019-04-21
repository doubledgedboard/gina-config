from gina_config.config_data_utils.settings import set_setting
from gina_config.names.settings import \
    EVERQUEST_FOLDER_SETTING, \
    IMPORTED_MEDIA_FILE_FOLDER_SETTING, \
    LOG_ARCHIVE_FOLDER_SETTING


# public api
# ============================================================================

def set_everquest_folder_path(path):
    set_setting(EVERQUEST_FOLDER_SETTING, path)


def set_imported_media_file_folder_path(path):
    set_setting(IMPORTED_MEDIA_FILE_FOLDER_SETTING, path)


def set_log_archive_folder_path(path):
    set_setting(LOG_ARCHIVE_FOLDER_SETTING, path)

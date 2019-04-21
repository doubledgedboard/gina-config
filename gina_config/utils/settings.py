from ..config_data.settings import settings


def update_settings_from_file_settings(file_settings) -> None:
    # update gina config settings
    settings['EverquestFolder'] = file_settings['everquest_folder']
    settings['ImportedMediaFileFolder'] = (
        file_settings['imported_media_file_folder'])
    settings['LogArchiveFolder'] = file_settings['log_archive_folder']

from . import gina_config


def update_settings(settings) -> None:
    # update gina config settings
    gina_config.settings['EverquestFolder'] = settings['everquest_folder']
    gina_config.settings['ImportedMediaFileFolder'] = (
        settings['imported_media_file_folder'])
    gina_config.settings['LogArchiveFolder'] = settings['log_archive_folder']

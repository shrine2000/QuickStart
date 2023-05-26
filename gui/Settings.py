from PyQt5.QtCore import QSettings

def store_string(key, value):
    settings = QSettings("app_config.ini", QSettings.IniFormat)
    settings.setValue(key, value)


def retrieve_string(key):
    settings = QSettings("app_config.ini", QSettings.IniFormat)
    return settings.value(key, "")
import configparser
import os
from OpenIni import  createConfig

def crudConfig(path):
    """
    Create, read, update, delete config
    """
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    # Читаем некоторые значения из конфиг. файла.
    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font_size")

    # Меняем значения из конфиг. файла.
    config.set("Settings", "font_size", "12")

    # Удаляем значение из конфиг. файла.
    config.remove_option("Settings", "font_style")

    # Вносим изменения в конфиг. файл.
    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.ini"
    crudConfig(path)

import configparser
import os


def createConfig(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Players skins")
    config.set("Players skins", "ANIMATION_RIGHT ", "Courier")
    config.set("Players skins", "ANIMATION_LEFT ", "10")
    config.set("Players skins", "ANIMATION_JUMP_LEFT", "Normal")
    config.set("Players skins", "ANIMATION_JUMP_RIGHT ", "Ye)s pt")
    config.set("Players skins", "ANIMATION_JUMP", "Normal")
    config.set("Players skins", "ANIMATION_STAY", "Normal")
    config.set("Players skins", "ANIMATION_DEATH", "Normal")

    config.add_section("Skins bot")
    config.set("Skins bot", "ANIMATION_RIGHT", "Courier")
    config.set("Skins bot", "ANIMATION_LEFT ", "10")
    config.set("Skins bot", "ANIMATION_STAY", "Normal")
    config.set("Skins bot", "ANIMATION_DEATH", "Courier")

    config.add_section("Game zone")
    config.set("Game zone", "background color", "(0, 50, 50)")
    config.set("Game zone", "image of block", "s/image/OTHERS/platform.png")
    config.set("Game zone", "WIDTH_WINDOW", "1100")
    config.set("Game zone", "HEIGHT_WINDOW", "640")
    config.set("Game zone", "HEIGHT_WINDOW", "640")

    config.add_section("Others")
    config.set("Others", "Medicine", "640")
    config.set("Others", "Gravity", "0.35")
    config.set("Others", "Speed", "7")
    config.set("Others", "Speed of bullet", "9")
    config.set("Others", "Jump", "-10")
    config.set("Others", "Speed bot", "5")
    with open(path, "w") as config_file:
        config.write(config_file)

if not os.path.exists("settings.ini"):
    createConfig("settings.ini")
if __name__ == "__main__":
    path = "settings.ini"
    createConfig(path)

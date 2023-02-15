"""for administrator powers"""
import ctypes
import os
import random
import sys
from pathlib import Path

from time import sleep

from colored import fg, attr
import cursor
import readchar
import yaml as y
from bullet import Bullet, Input, colors
from click import clear

# colors
RED    = fg('#FF0000')
ORANGE = fg('#FFA500')
YELLOW = fg('#FFFF00')
GREEN  = fg('#00FF00')
BLUE   = fg('#0000FF')
INDIGO = fg('#4B0082')
VIOLET = fg('#8F00FF')
CYAN   = fg('#00FFFF')

#attr
RESET  = attr('reset')
BOLD   = attr('bold')

COLORS: list = [RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET, CYAN]


EXECUTABLE: str = os.path.basename(sys.executable)
ANIMDL: str = f"{random.choice(COLORS)}[animdl-tui]"

ANIMDL_DEFAULT: dict = {
    "default_player": "mpv",
    "discord_presence": True,
    "players": {
        "mpv": {
            "executable": "mpv",
            "opts": []
        }
    }
}

TUI_DEFAULT: dict = {
    "provider": {
        "status": True,
        "val": "allanime"
    },

    "quality": {
        "status": True,
        "val": "1080/best"
    },

    "dir": {
        "status": False,
        "path": ""
    },

    "range": {
        "status": False,
        "val": ""
    },

    "special": {
        "status": False,
        "val": ""
    }
}

def confirmation(conf_prompt: str, choice1: str, choice2: str, color1=GREEN, color2=RED) -> bool:
    """Makes a confirmation prompt and returns either true or false based on user choice."""
    confirmation_bullet = Bullet(
        prompt=f"{conf_prompt}",
        choices=[
            f'- {color1} {choice1} {colors.foreground["default"]}',
            f'- {color2} {choice2} {colors.foreground["default"]}',
        ],
        bullet="",
        margin=0,
        align=1,
        word_on_switch=colors.foreground["default"],
        background_on_switch=colors.background["white"],
    )
    result = confirmation_bullet.launch()
    if choice1 in result:
        return True
    return False

def write_to_config(file: str, config, tree: str, key: str, value=""):
    """writes to config"""
    if value == "":
        config[tree] = f"{key}"
    else:
        config[tree][key] = f"{value}"

    with open(file, "w", encoding="utf-8") as buffer:
        y.dump(config, buffer)


def continue1():
    """Continue function"""
    print("\n Press any key to continue")
    getkey()

def main():
    """main function"""
    main_menu = Bullet (
        bullet="",
        prompt=f"{ANIMDL}",
        choices=[
            "1. Download",
            "2. Stream  ",
            "3. Search  ",
            "4. Schedule",
            "5. Grab    ",
            "6. Update  "
        ],
        pad_right=2,
        shift=2,
        return_index=True
    )
    main_menu_result = main_menu.launch()

if __name__ == "__main__":
    if "win32" in sys.version:
        config_path = Path(os.getenv('LOCALAPPDATA', ".")) / ".config" / "animdl-tui" / "config.yml"

    else:
        config_path = Path(os.getenv('HOME', ".")) / ".config"/"animdl-tui"/"config.yml"
    main()

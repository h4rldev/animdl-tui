"""for administrator powers"""
import os
import random
import sys
from pathlib import Path
from time import sleep

import cursor
import readchar
import yaml as y
from bullet import Bullet, Input, colors
from click import clear
from colored import attr, fg

from animdltui import download, grab, schedule, search, stream, update


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
    "skip_main_menu": False,

    "dir": {
      "status": False,
      "val": ""
    },

    "quality": {
      "status": True,
      "val": "1080/best"
    },

    "range": {
      "status": False,
      "val": "1-89"
    },

    "special": {
      "status": False,
      "val": ""
    }
}

def todo():
    pass

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

def main_menu() -> int:
    with open("config.yml", "r", encoding="utf-8") as buffer:
        tui_config = y.safeload(buffer)

    if tui_config["skip_main_menu"]:
        return 1

    menu = Bullet(
        bullet="",
        prompt=f"{ANIMDL}",
        choices=[
            "1. animdl-tui",
            "2. config",
            "3. exit"
        ]
    )
    if "1" in menu.launch():
        return 1
    elif "2" in menu.launch():
        return 2
    else:
        return 3

def provider():
    todo()

def directory():
    todo()


def main():
    """main function"""
    menu_choices: list = [
        [
            "1. animdl-tui",
            "2. config    ",
            "3. exit      "
        ],
        [
            "1. Download",
            "2. Stream  ",
            "3. Search  ",
            "4. Schedule",
            "5. Grab    ",
            "6. Update  ",
            "7. Quit    "
        ]
    ]

    config_menu_choices: list = [
        ""   
    ]

    menu_dict: dict = {
        {
            menu_choices[0][0] : animdl_menu(),
            menu_choices[0][1] : config_menu(),
            menu_choices[0][2] : sys.exit()
        },
        {
            menu_choices[1][0] : download_menu(),
            menu_choices[1][1] : stream_menu(),
            menu_choices[1][2] : search_menu(),
        }
    }

    config_menu = Bullet(
        bullet="",
        prompt=f"{ANIMDL}",
        choices=config_menu_choices
    )
    
    
    animdl_menu = Bullet (
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
    
    if 1 in main_menu():
        animdl_menu_result = animdl_menu.launch()
    else:
        config_menu_result = config_menu.launch()
        

if __name__ == "__main__":
    if "win32" in sys.version:
        config_path = Path(os.getenv('LOCALAPPDATA', ".")) / ".config" / "animdl-tui" / "config.yml"

    else:
        config_path = Path(os.getenv('HOME', ".")) / ".config"/"animdl-tui"/"config.yml"
    main()

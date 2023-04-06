import os
import random
import sys
from pathlib import Path
from time import sleep

import cursor
import readchar
import yaml as y
from rebullet import Bullet, Input, colors
from click import clear
from colored import attr, fg

from modules import download, grab, schedule, search, stream, update, colors, config

COLORS: list = [
    colors.FG_RED,
    colors.FG_ORANGE,
    colors.FG_YELLOW,
    colors.FG_GREEN,
    colors.FG_BLUE,
    colors.FG_INDIGO,
    colors.FG_VIOLET,
    colors.FG_CYAN,
]

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
            "7. Quit    ",
        ],
    ]


menu_results: dict = {
    menu_choices[1][0]: download.download(),
    menu_choices[1][1]: stream.stream(),
    menu_choices[1][2]: sys.exit(),
}

ANIMDL: str = f"{random.choice(COLORS)}[animdl-tui]"


def todo():
    pass

def confirmation(
    conf_prompt: str,
    choice1: str,
    choice2: str,
    color1=colors.FG_GREEN,
    color2=colors.FG_RED,
) -> bool:
    """
    Makes a confirmation prompt and returns either true or false based on user choice.
    """
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

def main():
    """main function"""

    init_menu = Bullet(
        bullet="", prompt=f"{ANIMDL}", choices=menu_choices[0], pad_right=2, shift=2
    )

    animdl_menu = Bullet(
        bullet="", prompt=f"{ANIMDL}", choices=menu_choices[1], pad_right=2, shift=2
    )

    try:
        with open("tui_config.yml", "r", encoding="utf-8") as buffer:
            tui_config = y.safeload(buffer)
            if tui_config["skip_main_menu"]:
                animdl_menu_result = animdl_menu.launch()
            else:
                init_menu_result = init_menu.launch()

    except FileNotFoundError:
        init_menu_result = init_menu.launch()

    if "1" in init_menu_result:
        animdl_menu_result = animdl_menu.launch()
        if animdl_menu_result in menu_choices[1]:
            menu_choices[animdl_menu_result]
        
    elif "3" in init_menu_result:
        sys.exit(0)
        
    else:
        config.main()

if __name__ == "__main__":
    main()
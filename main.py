"""for administrator powers"""
import ctypes
import os
import random
import sys
from msvcrt import getch as getkey
from time import sleep

import cursor
import yaml as y
from bullet import Bullet, Input, colors
from click import clear
from colored import attr, fg
from flask import Flask, render_template

def checkforadmin():
    """Checks if the user is admin"""
    if sys.platform == 'win32':
        return ctypes.windll.shell32.IsUserAnAdmin()

ANIMDL = "[animdl-tui]"
ANIMDL_CONFIG = "animdl_config.yml"
CONFIG_FILE = "config.yml"


ANIMDL_DEFAULT = {
    "default_player": "mpv",
    "players": {
        "mpv": {
            "executable": "mpv",
            "opts": []
        }
    },
    "discord_presence": False
}
CONFIG_DEFAULT = {
    "modifiers":{
        "dir": "\\",
        "provider": "animixplay",
        "quality": "1080/best",
        "range": "1-89",
        "special": "latest-89"
    },
    "toggles":{
        "dir": False,
        "quality": True,
        "range": False,
        "special": False,
    },
    "web":{
        "web": False
    }
}

def doespackageexist(package):
    """Checks if a package exists"""
    is_present = os.system(f"pip show {package}")
    if is_present == 1:
        return False
    return True

def ismoduleon(config_file, module: str):
    """Checks if pypresence is enabled or not"""
    with open(config_file, 'r', encoding="utf-8") as module_io:
        module_check = y.safe_load(module_io)
        if module_check[module] is True:
            return module_check[module]
        return False

def checkifexists(file, mode, default_data):
    """Checks if a file exists, if it doesn't it, it creates it and writes default data to it"""
    if os.path.isfile(file) is False:
        with open(file, mode, encoding="utf-8") as make_config_file:
            y.dump(default_data, make_config_file)
    else:
        pass

cyan = fg("cyan")
reset = attr("reset")
bold = attr("bold")
green = fg("green")
red = fg("red")
blue = fg("blue")
orange = fg("58")
purple = fg("54")
yellow = fg("yellow")
randcolors = [cyan, green, red, blue, orange, purple, yellow]

def randcolforname(name):
    """Randomly changes the color of a string based on an array of values"""
    randomcolors = random.choice(randcolors)
    print(f"{bold}{randomcolors} {name}\n{reset}")

def continue1():
    """Continue function"""
    print("\n Press any key to continue")
    getkey()

def cts():
    """Fixes actually nothing just convenient"""
    clear()
    thesettings()

def c_m():
    """Convenience"""
    clear()
    main()

def cpts():
    """"Fixes redundance and lint"""
    clear()
    print("Ok! returning...")
    thesettings()

def thesettings():
    """settings function"""
    cursor.hide()
    with open(CONFIG_FILE, 'r', encoding="utf-8") as configfile_read:
        tui_config = y.safe_load(configfile_read)
    with open(ANIMDL_CONFIG, 'r', encoding="utf-8") as animdl_config_read:
        animdl_config = y.safe_load(animdl_config_read)
    def special():
        cursor.hide()
        randomnumber = random.randint(0, 1000)
        randcolforname(ANIMDL)
        special_range = Bullet(
            prompt = f"{cyan} Are you sure you want a special range? {reset} \n",
            choices = [
                f'- {green}Yes {colors.foreground["default"]}',
                f'- {red}No  {colors.foreground["default"]}',
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch=colors.foreground["default"],
            background_on_switch=colors.background["white"]
        )
        result = special_range.launch()
        if result == f"- {green}Yes {colors.foreground['default']}":
            clear()
            randcolforname(ANIMDL)
            special_range_input = Input(
                prompt = (f"{cyan} Specify a special range.{reset}"
                        f" (Example: \"latest-{randomnumber}\")\n {red}:{reset} "),
                pattern = "latest-"
            )

            special_range_input_result = special_range_input.launch()
            if tui_config['toggles']['special'] is True:
                print(
                    f" ´SPECIAL RANGE´ is now '{special_range_input_result}'")
                tui_config['modifiers']['special'] = f'{special_range_input_result}'
                with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                    y.dump(tui_config, configfile_write)
                    sleep(1)
                    cts()

            else:
                print(" ´SPECIAL RANGE´ is False")
                special_toggle = Bullet(
                    prompt = (f"{cyan} Would you like to enable ´SPECIAL RANGE´? {reset} \n"),
                    choices = [
                        f'- {green}Yes {colors.foreground["default"]}',
                        f'- {red}No  {colors.foreground["default"]}',
                    ],
                    bullet = "",
                    margin = 0,
                    align = 1,
                    word_on_switch = colors.foreground["default"],
                    background_on_switch = colors.background["white"]
                )
                special_toggle_result = special_toggle.launch()
                if special_toggle_result == f"- {green}Yes {colors.foreground['default']}":
                    print(" ´SPECIAL RANGE´ is now True")
                    tui_config['toggles']['special'] = True
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile:
                        y.dump(tui_config, configfile)
                    print(
                        f" ´SPECIAL RANGE´ is now '{special_range_input_result}'")
                    tui_config['modifiers']['range'] = f'{special_range_input_result}'
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    sleep(1)
                    cts()
                else:
                    cpts()
        else:
            cpts()

    def therange():
        cursor.hide()
        randomnumber = random.randint(0, 1000)
        randcolforname(ANIMDL)
        specific_range = Bullet(
            prompt = f"{cyan} Are you sure you want a specific range? {reset} \n",
            choices = [
                f'- {green}Yes {colors.foreground["default"]}',
                f'- {red}No  {colors.foreground["default"]}',
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch = colors.foreground["default"],
            background_on_switch = colors.background["white"]
        )
        result = specific_range.launch()
        if result == f"- {green}Yes {colors.foreground['default']}":
            clear()
            randcolforname(ANIMDL)
            specific_range_input = Input(
                prompt = (f"{cyan}Specify a range.{reset}"
                        f" (Example: \"{randomnumber}-{randomnumber}\")"
                        f"\n {red}:{reset} "),
            )

            specific_range_input_result = specific_range_input.launch()
            if tui_config['toggles']['range'] is True:
                print(f"´RANGE´ is now {specific_range_input_result}")
                tui_config['modifiers']['range'] = f'{specific_range_input_result}'
                with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                    y.dump(tui_config, configfile_write)
                sleep(1)
                cts()

            else:
                print("´RANGE´ is False")
                specific_range_toggle = Bullet(
                    prompt = f"{cyan} Would you like to enable ´RANGE´? {reset} \n",
                    choices = [
                        f'- {green}Yes {colors.foreground["default"]}',
                        f'- {red}No  {colors.foreground["default"]}',
                    ],
                    bullet = "",
                    margin = 0,
                    align = 1,
                    word_on_switch = colors.foreground["default"],
                    background_on_switch = colors.background["white"]
                )
                specific_range_toggle_result = specific_range_toggle.launch()
                if specific_range_toggle_result == f"- {green}Yes {colors.foreground['default']}":
                    print(" ´RANGE´ is now True")
                    tui_config['toggles']['range'] = True
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    print(
                        f" ´RANGE´ is now {specific_range_input_result}")
                    tui_config['modifiers']['range'] = f'{specific_range_input_result}'
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    sleep(1)
                    cts()
                else:
                    cpts()
        else:
            cpts()

    def quality():
        cursor.hide()
        randcolforname(ANIMDL)
        quality = Bullet(
            prompt = f"{cyan} Are you sure you want a specific quality? {reset} \n",
            choices = [
                f'- {green}Yes {colors.foreground["default"]}',
                f'- {red}No  {colors.foreground["default"]}',
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch = colors.foreground["default"],
            background_on_switch = colors.background["white"],
        )
        result = quality.launch()
        if result == f"- {green}Yes {colors.foreground['default']}":
            clear()
            randcolforname(ANIMDL)
            quality_input = Input(
                prompt = (f"{cyan} Specify a quality.{reset}"
                f" (Examples: '1080', '1080/best', '1080/worst',"
                f" 'best[title]', 'best[title=r'^DUB']')"
                f"\n {red}:{reset} "),
            )
            quality_input_result = quality_input.launch()
            if tui_config['toggles']['quality'] is True:
                print(f" ´QUALITY´ is now {quality_input_result}")
                tui_config['modifiers']['quality'] = f'{quality_input_result}'
                with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                    y.dump(tui_config, configfile_write)
                sleep(1)
                cts()
            else:
                print(" ´QUALITY´ is False")
                quality_toggle = Bullet(
                    prompt = f"{cyan} Would you like to enable ´QUALITY´? {reset} \n",
                    choices = [
                        f'- {green}Yes {colors.foreground["default"]}',
                        f'- {red}No  {colors.foreground["default"]}',
                    ],
                    bullet = "",
                    margin = 0,
                    align = 1,
                    word_on_switch = colors.foreground["default"],
                    background_on_switch = colors.background["white"]
                )
                quality_toggle_result = quality_toggle.launch()
                if quality_toggle_result == f"- {green}Yes {colors.foreground['default']}":
                    print(" ´QUALITY´ is now True")
                    tui_config['toggles']['quality'] = True
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                        print(
                            f" ´QUALITY´ is now {quality_input_result}")
                        tui_config['modifiers']['quality'] = f'{quality_input_result}'
                        with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                            y.dump(tui_config, configfile_write)
                            sleep(1)
                            cts()
                else:
                    cpts()
        else:
            cpts()

    def player():
        cursor.hide()
        randcolforname(ANIMDL)
        player = Bullet(
            prompt = (f"{cyan}"
            f" Are you sure you want to switch to a different player?{reset} \n (default: mpv) \n"),
            choices = [
                f'- {green}Yes {colors.foreground["default"]}',
                f'- {red}No  {colors.foreground["default"]}',
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch = colors.foreground["default"],
            background_on_switch = colors.background["white"]
        )
        result = player.launch()
        if result == f"- {green}Yes {colors.foreground['default']}":
            clear()
            randcolforname(ANIMDL)
            player_choice = Bullet(
                prompt = f"{cyan} Choose a player. {reset} \n",
                choices = [
                    '- mpv (default)  ',
                    '- vlc            ',
                    '- ffplay (ffmpeg)',
                    '- exit           '
                ],
                bullet = "",
                margin = 0,
                align = 1,
                word_on_switch = colors.foreground["default"],
                background_on_switch = colors.background["cyan"]
            )
            player_choice_result = player_choice.launch()
            match player_choice_result:
                case '- mpv (default)  ':
                    data = {
                        "default_player": "mpv",
                        "players": {
                            "mpv": {
                                "executable": "mpv",
                                "opts": []
                            }
                        }
                    }
                    print(" mpv should now be the selected player.")

                    with open(ANIMDL_CONFIG, 'w', encoding="utf-8") as animdl_config_write:
                        y.dump(data, animdl_config_write)
                    sleep(1)
                    cts()

                case '- vlc            ':
                    data = {
                        "default_player": "vlc",
                        "players": {
                            "vlc": {
                                "executable": "vlc",
                                "opts": []
                            }
                        }
                    }

                    print(" vlc should now be the selected player.")

                    with open(ANIMDL_CONFIG, 'w', encoding="utf-8") as animdl_config_write:
                        y.dump(data, animdl_config_write)
                    sleep(1)
                    cts()


                case '- ffplay (ffmpeg)':
                    data = {
                        "default_player": "ffplay",
                        "players": {
                            "ffplay": {
                                "executable": "ffplay",
                                "opts": []
                            }
                        }
                    }

                    print(" ffplay should now be the selected player.")

                    with open(ANIMDL_CONFIG, 'w', encoding="utf-8") as animdl_config_write:
                        y.dump(data, animdl_config_write)
                    sleep(1)
                    cts()

                case '- exit           ':
                    cts()
        else:
            cpts()

    def provider():
        cursor.hide()
        randcolforname(ANIMDL)
        provider = Bullet(
            prompt = (f"{cyan} Are you sure you want to switch to a different provider? {reset}\n"
                    f" (default: animixplay) \n"),
            choices = [
                f'- {green}Yes {colors.foreground["default"]}',
                f'- {red}No  {colors.foreground["default"]}',
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch = colors.foreground["default"],
            background_on_switch = colors.background["white"]
        )
        result = provider.launch()
        if result == f"- {green}Yes {colors.foreground['default']}":
            clear()
            randcolforname(ANIMDL)
            provider_choice = Bullet(
                prompt = f"{cyan} Choose a provider {reset} (sorted by latency). \n",
                choices = [
                    '- animixplay (default)',
                    '- animepahe           ',
                    '- haho (NSFW)         ',
                    '- gogoanime           ',
                    '- tenshi.moe          ',
                    '- allanime            ',
                    '- exit                '
                    ],
                bullet = "",
                margin = 0,
                align = 1,
                word_on_switch=colors.foreground["default"],
                background_on_switch=colors.background["cyan"]
            )
            provider_choice_result = provider_choice.launch()

            match provider_choice_result:

                case '- animixplay (default)':
                    print(" The provider has now been set to animixplay.")
                    tui_config['modifiers']['provider'] = 'animixplay'
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    sleep(1)
                    cts()

                case '- animepahe           ':
                    print(" The provider has now been set to animepahe.")
                    tui_config['modifiers']['provider'] = 'animepahe'
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    sleep(1)
                    cts()

                case '- haho (NSFW)         ':
                    print(" The provider has now been set to haho (NSFW).")
                    tui_config['modifiers']['provider'] = 'haho'
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    sleep(1)
                    cts()

                case '- gogoanime           ':
                    print(" The provider has now been set to gogoanime.")
                    tui_config['modifiers']['provider'] = 'gogoanime'
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    sleep(1)
                    cts()

                case '- tenshi.moe          ':
                    print(" The provider has now been set to tenshi.moe.")
                    tui_config['modifiers']['provider'] = 'tenshi'
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    sleep(1)
                    cts()

                case '- allanime            ':
                    print(" The provider has now been set to allanime.")
                    tui_config['modifiers']['provider'] = 'allanime'
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    sleep(1)
                    cts()

                case '- exit                ':
                    cts()
        else:
            cpts()

    def toggle():
        cursor.hide()
        clear()
        if animdl_config['discord_presence'] is False:
            presencestatus = 'False'
            presencestatuscolor = red
        else:
            presencestatus = 'True'
            presencestatuscolor = green
        if tui_config['toggles']['special'] is False:
            specialstatus = 'False'
            specialstatuscolor = red
        else:
            specialstatus = 'True'
            specialstatuscolor = green

        if tui_config['toggles']['range'] is False:
            rangestatus = 'False'
            rangestatuscolor = red
        else:
            rangestatus = 'True'
            rangestatuscolor = green

        if tui_config['toggles']['quality'] is False:
            qualitystatus = 'False'
            qualitystatuscolor = red
        else:
            qualitystatus = 'True'
            qualitystatuscolor = green

        if tui_config['toggles']['dir'] is False:
            dirstatus = 'False'
            dirstatuscolor = red
        else:
            dirstatus = 'True'
            dirstatuscolor = green

        qualitychoice = f'- QUALITY = {qualitystatuscolor}{qualitystatus:5}'
        dirchoice = f'- DIR = {dirstatuscolor}{dirstatus:5}'
        rangechoice = f'- RANGE = {rangestatuscolor}{rangestatus:5}'
        specialchoice = f'- SPECIAL RANGE = {specialstatuscolor}{specialstatus:5}'
        presencechoice = f'- DISCORD PRESENCE = {presencestatuscolor}{presencestatus:5}'

        randcolforname(ANIMDL)
        modules = Bullet(
            prompt = f"{cyan} Toggle modules: {reset} \n",
            choices = [
                f'{qualitychoice}',
                f'{dirchoice}',
                f'{rangechoice}',
                f'{specialchoice}',
                f'{presencechoice}',
                '- Exit    '
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch = colors.foreground["default"],
            background_on_switch = colors.background["cyan"]
        )
        result = modules.launch()

        if result == qualitychoice:
            result = 0
        elif result == dirchoice:
            result = 1
        elif result == rangechoice:
            result = 2
        elif result == specialchoice:
            result = 3
        elif result == presencechoice:
            result = 4

        match result:
            case '- Exit    ':
                cts()

            case 0:
                if tui_config['toggles']['quality'] is True:
                    print(" ´QUALITY´ is now False")
                    tui_config['toggles']['quality'] = False
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    toggle()
                else:
                    print(" ´QUALITY´ is now True")
                    tui_config['toggles']['quality'] = True
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    toggle()
            case 1:
                if tui_config['toggles']['dir'] is True:
                    print(" ´DIR´ is now False")
                    tui_config['toggles']['dir'] = False
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    toggle()
                else:
                    print(" ´DIR´ is now True")
                    tui_config['toggles']['dir'] = True
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    toggle()
            case 2:
                if tui_config['toggles']['range'] is True:
                    print(" ´RANGE´ is now False")
                    tui_config['toggles']['range'] = False
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    toggle()
                else:
                    print(" ´RANGE´ is now True")
                    tui_config['toggles']['range'] = True
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    toggle()
            case 3:
                if tui_config['toggles']['special'] is True:
                    print(" ´SPECIAL RANGE´ is now False")
                    tui_config['toggles']['special'] = False
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    toggle()
                else:
                    print(" ´SPECIAL RANGE´ is now True")
                    tui_config['toggles']['special'] = True
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                    toggle()
            case 4:
                if animdl_config['discord_presence'] is True:
                    print(" ´DISCORD PRESENCE´ is now False")
                    animdl_config['discord_presence'] = False
                    with open(ANIMDL_CONFIG, 'w', encoding="utf-8") as animdl_config_write:
                        y.dump(animdl_config, animdl_config_write)
                    toggle()
                else:
                    print(" ´DISCORD PRESENCE´ is now True")
                    animdl_config['discord_presence'] = True
                    with open(ANIMDL_CONFIG, 'w', encoding="utf-8") as animdl_config_write:
                        y.dump(animdl_config, animdl_config_write)
                    if doespackageexist("pypresence") is True and ismoduleon(
                    ANIMDL_CONFIG,
                    "discord_presence"
                    ) is True:
                        toggle()

                    else:
                        print("Whoops, doesn't look like you have pypresence installed.")
                        print("Please install it manually or by pressing enter. Thanks")
                        continue1()
                        if os.path.isfile("pypresence.txt") is True:
                            print(
                                "Seems like you encountered a bug."
                                "Please report it to me on github.com"
                            )
                        else:
                            with open("pypresence.txt",
                                "a",
                                encoding="utf-8"
                            ) as pypresence_signal2:
                                pypresence_signal2.write("pypresence installus")
                                print(
                                    "pypresence will try to install on next startup of animdl-tui"
                                )
                            ctypes.windll.shell32.ShellExecuteW(
                                None,
                                "runas",
                                sys.executable,
                                " ".join(sys.argv),
                                None,
                                1
                            )
                            sys.exit()

    def directory():
        cursor.hide()
        randcolforname(ANIMDL)
        directory = Bullet(
            prompt = f"{cyan} Are you sure you want a specific directory? {reset} \n",
            choices = [
                f'- {green}Yes {colors.foreground["default"]}',
                f'- {red}No  {colors.foreground["default"]}',
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch = colors.foreground["default"],
            background_on_switch = colors.background["white"]
        )
        result = directory.launch()
        if result == f"- {green}Yes {colors.foreground['default']}":
            clear()
            randcolforname(ANIMDL)
            dir_input = Input(
                prompt = (f"{cyan} Enter a vaild directory. (Example: 'C:\\Users\\'){reset}"
                f"\n {red}:{reset} "),
                indent = 0,
            )
            dir_input_result = dir_input.launch()
            if tui_config['toggles']['dir'] is True:
                print(f" ´DIR´ is now {dir_input_result}")
                tui_config['modifiers']['dir'] = f'{dir_input_result}'
                with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                    y.dump(tui_config, configfile_write)
                sleep(1)
                cts()
            else:
                print(" ´DIR´ is False")
                dir_toggle = Bullet(
                    prompt = f"{green} - Would you like to enable ´DIR´? {reset} \n",
                    choices = [
                        f'- {green}Yes {colors.foreground["default"]}',
                        f'- {red}No  {colors.foreground["default"]}',
                    ],
                    bullet = "",
                    margin = 0,
                    align = 1,
                    word_on_switch = colors.foreground["default"],
                    background_on_switch = colors.background["white"]
                )
                dir_toggle_result = dir_toggle.launch()
                if dir_toggle_result == f"- {green}Yes {colors.foreground['default']}":
                    print(" ´DIR´ is now True")
                    tui_config['toggles']['dir'] = True
                    with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                        y.dump(tui_config, configfile_write)
                        print(
                            f" ´DIR´ is now {dir_input_result}")
                        tui_config['modifiers']['dir'] = f'"{dir_input_result}"'
                        with open(CONFIG_FILE, 'w', encoding="utf-8") as configfile_write:
                            y.dump(tui_config, configfile_write)
                            sleep(1)
                            cts()
                else:
                    cpts()
        else:
            cpts()

    clear()
    randcolforname(ANIMDL)
    settings = Bullet(
        prompt = f"{green} Settings: {reset} \n",
        choices = [
            '- Toggle  ',
            '- Provider',
            '- Player  ',
            '- Quality ',
            '- Range   ',
            '- Special ',
            '- Dir     ',
            '- Exit    '
        ],
        bullet = "",
        margin = 0,
        align = 1,
        word_on_switch = colors.foreground["default"],
        background_on_switch = colors.background["cyan"]
    )
    result = settings.launch()
    match result:
        case '- Toggle  ':
            clear()
            toggle()
        case '- Provider':
            clear()
            provider()
        case '- Player  ':
            clear()
            player()
        case '- Quality ':
            clear()
            quality()
        case '- Range   ':
            clear()
            therange()
        case '- Special ':
            clear()
            special()
        case '- Dir     ':
            clear()
            directory()
        case '- Exit    ':
            clear()
            main()

def main():
    """main function"""
    cursor.hide()
    def update():
        cursor.hide()
        if os.path.isfile("update.txt") is True:
            print("Seems like you encountered a bug. Please report it to me on github.com")
        else:
            with open("update.txt", "a", encoding="utf-8") as update_signal:
                update_signal.write("updatus")
                print("animdl will try to update on next startup of animdl-tui")
            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                sys.executable,
                " ".join(sys.argv),
                None,
                1
            )
            sys.exit()

    def web():
        cursor.hide()
        app = Flask(__name__)

        @app.route("/")
        def index():
            return render_template('index.html')

        app.run()

    def stream():
        cursor.hide()
        with open (ANIMDL_CONFIG, 'r', encoding='utf8') as animdl_config_read:
            animdl_config = y.safe_load(animdl_config_read)

        with open(CONFIG_FILE, 'r', encoding="utf-8") as configfile_read:
            tui_config = y.safe_load(configfile_read)

        quality_status = tui_config['toggles']['quality']
        quality = tui_config['modifiers']['quality']
        animdlrange_status = tui_config['toggles']['range']
        animdlrange = tui_config['modifiers']['range']
        special_status = tui_config['toggles']['special']
        special = tui_config['modifiers']['special']
        provider = tui_config['modifiers']['provider']

        randcolforname(ANIMDL)

        print(f"Provider = {cyan}{tui_config['modifiers']['provider']}{reset}")
        if quality_status is True:
            qualityarg = f"-q {quality}"
            print(f" Quality = {cyan}{quality}{reset}")
        else:
            qualityarg = ""
            print(f" Quality is {red}{quality_status}{reset}")
        if animdlrange_status is True:
            rangearg = f"-r {animdlrange}"
            print(f" Range = {cyan}{animdlrange}{reset}")
        else:
            rangearg = ""
            print(f" Range is {red}{animdlrange_status}{reset}")
        if special_status is True:
            specialarg = f"-s {special}"
            print(f" Special Range = {cyan}{special}{reset}")
        else:
            specialarg = ""
            print(f" Special Range is {red}{special_status}{reset}")
        print(f" Player = {cyan}{animdl_config['default_player']}{reset}")
        streamus = Input(
            prompt = f"{cyan} Enter anime name.\n {red}:{reset} ",
            indent = 0
        )
        streamus.result = streamus.launch()
        streamareyousure = Bullet(
            prompt = f"{cyan} Are you sure you want to stream {streamus.result}? \n",
            choices = [
                f"- {green}Yes",
                f"- {red}No",
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch=colors.foreground["default"],
            background_on_switch=colors.background["white"]
        )
        streamareyousure.result = streamareyousure.launch()
        if streamareyousure.result == f"- {green}Yes":
            pass
        else:
            c_m()
        os.system(f'animdl stream'
                f'{specialarg} {rangearg} {qualityarg} "{provider}:{streamus.result}"')
        continue1()
        clear()
        randcolforname(ANIMDL)
        locs = Bullet(
            prompt = f"{cyan} Do you want to leave or do you want to continue streaming?{reset}",
            choices = [
                f"- {green}Continue",
                f"- {red}Leave",
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch=colors.foreground["default"],
            background_on_switch=colors.background["white"]
        )
        locs.result = locs.launch()
        if locs.result == f"- {green}Continue":
            locs.result = 0
        else:
            locs.result = 1

        match locs.result:
            case 0:
                clear()
                stream()
            case 1:
                c_m()

    def search():
        cursor.hide()
        with open(CONFIG_FILE, 'r', encoding="utf-8") as configfile_read:
            tui_config = y.safe_load(configfile_read)
        provider = tui_config['modifiers']['provider']
        searchus = Input(
            prompt = f"{cyan} Enter anime name.\n {red}:{reset} ",
            indent = 0
        )
        searchus.result = searchus.launch()
        searchusareyousure = Bullet(
            prompt = f"{cyan} Are you sure you want to search {searchus.result}? \n",
            choices = [
                f"- {green}Yes",
                f"- {red}No",
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch=colors.foreground["default"],
            background_on_switch=colors.background["white"]
        )
        searchusareyousure.result = searchusareyousure.launch()
        if searchusareyousure.result == f"- {green}Yes":
            pass
        else:
            c_m()
        os.system(f'animdl search -p {provider} "{searchus.result}"')
        clear()
        randcolforname(ANIMDL)
        locs = Bullet(
            prompt = f"{cyan} Do you want to leave or do you want to continue searching?{reset}",
            choices = [
                f"- {green}Continue",
                f"- {red}Leave",
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch=colors.foreground["default"],
            background_on_switch=colors.background["white"]
        )
        locs.result = locs.launch()
        if locs.result == f"- {green}Continue":
            locs.result = 0
        else:
            locs.result = 1

        match locs.result:
            case 0:
                clear()
                download()
            case 1:
                c_m()

    def schedule():
        cursor.hide()
        randcolforname(ANIMDL)
        print(f"{cyan} Schedule: {reset}")
        os.system("animdl schedule")
        continue1()
        c_m()

    def grab():
        cursor.hide()
        with open(CONFIG_FILE, 'r', encoding="utf-8") as configfile_read:
            tui_config = y.safe_load(configfile_read)
        provider = tui_config['modifiers']['provider']
        grabus = Input(
            prompt = f"{cyan} Enter anime name.\n {red}:{reset} ",
            indent = 0
        )
        grabus.result = grabus.launch()
        grabusareyousure = Bullet(
            prompt = f"{cyan} Are you sure you want to search {grabus.result}? \n",
            choices = [
                f"- {green}Yes",
                f"- {red}No",
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch=colors.foreground["default"],
            background_on_switch=colors.background["white"]
        )
        grabusareyousure.result = grabusareyousure.launch()
        if grabusareyousure.result == f"- {green}Yes":
            pass
        else:
            c_m()
        os.system(f'animdl grab "{provider}:{grabus.result}"')
        continue1()
        clear()
        randcolforname(ANIMDL)
        locg = Bullet(
            prompt = f"{cyan} Do you want to leave or do you want to continue grabbing?{reset}",
            choices = [
                f"- {green}Continue",
                f"- {red}Leave",
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch=colors.foreground["default"],
            background_on_switch=colors.background["white"]
        )
        locg.result = locg.launch()
        if locg.result == f"- {green}Continue":
            locg.result = 0
        else:
            locg.result = 1

        match locg.result:
            case 0:
                clear()
                download()
            case 1:
                c_m()

    def download():
        cursor.hide()
        with open (ANIMDL_CONFIG, 'r', encoding='utf8') as animdl_config_read:
            animdl_config = y.safe_load(animdl_config_read)

        with open(CONFIG_FILE, 'r', encoding="utf-8") as configfile_read:
            tui_config = y.safe_load(configfile_read)

        directory_status = tui_config['toggles']['dir']
        directory = tui_config['modifiers']['dir']
        quality_status = tui_config['toggles']['quality']
        quality = tui_config['modifiers']['quality']
        animdlrange_status = tui_config['toggles']['range']
        animdlrange = tui_config['modifiers']['range']
        special_status = tui_config['toggles']['special']
        special = tui_config['modifiers']['special']
        provider = tui_config['modifiers']['provider']

        randcolforname(ANIMDL)

        print(f"Provider = {cyan}{tui_config['modifiers']['provider']}{reset}")
        if quality_status is True:
            qualityarg = f"-q {quality}"
            print(f" Quality = {cyan}{quality}{reset}")
        else:
            qualityarg = ""
            print(f" Quality is {red}{quality_status}{reset}")
        if directory_status is True:
            directoryarg = f"-d {directory}"
            print(f" Directory = {cyan}{directory}{reset}")
        else:
            directoryarg = ""
            print(f" Directory is {red}{directory_status}{reset}")
        if animdlrange_status is True:
            rangearg = f"-r {animdlrange}"
            print(f" Range = {cyan}{animdlrange}{reset}")
        else:
            rangearg = ""
            print(f" Range is {red}{animdlrange_status}{reset}")
        if special_status is True:
            specialarg = f"-s {special}"
            print(f" Special Range = {cyan}{special}{reset}")
        else:
            specialarg = ""
            print(f" Special Range is {red}{special_status}{reset}")
        print(f" Player = {cyan}{animdl_config['default_player']}{reset}")
        downloadus = Input(
            prompt = f"{cyan} Enter anime name.\n {red}:{reset} ",
            indent = 0
        )
        downloadus.result = downloadus.launch()
        downloadusareyousure = Bullet(
            prompt = f"{cyan} Are you sure you want to search {downloadus.result}? \n",
            choices = [
                f"- {green}Yes",
                f"- {red}No",
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch=colors.foreground["default"],
            background_on_switch=colors.background["white"]
        )
        downloadusareyousure.result = downloadusareyousure.launch()
        if downloadusareyousure.result == f"- {green}Yes":
            pass
        else:
            c_m()
        os.system(f'animdl download'
                f'{specialarg} {rangearg} {qualityarg} {directoryarg} '
                f'"{provider}:{downloadus.result}"')
        continue1()
        clear()
        randcolforname(ANIMDL)
        locd = Bullet(
            prompt = f"{cyan} Do you want to leave or do you want to continue downloading?{reset}",
            choices = [
                f"- {green}Continue",
                f"- {red}Leave",
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch=colors.foreground["default"],
            background_on_switch=colors.background["white"]
        )
        locd.result = locd.launch()
        if locd.result == f"- {green}Continue":
            locd.result = 0
        else:
            locd.result = 1

        match locd.result:
            case 0:
                clear()
                download()
            case 1:
                c_m()

    def menu():
        cursor.hide()
        randcolforname(ANIMDL)
        menu = Bullet(
            prompt = f"{green} Main Menu: {reset} \n",
            choices = [
                '- Download',
                '- Stream  ',
                '- Search  ',
                '- Schedule',
                '- Grab    ',
                '- Update  ',
                '- Settings',
                '- Web (WIP/Not Working)',
                '- Exit    '
            ],
            bullet = "",
            margin = 0,
            align = 1,
            word_on_switch = colors.foreground["default"],
            background_on_switch = colors.background["cyan"]
        )

        menu.result = menu.launch()

        match menu.result:
            case '- Download':
                clear()
                download()
            case '- Stream  ':
                clear()
                stream()
            case '- Search  ':
                clear()
                search()
            case '- Schedule':
                clear()
                schedule()
            case '- Grab    ':
                clear()
                grab()
            case '- Update  ':
                clear()
                update()
            case '- Settings':
                clear()
                thesettings()
            case '- Web (WIP/Not Working)':
                clear()
                web()
            case '- Exit    ':
                clear()
                sys.exit()
    menu()

if __name__ == '__main__':
    clear()
    cursor.hide()

    if checkforadmin() is True:
        ctypes.windll.kernel32.SetConsoleTitleW("animdl-tui - Administrator")
    else:
        ctypes.windll.kernel32.SetConsoleTitleW("animdl-tui")

    checkifexists(ANIMDL_CONFIG, 'x', ANIMDL_DEFAULT)
    checkifexists(CONFIG_FILE, 'x', CONFIG_DEFAULT)

    if checkforadmin() and os.path.isfile("animdl.txt") is True:
        with open("animdl.txt", "r", encoding="utf-8") as animdl_signal_read:
            if animdl_signal_read.read() == "animdl installus":
                os.system("pip install animdl")
            else:
                print("bruh")
        os.remove("animdl.txt")
        continue1()
        clear()
    else:
        pass

    if checkforadmin() and os.path.isfile("pypresence.txt") is True:
        with open("pypresence.txt", "r", encoding="utf-8") as pypresence_signal_read:
            if pypresence_signal_read.read() == "pypresence installus":
                os.system("pip install pypresence")
            else:
                print("bruh")
        os.remove("pypresence.txt")
        continue1()
        clear()
    else:
        pass

    if checkforadmin() and os.path.isfile("update.txt") is True:
        with open("update.txt", "r", encoding="utf-8") as update_signal_read:
            if update_signal_read.read() == "updatus":
                os.system("animdl update")
            else:
                print("bruh")
        os.remove("update.txt")
        continue1()
        clear()
    else:
        pass


    if doespackageexist("animdl") is True:
        pass

    else:
        print("Whoops, doesn't look like you have animdl installed.")
        print("Please install it manually or by pressing enter. Thanks")
        continue1()
        if os.path.isfile("animdl.txt") is True:
            print("Seems like you encountered a bug. Please report it to me on github.com")
        else:
            with open("animdl.txt", "a", encoding="utf-8") as animdl_signal:
                animdl_signal.write("animdl installus")
                print("animdl will try to install on next startup of animdl-tui")
            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                sys.executable,
                " ".join(sys.argv),
                None,
                1
            )

            sys.exit()

    if doespackageexist("pypresence") is True and ismoduleon(
        ANIMDL_CONFIG,
        "discord_presence"
        ) is True:
        pass

    elif doespackageexist("pypresence") is False and ismoduleon(
        ANIMDL_CONFIG,
        "discord_presence"
        ) is True:
        print("Whoops, doesn't look like you have pypresence installed.")
        print("Please install it manually or by pressing enter. Thanks")
        continue1()
        if os.path.isfile("pypresence.txt") is True:
            print("Seems like you encountered a bug. Please report it to me on github.com")
        else:
            with open("pypresence.txt", "a", encoding="utf-8") as pypresence_signal:
                pypresence_signal.write("pypresence installus")
                print("pypresence will try to install on next startup of animdl-tui")
            ctypes.windll.shell32.ShellExecuteW(
                None,
                "runas",
                sys.executable,
                " ".join(sys.argv),
                None,
                1
            )
            sys.exit()
    else:
        pass
    clear()
    main()

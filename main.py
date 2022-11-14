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

ANIMDL_CONFIG = "animdl_config.yml"
CONFIG_FILE = "config.yml"

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

randomcolors = random.choice(randcolors)

ANIMDL = "[animdl-tui]"

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
    def special():
        cursor.hide()
        randomnumber = random.randint(0, 1000)
        print(
            f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
            print(
                f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
        print(
            f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
            print(
                f"{bold}{randomcolors}{ANIMDL}\n{reset}")
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
                    tui_config['toggles']['range'] = f'{specific_range_input_result}'
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
        print(
            f"{bold}{randomcolors}{ANIMDL}\n{reset}")
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
            print(
                f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
        print(
            f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
            print(
                f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
        print(
            f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
            print(
                f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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

        print(
            f"{bold}{randomcolors} {ANIMDL}\n{reset}")
        modules = Bullet(
            prompt = f"{cyan} Toggle modules: {reset} \n",
            choices = [
                f'{qualitychoice}',
                f'{dirchoice}',
                f'{rangechoice}',
                f'{specialchoice}',
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

    def directory():
        cursor.hide()
        print(
            f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
            print(
                f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
    print(f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
        match sys.platform:
            case 'win32':
                if is_admin():
                    os.system("animdl update")
                    os.system("pause")

                else:
                    # Re-run the program with admin rights
                    ctypes.windll.shell32.ShellExecuteW(
                        None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                    os.system(f"powershell.exe {__file__}")

            case _:
                print("I can't test this with anything but windows rn.",
                    "Run \'sudo animdl update to update or whatever.\'")
                sys.exit()

    def web():
        cursor.hide()
        app = Flask(__name__)

        @app.route("/")
        def index():
            return render_template('index.html')

        @app.route("/")
        def backend():
            """empty"""
            return 0

        @app.route("/download")
        def download():
            """empty"""
            return 0

        @app.route("/stream")
        def stream():
            """empty"""
            return 0

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

        print(f"{bold}{randomcolors} {ANIMDL}\n{reset}")

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
        os.system(f'animdl stream'
                f'{specialarg} {rangearg} {qualityarg} "{provider}:{streamus.result}"')
        clear()
        print(f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
        search = Input(
            prompt = f"{cyan} Enter anime name.\n {red}:{reset} ",
            indent = 0
        )
        search.result = search.launch()
        os.system(f'animdl search -p {provider} "{search.result}"')
        clear()
        print(f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
        print(f"{bold}{randomcolors} {ANIMDL}\n{reset}")
        print(f"{cyan} Schedule: {reset}")
        os.system("animdl schedule")
        continue1()
        c_m()

    def grab():
        cursor.hide()
        with open(CONFIG_FILE, 'r', encoding="utf-8") as configfile_read:
            tui_config = y.safe_load(configfile_read)
        provider = tui_config['modifiers']['provider']
        grab = Input(
            prompt = f"{cyan} Enter anime name.\n {red}:{reset} ",
            indent = 0
        )
        grab.result = grab.launch()
        os.system(f'animdl grab "{provider}:{grab.result}"')
        clear()
        print(f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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

        print(f"{bold}{randomcolors} {ANIMDL}\n{reset}")

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
        os.system(f'animdl download'
                f'{specialarg} {rangearg} {qualityarg} {directoryarg} '
                f'"{provider}:{downloadus.result}"')
        clear()
        print(f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
        print(
            f"{bold}{randomcolors} {ANIMDL}\n{reset}")
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
                '- Web     ',
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
            case '- Web     ':
                clear()
                web()
            case '- Exit    ':
                clear()
                sys.exit()
    menu()

if __name__ == '__main__':
    clear()
    cursor.hide()
    def is_admin():
        """if the user is administrator"""
        if sys.platform == 'win32':
            return ctypes.windll.shell32.IsUserAnAdmin()

    python_path = os.path.dirname(sys.executable)
    if os.path.exists(python_path) is True:
        animdl_path = os.path.join(python_path,"Scripts\\animdl.exe")
        if os.path.isfile(animdl_path) is True:
            pass

        else:
            if is_admin():
                os.system("pip install animdl")
            print("Whoops, doesn't look like you have animdl installed.")
            print("Please install it manually or by pressing enter. Thanks")
            continue1()

            if is_admin():
                os.system("pip install animdl")
                sys.exit()

            else:
                # Re-run the program with admin rights
                ctypes.windll.shell32.ShellExecuteW(None,
                "runas", sys.executable, " ".join(sys.argv), None, 1)
    else:
        print("How the fuck are you running this")

    if is_admin():
        os.system("animdl update")
        sleep(2)
        sys.exit()

    ctypes.windll.kernel32.SetConsoleTitleW("animdl-tui")
    main()

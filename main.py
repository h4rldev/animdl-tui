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

CONFIG_FILE = "config.yml"
with open(CONFIG_FILE, 'r') as configfile:
    tui_config = y.safe_load(configfile)


cyan = fg("cyan")
reset = attr("reset")
bold = attr("bold")
green = fg("green")
red = fg("red")

ANIMDL1 = "    ___    _   ________  _______  __       ________  ______"
ANIMDL2 = "   /   |  / | / /  _/  |/  / __ \/ /      /_  __/ / / /  _/"
ANIMDL3 = "  / /| | /  |/ // // /|_/ / / / / /  ______/ / / / / // /  "
ANIMDL4 = " / ___ |/ /|  // // /  / / /_/ / /__/_____/ / / /_/ // /   "
ANIMDL5 = "/_/  |_/_/ |_/___/_/  /_/_____/_____/    /_/  \____/___/ "

def continue1():
    print("\n Press any key to continue")
    getkey()

def thesettings(settings):
    def special(special_range):
        randomnumber = random.randint(0, 1000)
        print(f"{bold}{cyan}{ANIMDL1}\n{ANIMDL2}\n{ANIMDL3}\n{ANIMDL4}\n{ANIMDL5}\n{reset}");
        special_range = Bullet(
            prompt=f"{bold}         Are you sure you want a special range? {reset} \n",
            choices=[
                f'- {green}YES {colors.foreground["default"]}',
                f'- {red}NO  {colors.foreground["default"]}',
            ],
            bullet="",
            margin = 0,
            align = 22,
            word_on_switch=colors.foreground["white"],
            background_on_switch=colors.background["cyan"]
        )
        result = special_range.launch()
        if result == f"- {green}YES {colors.foreground['default']}":
            clear();
            print(f"{bold}{cyan}{ANIMDL1}\n{ANIMDL2}\n{ANIMDL3}\n{ANIMDL4}\n{ANIMDL5}\n{reset}");
            special_range_input = Input(
                prompt=f"{bold}     Specify a special range. (Example: \"latest-{randomnumber}\"){reset} \n\n        : ",
                word_color=colors.foreground['cyan'],
                pattern="latest-"
            )

            special_range_input_result = special_range_input.launch()
            if tui_config['toggles']['special'] is True:
                print(f"The SPECIAL RANGE MODULE is now {special_range_input_result}")
                tui_config['modifiers']['special'] = f'{special_range_input_result}'
                with open(CONFIG_FILE, 'w') as configfile:
                    y.dump(tui_config, configfile)
                    sleep(1)
                    clear();
                    return

            else:
                print(f"The SPECIAL RANGE MODULE is FALSE")
                special_toggle = Bullet(
                    prompt=f"{bold}        Would you like to enable the SPECIAL RANGE MODULE? {reset} \n",
                    choices=[
                        f'- {green}YES {colors.foreground["default"]}',
                        f'- {red}NO  {colors.foreground["default"]}',
                    ],
                    bullet="",
                    margin = 0,
                    align = 22,
                    word_on_switch=colors.foreground["white"],
                    background_on_switch=colors.background["cyan"]
                )
                special_toggle_result = special_toggle.launch()
                if special_toggle_result == f"- {green}YES {colors.foreground['default']}":
                    print("The SPECIAL RANGE MODULE is now True")
                    tui_config['toggles']['special'] = True
                    with open(file, 'w') as configfile:
                        y.dump(tui_config, configfile)
                    print(f"The SPECIAL RANGE MODULE is now {special_range_input_result}")
                    tui_config['modifiers']['range'] = f'{special_range_input_result}'
                    with open(file, 'w') as configfile:
                        y.dump(tui_config, configfile)
                    clear();
                    thesettings()
                else:
                    clear();
                    print("Ok! returning...")
                    thesettings()
        else:
            clear();
            print("Ok! returning...")
            thesettings();

        def therange():
            randomnumber = random.randint(0, 1000)
            print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
            specific_range = Bullet(
                prompt=f"{bold}         Are you sure you want a specific range? {reset} \n",
                choices=[
                    f'- {green}YES {colors.foreground["default"]}',
                    f'- {red}NO  {colors.foreground["default"]}',
                ],
                bullet="",
                margin = 0,
                align = 22,
                word_on_switch=colors.foreground["white"],
                background_on_switch=colors.background["cyan"]
            )
            result = specific_range.launch()
            if result == f"- {green}YES {colors.foreground['default']}":
                clear();
                print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
                specific_range_input = Input(
                    prompt=f"{bold}     Specify a range. (Example: \"{randomnumber}-{randomnumber}\"){reset} \n\n        : ",
                    word_color=colors.foreground['cyan'],
                )

                specific_range_input_result = specific_range_input.launch()
                if tui_config['toggles']['range'] == True:
                    print(f"The RANGE MODULE is now {specific_range_input_result}")
                    tui_config['modifiers']['range'] = f'{specific_range_input_result}'
                    with open(file, 'w') as configfile:
                        y.dump(tui_config, configfile)
                    sleep(1)
                    clear();
                    thesettings();

                else:
                    print(f"The RANGE MODULE is FALSE")
                    specific_range_toggle = Bullet(
                        prompt=f"{bold}        Would you like to enable the RANGE MODULE? {reset} \n",
                        choices=[
                            f'- {green}YES {colors.foreground["default"]}',
                            f'- {red}NO  {colors.foreground["default"]}',
                        ],
                        bullet="",
                        margin = 0,
                        align = 22,
                        word_on_switch=colors.foreground["white"],
                        background_on_switch=colors.background["cyan"]
                    )
                    specific_range_toggle_result = specific_range_toggle.launch()
                    if specific_range_toggle_result == f"- {green}YES {colors.foreground['default']}":
                        print("The RANGE MODULE is now True")
                        tui_config['toggles']['range'] = True
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        print(f"The RANGE MODULE is now {specific_range_input_result}")
                        tui_config['toggles']['range'] = f'{specific_range_input_result}'
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        sleep(1)
                        clear();
                        thesettings();
                    else:
                        clear();
                        print("Ok! returning...")
                        thesettings();

        def quality():
            print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
            quality = Bullet(
                prompt=f"{bold}         Are you sure you want a specific quality? {reset} \n",
                choices=[
                    f'- {green}YES {colors.foreground["default"]}',
                    f'- {red}NO  {colors.foreground["default"]}',
                ],
                bullet="",
                margin = 0,
                align = 22,
                word_on_switch=colors.foreground["white"],
                background_on_switch=colors.background["cyan"]
            )
            result = quality.launch()
            if result == f"- {green}YES {colors.foreground['default']}":
                clear();
                print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
                quality_input = Input(
                    prompt=f"{bold}     Specify a quality. (Examples: \"1080/best\", \"1080/worst\", \"best[title]\", \"best[title=r'^DUB']\"){reset} \n\n        : ",
                    word_color=colors.foreground['cyan']
                )

                quality_input_result = quality_input.launch()
                if tui_config['toggles']['quality'] == True:
                    print(f"The QUALITY MODULE is now {quality_input_result}")
                    tui_config['toggles']['quality'] = f'{quality_input_result}'
                    with open(file, 'w') as configfile:
                        y.dump(tui_config, configfile)
                    sleep(1)
                    clear();
                    thesettings();

                else:
                    print(f"The QUALITY MODULE is FALSE")
                    quality_toggle = Bullet(
                        prompt=f"{bold}        Would you like to enable the QUALITY MODULE? {reset} \n",
                        choices=[
                            f'- {green}YES {colors.foreground["default"]}',
                            f'- {red}NO  {colors.foreground["default"]}',
                        ],
                        bullet="",
                        margin = 0,
                        align = 22,
                        word_on_switch=colors.foreground["white"],
                        background_on_switch=colors.background["cyan"]
                    )
                    quality_toggle_result = quality_toggle.launch()
                    if quality_toggle_result == f"- {green}YES {colors.foreground['default']}":
                        print("The QUALITY MODULE is now True")
                        tui_config['toggles']['quality'] = True
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        print(f"The QUALITY MODULE is now {quality_input_result}")
                        tui_config['toggles']['quality'] = f'{quality_input_result}'
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        sleep(1)
                        clear();
                        thesettings();
                    else:
                        clear();
                        print("Ok! returning...")
                        thesettings();

        def player():
            file = "animdl_config.yml"
            print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
            player = Bullet(
                prompt=f"{bold}         Are you sure you want to switch to a different player? (default: mpv) {reset} \n",
                choices=[
                    f'- {green}YES {colors.foreground["default"]}',
                    f'- {red}NO  {colors.foreground["default"]}',
                ],
                bullet="",
                margin = 0,
                align = 22,
                word_on_switch=colors.foreground["white"],
                background_on_switch=colors.background["cyan"]
            )
            result = player.launch()
            if result == f"- {green}YES {colors.foreground['default']}":
                clear();
                print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
                player_choice = Bullet(
                    prompt=f"{bold}     Choose a player. {reset} \n",
                    choices=[
                        '- mpv (default)  ',
                        '- vlc            ',
                        '- ffplay (ffmpeg)',
                        '- exit           '
                    ],
                    bullet="",
                    margin = 0,
                    align = 22,
                    word_on_switch=colors.foreground["white"],
                    background_on_switch=colors.background["cyan"]
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

                        print("mpv should now be the selected player.")

                        with open(file, 'w') as ymlconfig:
                            y.dump(data, ymlconfig)
                        sleep(1)
                        thesettings();

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

                        print("vlc should now be the selected player.")

                        with open(file, 'w') as ymlconfig:
                            y.dump(data, ymlconfig)
                        sleep(1)
                        thesettings();


                    case '- ffplay (ffmpeg)':
                        data = {
                            "default_player": "ffplay",
                            "players": {
                                "ffplay":{
                                    "executable": "ffplay",
                                    "opts": []
                                }
                            }
                        }

                        print("ffplay should now be the selected player.")

                        with open(file, 'w') as ymlconfig:
                            y.dump(data, ymlconfig)
                        sleep(1)
                        thesettings();

                    case '- exit           ':
                        clear();
                        thesettings();

            else:
                clear();
                thesettings();

        def provider():
            print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
            provider = Bullet(
                prompt=f"{bold}         Are you sure you want to switch to a different provider? (default: animixplay) {reset} \n",
                choices=[
                    f'- {green}YES {colors.foreground["default"]}',
                    f'- {red}NO  {colors.foreground["default"]}',
                ],
                bullet="",
                margin = 0,
                align = 22,
                word_on_switch=colors.foreground["white"],
                background_on_switch=colors.background["cyan"]
            )
            result = provider.launch()
            if result == f"- {green}YES {colors.foreground['default']}":
                clear();
                print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
                provider_choice = Bullet(
                    prompt=f"{bold}     Choose a provider (sorted by latency). {reset} \n",
                    choices=[
                        '- animixplay (default)',
                        '- animepahe           ',
                        '- haho (NSFW)         ',
                        '- gogoanime           ',
                        '- tenshi.moe          ',
                        '- allanime            ',
                        '- exit                '
                    ],
                    bullet="",
                    margin = 0,
                    align = 22,
                    word_on_switch=colors.foreground["white"],
                    background_on_switch=colors.background["cyan"]
                )
                provider_choice_result = provider_choice.launch()

                match provider_choice_result:

                    case '- animixplay (default)':
                        print("The provider has now been set to animixplay.")
                        tui_config['modifiers']['provider'] = 'animixplay'
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        sleep(1)
                        clear();
                        thesettings();

                    case '- animepahe           ':
                        print("The provider has now been set to animepahe.")
                        tui_config['modifiers']['provider'] = 'animepahe'
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        sleep(1)
                        clear();
                        thesettings();

                    case '- haho (NSFW)         ':
                        print("The provider has now been set to haho (NSFW).")
                        tui_config['modifiers']['provider'] = 'haho'
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        sleep(1)
                        clear();
                        thesettings();

                    case '- gogoanime           ':
                        print("The provider has now been set to gogoanime.")
                        tui_config['modifiers']['provider'] = 'gogoanime'
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        sleep(1)
                        clear();
                        thesettings();

                    case '- tenshi.moe          ':
                        print("The provider has now been set to tenshi.moe.")
                        tui_config['modifiers']['provider'] = 'tenshi'
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        sleep(1)
                        clear();
                        thesettings();

                    case '- allanime            ':
                        print("The provider has now been set to allanime.")
                        tui_config['modifiers']['provider'] = 'allanime'
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        sleep(1)
                        clear();
                        thesettings();

                    case '- exit                ':
                        clear();
                        thesettings();

        def toggle():
            clear();

            if tui_config['toggles']['special'] == False:
                specialstatus = 'False'
                specialstatuscolor = red
            else:
                specialstatus = 'True'
                specialstatuscolor = green

            if tui_config['toggles']['range'] == False:
                rangestatus = 'False'
                rangestatuscolor = red
            else:
                rangestatus = 'True'
                rangestatuscolor = green

            if tui_config['toggles']['quality'] == False:
                qualitystatus = 'False'
                qualitystatuscolor = red
            else:
                qualitystatus = 'True'
                qualitystatuscolor = green

            qualitychoice = f'- Quality = {qualitystatuscolor}{qualitystatus:5}'
            rangechoice = f'- Range = {rangestatuscolor}{rangestatus:5}'
            specialchoice = f'- Special = {specialstatuscolor}{specialstatus:5}'

            print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
            modules = Bullet(
                prompt = f"{bold}                     Toggle modules: {reset} \n",
                choices = [
                    f'{qualitychoice}',
                    f'{rangechoice}',
                    f'{specialchoice}',
                    f'- Exit    '
                ],
                bullet = "",
                margin = 0,
                align = 20,
                word_on_switch=colors.foreground["white"],
                background_on_switch=colors.background["cyan"]
            )
            result = modules.launch()

            if result == qualitychoice:
                result = 0
            elif result == rangechoice:
                result = 1
            elif result == specialchoice:
                result = 2

            match result:
                case '- Exit    ':
                    clear();
                    thesettings();

                case 0:
                    if tui_config['toggles']['quality'] == True:
                        print("The QUALITY MODULE is now False")
                        tui_config['toggles']['quality'] = False
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        toggle();
                    else:
                        print("The QUALITY MODULE is now True")
                        tui_config['toggles']['quality'] = True
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        toggle();
                case 1:
                    if tui_config['toggles']['range'] == True:
                        print("The RANGE MODULE is now False")
                        tui_config['toggles']['range'] = False
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        toggle();
                    else:
                        print("The RANGE MODULE is now True")
                        tui_config['toggles']['range'] = True
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        toggle();
                case 2:
                    if tui_config['toggles']['special'] == True:
                        print("The SPECIAL RANGE MODULE is now False")
                        tui_config['toggles']['special'] = False
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        toggle();
                    else:
                        print("The SPECIAL RANGE MODULE is now True")
                        tui_config['toggles']['special'] = True
                        with open(file, 'w') as configfile:
                            y.dump(tui_config, configfile)
                        toggle();

    clear();
    print(f"{bold}{cyan}{ANIMDL_LOGO1}\n{ANIMDL_LOGO2}\n{ANIMDL_LOGO3}\n{ANIMDL_LOGO4}\n{ANIMDL_LOGO5}\n{reset}");
    settings = Bullet(
        prompt = f"{bold}                       Settings:  {reset} \n",
        choices = [
            '- Toggle  ',
            '- Provider',
            '- Player  ',
            '- Quality ',
            '- Range   ',
            '- Special ',
            '- Exit    '
        ],
        bullet = "",
        margin = 0,
        align = 22,
        word_on_switch=colors.foreground["white"],
        background_on_switch=colors.background["cyan"]
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
        case '- Exit    ':
            clear()
            menu()
    
def main():
    def update():
        match sys.platform:
            case 'win32':
                def is_admin():
                    try:
                        return ctypes.windll.shell32.IsUserAnAdmin()
                    except:
                        return False
                if is_admin():
                    os.system("animdl update")
                    os.system("pause")

                else:
                    # Re-run the program with admin rights
                    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
                    os.system(f"powershell.exe {__file__}")

            case _:
                print("I can't test this with anything but windows rn.",
                "Run \'sudo animdl update to update or whatever.\'")
                sys.exit();

    def web(app):
        app = Flask(__name__)
        @app.route("/")
        def index():
            return render_template('index.html')
        print("big sex")

        app.run()

    def stream():
        getkey()

    def search():
        getkey()

    def schedule():
        getkey()

    def grab():
        getkey()

    def download():
        getkey()

    def menu():
        cursor.hide()
        print(f"{bold}{cyan}{ANIMDL1}\n{ANIMDL2}\n{ANIMDL3}\n{ANIMDL4}\n{ANIMDL5}\n{reset}")
        menu = Bullet(
            prompt = f"{bold}                       Main Menu:  {reset} \n",
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
            align = 22,
            word_on_switch=colors.foreground["white"],
            background_on_switch=colors.background["cyan"]
        )

        result = menu.launch()

        match result:
            case '- Download':
                clear();
                download();
            case '- Stream  ':
                clear();
                stream();
            case '- Search  ':
                clear();
                search();
            case '- Schedule':
                clear();
                schedule();
            case '- Grab    ':
                clear();
                grab();
            case '- Update  ':
                clear();
                update();
            case '- Settings':
                clear();
                thesettings();
            case '- Web     ':
                clear();
                web();
            case '- Exit    ':
                clear();
                exit;
    menu();

if __name__ == '__main__':
    clear();

    def is_admin():
        if sys.platform == 'win32':
            return ctypes.windll.shell32.IsUserAnAdmin()


    if is_admin():
        os.system("animdl update");
        sleep(2)
        sys.exit();

    ctypes.windll.kernel32.SetConsoleTitleW("animdl-tui")
    main();
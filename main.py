import sys, platform, os, ctypes, cursor, random
from time import sleep
from colored import fg, attr
from bullet import Bullet, Input, colors
from msvcrt import getch as getkey
from click import clear
from configparser import ConfigParser
import yaml as y

cyan = fg("cyan")
reset = attr("reset")
bold = attr("bold")
green = fg("green")
red = fg("red")

animdl1 = "    ___    _   ________  _______  __       ________  ______"
animdl2 = "   /   |  / | / /  _/  |/  / __ \/ /      /_  __/ / / /  _/"
animdl3 = "  / /| | /  |/ // // /|_/ / / / / /  ______/ / / / / // /  "
animdl4 = " / ___ |/ /|  // // /  / / /_/ / /__/_____/ / / /_/ // /   "
animdl5 = "/_/  |_/_/ |_/___/_/  /_/_____/_____/    /_/  \____/___/ "

def continue1():
    print("\n Press any key to continue");
    getkey();

def main():
    def special():
        file = "config.ini"
        config = ConfigParser()
        config.read(file)
        randomnumber = random.randint(0, 1000)
        print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
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
        if result == f"- {green}YES {colors.foreground['default']}-":
            clear();
            print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
            special_range_input = Input(
                prompt=f"{bold}     Specify a special range. (Example: \"latest-{randomnumber}\"){reset} \n\n        : ",
                word_color=colors.foreground['cyan'],
                pattern="latest-"
            )

            special_range_input_result = special_range_input.launch()
            if config['toggles']['special'] == 'True':
                print(f"The SPECIAL RANGE MODULE is now {special_range_input_result}")
                config.set('modifiers', 'special', f'{special_range_input_result}')
                with open(file, 'w') as configfile:
                    config.write(configfile)
                sleep(1)
                clear();
                thesettings();

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
                    config.set('toggles', 'special', 'True')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    print(f"The SPECIAL RANGE MODULE is now {special_range_input_result}")
                    config.set('modifiers', 'special', f'{special_range_input_result}')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    sleep(1)
                    clear();
                    thesettings();
                else:
                    clear();
                    print("Ok! returning...")
                    thesettings();
        else:
            clear();
            print("Ok! returning...")
            thesettings();

    def range():
        file = "config.ini"
        config = ConfigParser()
        config.read(file)
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
            if config['toggles']['range'] == 'True':
                print(f"The RANGE MODULE is now {specific_range_input_result}")
                config.set('modifiers', 'range', f'{specific_range_input_result}')
                with open(file, 'w') as configfile:
                    config.write(configfile)
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
                    config.set('toggles', 'range', 'True')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    print(f"The RANGE MODULE is now {specific_range_input_result}")
                    config.set('modifiers', 'range', f'{specific_range_input_result}')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    sleep(1)
                    clear();
                    thesettings();
                else:
                    clear();
                    print("Ok! returning...")
                    thesettings();

    def quality():
        file = "config.ini"
        config = ConfigParser()
        config.read(file)
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
            if config['toggles']['quality'] == 'True':
                print(f"The QUALITY MODULE is now {quality_input_result}")
                config.set('modifiers', 'quality', f'{quality_input_result}')
                with open(file, 'w') as configfile:
                    config.write(configfile)
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
                    config.set('toggles', 'quality', 'True')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    print(f"The QUALITY MODULE is now {quality_input_result}")
                    config.set('modifiers', 'quality', f'{quality_input_result}')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
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
        file = 'config.ini'
        config = ConfigParser()
        config.read(file)
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
                    config.set('modifiers', 'provider', 'animixplay')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    sleep(1)
                    clear();
                    thesettings();

                case '- animepahe           ':
                    print("The provider has now been set to animepahe.")
                    config.set('modifiers', 'provider', 'animepahe')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    sleep(1)
                    clear();
                    thesettings();

                case '- haho (NSFW)         ':
                    print("The provider has now been set to haho (NSFW).")
                    config.set('modifiers', 'provider', 'haho')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    sleep(1)
                    clear();
                    thesettings();

                case '- gogoanime           ':
                    print("The provider has now been set to gogoanime.")
                    config.set('modifiers', 'provider', 'gogoanime')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    sleep(1)
                    clear();
                    thesettings();

                case '- tenshi.moe          ':
                    print("The provider has now been set to tenshi.moe.")
                    config.set('modifiers', 'provider', 'tenshi')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    sleep(1)
                    clear();
                    thesettings();

                case '- allanime            ':
                    print("The provider has now been set to allanime.")
                    config.set('modifiers', 'provider', 'allanime')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    sleep(1)
                    clear();
                    thesettings();

                case '- exit                ':
                    clear();
                    thesettings();

    def toggle():
        clear();
        file = "config.ini"
        config = ConfigParser()
        config.read(file)

        if config['toggles']['provider'] == 'False':
            providerstatuscolor = red
        else:
            providerstatuscolor = green

        if config['toggles']['special'] == 'False':
            specialstatuscolor = red
        else:
            specialstatuscolor = green

        if config['toggles']['range'] == 'False':
            rangestatuscolor = red
        else:
            rangestatuscolor = green

        if config['toggles']['quality'] == 'False':
            qualitystatuscolor = red
        else:
            qualitystatuscolor = green

        print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");

        print("               +-----------------------+")
        print(f"               | PROVIDER      ={providerstatuscolor} {config['toggles']['provider']:5} {reset}|")
        print(f"               | QUALITY       ={qualitystatuscolor} {config['toggles']['quality']:5} {reset}|")
        print(f"               | RANGE         ={rangestatuscolor} {config['toggles']['range']:5} {reset}|")
        print(f"               | SPECIAL RANGE ={specialstatuscolor} {config['toggles']['special']:5} {reset}|")
        print("               +-----------------------+")
        modules = Bullet(
            prompt = f"{bold}                     Toggle modules: {reset} \n",
            choices = [
                '- Provider',
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
        result = modules.launch()
        match result:
            case '- Provider':
                if config['toggles']['provider'] == 'True': # planning to switch to yaml
                    print("The PROVIDER MODULE is now False")
                    config.set('toggles', 'provider', 'False')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    toggle();
                else:
                    print("The PROVIDER MODULE is now True")
                    config.set('toggles', 'provider', 'True')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    toggle();
            case '- Quality ':
                if config['toggles']['quality'] == 'True':
                    print("The QUALITY MODULE is now False")
                    config.set('toggles', 'quality', 'False')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    toggle();
                else:
                    print("The QUALITY MODULE is now True")
                    config.set('toggles', 'quality', 'True')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    toggle();
            case '- Range   ':
                if config['toggles']['range'] == 'True':
                    print("The RANGE MODULE is now False")
                    config.set('toggles', 'range', 'False')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    toggle();
                else:
                    print("The RANGE MODULE is now True")
                    config.set('toggles', 'range', 'True')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    toggle();
            case '- Special ':
                if config['toggles']['special'] == 'True':
                    print("The SPECIAL RANGE MODULE is now False")
                    config.set('toggles', 'special', 'False')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    toggle();
                else:
                    print("The SPECIAL RANGE MODULE is now True")
                    config.set('toggles', 'special', 'True')
                    with open(file, 'w') as configfile:
                        config.write(configfile)
                    toggle();
            case '- Exit    ':
                clear();
                thesettings();

    def thesettings():
        clear();
        print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
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
                clear();
                toggle();
            case '- Provider':
                clear();
                provider();
            case '- Player  ':
                clear();
                player();
            case '- Quality ':
                clear();
                quality();
            case '- Range   ':
                clear();
                range();
            case '- Special ':
                clear();
                special();
            case '- Exit    ':
                clear();
                menu();

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
                    os.system("powershell.exe %s" % (__file__))

            case _:
                print("I can't test this with anything but windows rn.",
                "Run \'sudo animdl update to update or whatever.\'")
                exit();

    def stream():
        getkey();

    def search():
        getkey();

    def schedule():
        getkey();

    def grab():
        getkey();

    def download():
        getkey();

    def menu():
        def is_admin():
            if sys.platform == 'win32':
                try:
                    return ctypes.windll.shell32.IsUserAnAdmin()
                except:
                    return False

        cursor.hide();
        if is_admin():
            os.system("animdl update");
            os.system("pause")
            clear();
        print(f"{bold}{cyan}{animdl1}\n{animdl2}\n{animdl3}\n{animdl4}\n{animdl5}\n{reset}");
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
                print("empty rn")
                main();
            case '- Exit    ':
                clear();
                exit;
    menu();

if __name__ == '__main__':
    clear();
    ctypes.windll.kernel32.SetConsoleTitleW("animdl-tui")
    main();
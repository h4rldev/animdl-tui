"""for administrator powers"""
import ctypes
import os
import random
import sys

from time import sleep

from modules.default_configs import ANIMDL_DEFAULT, CONFIG_DEFAULT
from modules.checks import doespackageexist, ismoduleon, checkifexists, checkiffalse
from modules.colors import cyan, green, red, yellow, blue, orange, purple, reset, bold
import cursor
import readchar
import yaml as y
from bullet import Bullet, Input, colors
from click import clear

if sys.platform == "win32":
    # trunk-ignore(pylint/E0401)
    from msvcrt import getch as getkey
else:
    import getch as getkey


__version__ = "0.0.3"

EXECUTABLE: str = os.path.basename(sys.executable)
ANIMDL: str = "[animdl-tui]"

randcolors = [cyan, green, red, blue, orange, purple, yellow]

def confirmation(conf_prompt: str, choice1: str, choice2: str, color1=green, color2=red) -> bool:
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
    if value == "":
        config[tree] = f"{key}"
    else:
        config[tree][key] = f"{value}"

    with open(file, "w", encoding="utf-8") as buffer:
        y.dump(config, buffer)


def randcolforname(name):
    """Randomly changes the color of a string based on an array of values"""
    randomcolors = random.choice(randcolors)
    print(f"{bold}{randomcolors} {name}\n{reset}")


def continue1():
    """Continue function"""
    print("\n Press any key to continue")
    getkey()

def thesettings():
    """settings function"""
    try:
        cursor.hide()
        with open("config.yml", "r", encoding="utf-8") as configfile_read:
            tui_read_config = y.safe_load(configfile_read)
        with open("animdl_config.yml", "r", encoding="utf-8") as animdl_config_read:
            animdl_read_config = y.safe_load(animdl_config_read)

        def _special():
            settings_special_status = checkiffalse(tui_read_config, "special")
            cursor.hide()
            randomnumber = random.randint(0, 1000)
            randcolforname("[animdl-tui]")
            special = confirmation(
                f"{cyan} Are you sure you want a special range? {reset} \n"
                f" {settings_special_status}\n",
                "Yes",
                "No"
            )
            if special:
                clear()
                randcolforname("[animdl-tui]")
                special_input = Input(
                    prompt=(
                        f"{cyan} Specify a special range.{reset}"
                        f' (Example: "latest-{randomnumber}")\n'
                        f" {red}:{reset} "
                    ),
                    pattern="latest-",
                )

                special_input_result = special_input.launch()
                if tui_read_config["modifiers"]["special"] is True:
                    print(f" ´SPECIAL RANGE´ is now '{special_input_result}'")
                    write_to_config(
                        "config.yml",
                        tui_read_config,
                        "modifiers",
                        "special",
                        special_input_result
                    )
                    continue1()
                    thesettings()

                else:
                    print(" ´SPECIAL RANGE´ is False")
                    special_toggle = confirmation(
                        f"{cyan} Would you like to enable ´SPECIAL RANGE´? {reset} \n",
                        "Yes",
                        "No"
                    )
                    if special_toggle:
                        print(" ´SPECIAL RANGE´ is now True")
                        write_to_config("config.yml", tui_read_config, "toggles", "special", True)
                        print(f" ´SPECIAL RANGE´ is now '{special_input_result}'")
                        write_to_config(
                            "config.yml",
                            tui_read_config,
                            "modifiers",
                            "special",
                            special_input_result
                        )
                        sleep(1)
                        cts()
                    else:
                        cpts()
            else:
                cpts()

        def _range():
            settings_range_status = checkiffalse(tui_read_config, "range")
            cursor.hide()
            randomnumber = random.randint(0, 1000)
            randcolforname("[animdl-tui]")
            _range = confirmation(
                f"{cyan} Are you sure you want a range? {reset} \n"
                f" {settings_range_status}\n",
                "Yes",
                "No"
            )
            if _range:
                clear()
                randcolforname("[animdl-tui]")
                range_input = Input(
                    prompt=(
                        f"{cyan}Specify a range.{reset}"
                        f' (Example: "{randomnumber}-{randomnumber}")'
                        f"\n {red}:{reset} "
                    ),
                )

                range_input_result = range_input.launch()
                if tui_read_config["toggles"]["range"] is True:
                    print(f"´RANGE´ is now {range_input_result}")
                    write_to_config(
                        "config.yml",
                        tui_read_config,
                        "modifiers",
                        "range",
                        range_input_result
                    )
                    sleep(1)
                    cts()

                else:
                    print("´RANGE´ is False")
                    range_toggle = confirmation(
                        f"{cyan} Would you like to enable ´RANGE´? {reset} \n",
                        "Yes",
                        "No"
                    )
                    if range_toggle:
                        print(" ´RANGE´ is now True")
                        write_to_config(
                            "config.yml",
                            tui_read_config,
                            "toggles",
                            "range",
                            range_input_result
                        )
                        print(f" ´RANGE´ is now {range_input_result}")
                        write_to_config (
                            "config.yml",
                            tui_read_config,
                            "modifiers",
                            "range",
                            range_input_result
                        )
                        sleep(1)
                        cts()
                    else:
                        cpts()
            else:
                cpts()

        def quality():
            settings_quality_status = checkiffalse(tui_read_config, "quality")
            cursor.hide()
            randcolforname("[animdl-tui]")
            quality = confirmation(
                f"{cyan} Are you sure you want a specific quality? {reset} \n"
                f" {settings_quality_status}\n",
                "Yes",
                "No"
            )
            if quality:
                clear()
                randcolforname("[animdl-tui]")
                quality_input = Input(
                    prompt=(
                        f"{cyan} Specify a quality.{reset}"
                        f" (Examples: '1080', '1080/best', '1080/worst',"
                        f" 'best[title]', 'best[title=r'^DUB']')"
                        f"\n {red}:{reset} "
                    ),
                )
                quality_input_result = quality_input.launch()
                if tui_read_config["toggles"]["quality"] is True:
                    print(f" ´QUALITY´ is now {quality_input_result}")
                    tui_read_config["modifiers"]["quality"] = f"{quality_input_result}"
                    with open("config.yml", "w", encoding="utf-8") as configfile_write:
                        y.dump(tui_read_config, configfile_write)
                    sleep(1)
                    cts()
                else:
                    print(" ´QUALITY´ is False")
                    quality_toggle = confirmation(
                        f"{cyan} Would you like to enable ´QUALITY´? {reset} \n",
                        "Yes",
                        "No"
                    )
                    if quality_toggle:
                        print(" ´QUALITY´ is now True")
                        tui_read_config["toggles"]["quality"] = True
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                            print(f" ´QUALITY´ is now {quality_input_result}")
                            tui_read_config["modifiers"][
                                "quality"
                            ] = f"{quality_input_result}"
                            with open(
                                "config.yml", "w", encoding="utf-8"
                            ) as configfile_write:
                                y.dump(tui_read_config, configfile_write)
                                sleep(1)
                                cts()
                    else:
                        cpts()
            else:
                cpts()

        def player():
            settings_player_status = checkiffalse(animdl_read_config, "default_player")
            cursor.hide()
            randcolforname("[animdl-tui]")
            player = confirmation(
                (
                    f"{cyan}"
                    f" Are you sure you want to switch to a different player?{reset}"
                    f" \n (default: mpv) \n {settings_player_status}\n"
                ),
                "Yes",
                "No"
            )
            if player:
                clear()
                randcolforname("[animdl-tui]")
                player_choice = Bullet(
                    prompt=f"{cyan} Choose a player. {reset} \n",
                    choices=[
                        "- mpv (default)  ",
                        "- vlc            ",
                        "- ffplay (ffmpeg)",
                        "- exit           ",
                    ],
                    bullet="",
                    margin=0,
                    align=1,
                    word_on_switch=colors.foreground["default"],
                    background_on_switch=colors.background["cyan"],
                )
                player_choice_result = player_choice.launch()
                match player_choice_result:
                    case "- mpv (default)  ":
                        data = {
                            "default_player": "mpv",
                            "players": {"mpv": {"executable": "mpv", "opts": []}},
                        }
                        print(" mpv should now be the selected player.")

                        with open(
                            "animdl_config.yml", "w", encoding="utf-8"
                        ) as animdl_config_write:
                            y.dump(data, animdl_config_write)
                        sleep(1)
                        cts()

                    case "- vlc            ":
                        data = {
                            "default_player": "vlc",
                            "players": {"vlc": {"executable": "vlc", "opts": []}},
                        }

                        print(" vlc should now be the selected player.")

                        with open(
                            "animdl_config.yml", "w", encoding="utf-8"
                        ) as animdl_config_write:
                            y.dump(data, animdl_config_write)
                        sleep(1)
                        cts()

                    case "- ffplay (ffmpeg)":
                        data = {
                            "default_player": "ffplay",
                            "players": {"ffplay": {"executable": "ffplay", "opts": []}},
                        }

                        print(" ffplay should now be the selected player.")

                        with open(
                            "animdl_config.yml", "w", encoding="utf-8"
                        ) as animdl_config_write:
                            y.dump(data, animdl_config_write)
                        sleep(1)
                        cts()

                    case "- exit           ":
                        cts()
            else:
                cpts()

        def provider():
            settings_provider_status = checkiffalse(tui_read_config, "provider")
            cursor.hide()
            randcolforname("[animdl-tui]")
            provider = confirmation(
                (
                    f"{cyan} Are you sure you want to"
                    f" switch to a different provider? {reset}\n"
                    f" (default: animixplay) \n"
                    f" {settings_provider_status} \n"
                ),
                "Yes",
                "No"
            )
            if provider:
                clear()
                randcolforname("[animdl-tui]")
                provider_choice = Bullet(
                    prompt=f"{cyan} Choose a provider {reset} (sorted by latency). \n",
                    choices=[
                        "- animixplay (default)",
                        "- animepahe           ",
                        "- haho (NSFW)         ",
                        "- gogoanime           ",
                        "- tenshi.moe          ",
                        "- allanime            ",
                        "- exit                ",
                    ],
                    bullet="",
                    margin=0,
                    align=1,
                    word_on_switch=colors.foreground["default"],
                    background_on_switch=colors.background["cyan"],
                )
                provider_choice_result = provider_choice.launch()

                match provider_choice_result:
                    case "- animixplay (default)":
                        print(" The provider has now been set to animixplay.")
                        tui_read_config["modifiers"]["provider"] = "animixplay"
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        sleep(1)
                        cts()

                    case "- animepahe           ":
                        print(" The provider has now been set to animepahe.")
                        tui_read_config["modifiers"]["provider"] = "animepahe"
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        sleep(1)
                        cts()

                    case "- haho (NSFW)         ":
                        print(" The provider has now been set to haho (NSFW).")
                        tui_read_config["modifiers"]["provider"] = "haho"
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        sleep(1)
                        cts()

                    case "- gogoanime           ":
                        print(" The provider has now been set to gogoanime.")
                        tui_read_config["modifiers"]["provider"] = "gogoanime"
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        sleep(1)
                        cts()

                    case "- tenshi.moe          ":
                        print(" The provider has now been set to tenshi.moe.")
                        tui_read_config["modifiers"]["provider"] = "tenshi"
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        sleep(1)
                        cts()

                    case "- allanime            ":
                        print(" The provider has now been set to allanime.")
                        tui_read_config["modifiers"]["provider"] = "allanime"
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        sleep(1)
                        cts()

                    case "- exit                ":
                        cts()
            else:
                cpts()

        def stylize_bool_in_config(config, tree, key):
            if key == "":
                if config[tree]:
                    return f"{green} True"
                return f"{red} False"

            if config[tree][key]:
                return f"{green} True"
            return f"{red} False"

        def toggle():
            cursor.hide()
            clear()
            qualitychoice = (
                "- QUALITY ="
                f"{stylize_bool_in_config(tui_read_config, 'toggles', 'quality'):5}"
            )
            dirchoice = (
                "- DIR ="
                f"{stylize_bool_in_config(tui_read_config, 'toggles', 'dir'):5}"
            )
            rangechoice = (
                "- RANGE ="
                f"{stylize_bool_in_config(tui_read_config, 'toggles', 'range'):5}"
            )
            specialchoice = (
                "- SPECIAL RANGE ="
                f"{stylize_bool_in_config(tui_read_config, 'toggles', 'special'):5}"
            )
            presencechoice = (
                "- DISCORD PRESENCE ="
                f"{stylize_bool_in_config(animdl_read_config, 'discord_presence', ''):5}"
            )

            randcolforname("[animdl-tui]")
            modules = Bullet(
                prompt=f"{cyan} Toggle modules: {reset} \n",
                choices=[
                    f"{qualitychoice}",
                    f"{dirchoice}",
                    f"{rangechoice}",
                    f"{specialchoice}",
                    f"{presencechoice}",
                    "- Exit    ",
                ],
                bullet="",
                margin=0,
                align=1,
                word_on_switch=colors.foreground["default"],
                background_on_switch=colors.background["cyan"],
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
                case "- Exit    ":
                    cts()

                case 0:
                    if tui_read_config["toggles"]["quality"] is True:
                        print(" ´QUALITY´ is now False")
                        tui_read_config["toggles"]["quality"] = False
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        toggle()
                    else:
                        print(" ´QUALITY´ is now True")
                        tui_read_config["toggles"]["quality"] = True
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        toggle()
                case 1:
                    if tui_read_config["toggles"]["dir"] is True:
                        print(" ´DIR´ is now False")
                        tui_read_config["toggles"]["dir"] = False
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        toggle()
                    else:
                        print(" ´DIR´ is now True")
                        tui_read_config["toggles"]["dir"] = True
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        toggle()
                case 2:
                    if tui_read_config["toggles"]["range"] is True:
                        print(" ´RANGE´ is now False")
                        tui_read_config["toggles"]["range"] = False
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        toggle()
                    else:
                        print(" ´RANGE´ is now True")
                        tui_read_config["toggles"]["range"] = True
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        toggle()
                case 3:
                    if tui_read_config["toggles"]["special"] is True:
                        print(" ´SPECIAL RANGE´ is now False")
                        tui_read_config["toggles"]["special"] = False
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        toggle()
                    else:
                        print(" ´SPECIAL RANGE´ is now True")
                        tui_read_config["toggles"]["special"] = True
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_read_config, configfile_write)
                        toggle()
                case 4:
                    if animdl_read_config["discord_presence"] is True:
                        print(" ´DISCORD PRESENCE´ is now False")
                        animdl_read_config["discord_presence"] = False
                        with open(
                            "animdl_config.yml", "w", encoding="utf-8"
                        ) as animdl_config_write:
                            y.dump(animdl_read_config, animdl_config_write)
                        toggle()
                    else:
                        print(" ´DISCORD PRESENCE´ is now True")
                        animdl_read_config["discord_presence"] = True
                        with open(
                            "animdl_config.yml", "w", encoding="utf-8"
                        ) as animdl_config_write:
                            y.dump(animdl_read_config, animdl_config_write)
                        if (
                            doespackageexist("pypresence") is True
                            and ismoduleon("animdl_config.yml", "discord_presence") is True
                        ):
                            toggle()

                        else:
                            print(
                                "Whoops, doesn't look like you have pypresence installed."
                            )
                            print(
                                "Please install it manually or by pressing enter. Thanks"
                            )
                            continue1()
                            if os.path.isfile("pypresence.txt") is True:
                                print(
                                    "Seems like you encountered a bug."
                                    "Please report it to me on github.com"
                                )
                            else:
                                with open(
                                    "pypresence.txt", "a", encoding="utf-8"
                                ) as pypresence_signal2:
                                    pypresence_signal2.write("pypresence installus")
                                    print(
                                        "pypresence will try to "
                                        "install on next startup of animdl-tui"
                                    )
                                ctypes.windll.shell32.ShellExecuteW(
                                    None,
                                    "runas",
                                    sys.executable,
                                    " ".join(sys.argv),
                                    None,
                                    1,
                                )
                                sys.exit()

        def directory():
            settings_dir_status = checkiffalse(tui_read_config, "dir")
            cursor.hide()
            randcolforname("[animdl-tui]")
            directory = confirmation(
                f"{cyan} Are you sure you want a specific directory? {reset} \n"
                f" {settings_dir_status} \n",
                "Yes",
                "No"
            )
            if directory:
                clear()
                randcolforname("[animdl-tui]")
                dir_input = Input(
                    prompt=(
                        f"{cyan} Enter a vaild directory. (Example: 'C:\\Users\\'){reset}"
                        f"\n {red}:{reset} "
                    ),
                    indent=0,
                )
                dir_input_result = dir_input.launch()
                if tui_read_config["toggles"]["dir"] is True:
                    print(f" ´DIR´ is now {dir_input_result}")
                    tui_read_config["modifiers"]["dir"] = f"{dir_input_result}"
                    with open("config.yml", "w", encoding="utf-8") as configfile_write:
                        y.dump(tui_read_config, configfile_write)
                    sleep(1)
                    cts()
                else:
                    print(" ´DIR´ is False")
                    dir_toggle = Bullet(
                        f"{green} - Would you like to enable ´DIR´? {reset} \n",
                        "Yes",
                        "No"
                    )
                    if dir_toggle:
                        print(" ´DIR´ is now True")
                        tui_config["toggles"]["dir"] = True
                        with open(
                            "config.yml", "w", encoding="utf-8"
                        ) as configfile_write:
                            y.dump(tui_config, configfile_write)
                            print(f" ´DIR´ is now {dir_input_result}")
                            tui_config["modifiers"]["dir"] = f'"{dir_input_result}"'
                            with open(
                                "config.yml", "w", encoding="utf-8"
                            ) as configfile_write:
                                y.dump(tui_config, configfile_write)
                                sleep(1)
                                cts()
                    else:
                        cpts()
            else:
                cpts()

        clear()
        randcolforname("[animdl-tui]")
        settings = Bullet(
            prompt=f"{green} Settings: {reset} \n",
            choices=[
                "- Toggle  ",
                "- Provider",
                "- Player  ",
                "- Quality ",
                "- Range   ",
                "- Special ",
                "- Dir     ",
                "- Exit    ",
            ],
            bullet="",
            margin=0,
            align=1,
            word_on_switch=colors.foreground["default"],
            background_on_switch=colors.background["cyan"],
        )
        result = settings.launch()
        match result:
            case "- Toggle  ":
                clear()
                toggle()
            case "- Provider":
                clear()
                provider()
            case "- Player  ":
                clear()
                player()
            case "- Quality ":
                clear()
                quality()
            case "- Range   ":
                clear()
                _range()
            case "- Special ":
                clear()
                _special()
            case "- Dir     ":
                clear()
                directory()
            case "- Exit    ":
                clear()
                main()
    except KeyboardInterrupt:
        print("Are you sure you want to exit the terminal? (Y/N)")
        decision = readchar.readchar()
        match decision:
            case "y":
                sys.exit()
            case "n":
                continue1()


def main():
    """main function"""
    try:
        cursor.hide()
        def stream():
            cursor.hide()
            with open("config.yml", "r", encoding="utf-8") as configfile_read:
                tui_config = y.safe_load(configfile_read)
            with open("animdl_config.yml", "r", encoding="utf-8") as animdl_configfile_read:
                animdl_config = y.safe_load(animdl_configfile_read)

            qualityarg = tui_config["modifiers"]["quality"]
            rangearg = f"-r {tui_config['modifiers']['range']}"
            specialarg = f"-s {tui_config['modifiers']['special']}"
            provider = tui_config["modifiers"]["provider"]

            randcolforname("[animdl-tui]")

            print(checkiffalse(tui_config, "quality"))
            print(checkiffalse(tui_config, "range"))
            print(checkiffalse(tui_config, "special"))
            print(checkiffalse(animdl_config, "default_player"))
            print(checkiffalse(tui_config, "provider"))
            streamus = Input(
                prompt=f"\n{cyan} Enter anime name.\n {red}:{reset} ", indent=0
            )
            streamus.result = streamus.launch()
            streamareyousure = Bullet(
                prompt=f"{cyan} Are you sure you want to stream {streamus.result}? \n",
                choices=[
                    f"- {green}Yes",
                    f"- {red}No",
                ],
                bullet="",
                margin=0,
                align=1,
                word_on_switch=colors.foreground["default"],
                background_on_switch=colors.background["white"],
            )
            streamareyousure.result = streamareyousure.launch()
            if streamareyousure.result == f"- {green}Yes":
                pass
            else:
                c_m()
                os.system(
                    f"animdl stream"
                    f'{specialarg} {rangearg} {qualityarg} "{provider}:{streamus.result}"'
                )
            clear()
            randcolforname("[animdl-tui]")
            locs = Bullet(
                prompt=f"{cyan} Do you want to leave "
                "or"
                f" do you want to continue streaming?{reset}",
                choices=[
                    f"- {green}Continue",
                    f"- {red}Leave",
                ],
                bullet="",
                margin=0,
                align=1,
                word_on_switch=colors.foreground["default"],
                background_on_switch=colors.background["white"],
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
            with open("config.yml", "r", encoding="utf-8") as configfile_read:
                tui_config = y.safe_load(configfile_read)
            provider = tui_config["modifiers"]["provider"]

            randcolforname("[animdl-tui]")

            print(checkiffalse(tui_config, "provider"))
            searchus = Input(
                prompt=f"{cyan} Enter anime name.\n {red}:{reset} ", indent=0
            )
            searchus.result = searchus.launch()
            searchusareyousure = Bullet(
                prompt=f"{cyan} Are you sure you want to search {searchus.result}? \n",
                choices=[
                    f"- {green}Yes",
                    f"- {red}No",
                ],
                bullet="",
                margin=0,
                align=1,
                word_on_switch=colors.foreground["default"],
                background_on_switch=colors.background["white"],
            )
            searchusareyousure.result = searchusareyousure.launch()
            if searchusareyousure.result == f"- {green}Yes":
                pass
            else:
                c_m()
            os.system(f'animdl search -p {provider} "{searchus.result}"')
            clear()
            randcolforname("[animdl-tui]")
            locs = Bullet(
                prompt=f"{cyan} Do you want to leave "
                "or"
                " do you want to continue searching?{reset}",
                choices=[
                    f"- {green}Continue",
                    f"- {red}Leave",
                ],
                bullet="",
                margin=0,
                align=1,
                word_on_switch=colors.foreground["default"],
                background_on_switch=colors.background["white"],
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
            randcolforname("[animdl-tui]")
            print(f"{cyan} Schedule: {reset}")
            os.system("animdl schedule")
            continue1()
            c_m()

        def grab():
            cursor.hide()

            with open("config.yml", "r", encoding="utf-8") as configfile_read:
                tui_config = y.safe_load(configfile_read)
            provider = tui_config["modifiers"]["provider"]

            randcolforname("[animdl-tui]")

            print(checkiffalse(tui_config, "provider"))
            grabus = Input(
                prompt=f"{cyan} Enter anime name.\n {red}:{reset} ", indent=0
            )
            grabus.result = grabus.launch()
            grabusareyousure = Bullet(
                prompt=f"{cyan} Are you sure you want to grab {grabus.result}? \n",
                choices=[
                    f"- {green}Yes",
                    f"- {red}No",
                ],
                bullet="",
                margin=0,
                align=1,
                word_on_switch=colors.foreground["default"],
                background_on_switch=colors.background["white"],
            )
            grabusareyousure.result = grabusareyousure.launch()
            if grabusareyousure.result == f"- {green}Yes":
                pass
            else:
                c_m()
            os.system(f'animdl grab "{provider}:{grabus.result}"')
            continue1()
            clear()
            randcolforname("[animdl-tui]")
            locg = Bullet(
                prompt=f"{cyan} Do you want to leave or do you want to continue grabbing?{reset}",
                choices=[
                    f"- {green}Continue",
                    f"- {red}Leave",
                ],
                bullet="",
                margin=0,
                align=1,
                word_on_switch=colors.foreground["default"],
                background_on_switch=colors.background["white"],
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
            with open("animdl_config.yml", "r", encoding="utf8") as animdl_config_read:
                animdl_config = y.safe_load(animdl_config_read)

            with open("config.yml", "r", encoding="utf-8") as configfile_read:
                tui_config = y.safe_load(configfile_read)

            qualityarg = tui_config["modifiers"]["quality"]
            rangearg = f"-r {tui_config['modifiers']['range']}"
            specialarg = f"-s {tui_config['modifiers']['special']}"
            directoryarg = f"-d {tui_config['modifiers']['dir']}"
            provider = tui_config["modifiers"]["provider"]

            randcolforname("[animdl-tui]")

            print(checkiffalse(tui_config, "quality"))
            print(checkiffalse(tui_config, "range"))
            print(checkiffalse(tui_config, "special"))
            print(checkiffalse(animdl_config, "default_player"))
            print(checkiffalse(tui_config, "dir"))
            print(checkiffalse(tui_config, "provider"))
            downloadus = Input(
                prompt=f"{cyan} Enter anime name.\n {red}:{reset} ", indent=0
            )
            downloadus.result = downloadus.launch()
            downloadusareyousure = Bullet(
                prompt=f"{cyan} Are you sure you want to download {downloadus.result}? \n",
                choices=[
                    f"- {green}Yes",
                    f"- {red}No",
                ],
                bullet="",
                margin=0,
                align=1,
                word_on_switch=colors.foreground["default"],
                background_on_switch=colors.background["white"],
            )
            downloadusareyousure.result = downloadusareyousure.launch()
            if downloadusareyousure.result == f"- {green}Yes":
                pass
            else:
                c_m()
            os.system(
                f"animdl download"
                f"{specialarg} {rangearg} {qualityarg} {directoryarg} "
                f'"{provider}:{downloadus.result}"'
            )
            continue1()
            clear()
            randcolforname("[animdl-tui]")
            locd = Bullet(
                prompt=f"{cyan} Do you want to leave "
                "or"
                " do you want to continue downloading?{reset}",
                choices=[
                    f"- {green}Continue",
                    f"- {red}Leave",
                ],
                bullet="",
                margin=0,
                align=1,
                word_on_switch=colors.foreground["default"],
                background_on_switch=colors.background["white"],
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
            randcolforname("[animdl-tui]")
            menu = Bullet(
                prompt=f"{green} Main Menu: {reset} \n",
                choices=[
                    "- Download",
                    "- Stream  ",
                    "- Search  ",
                    "- Schedule",
                    "- Grab    ",
                    "- Update  ",
                    "- Settings",
                    #'- Web (WIP/Not Working)',
                    "- Exit    ",
                ],
                bullet="",
                margin=0,
                align=1,
                word_on_switch=colors.foreground["default"],
                background_on_switch=colors.background["cyan"],
            )

            menu.result = menu.launch()

            match menu.result:
                case "- Download":
                    clear()
                    download()
                case "- Stream  ":
                    clear()
                    stream()
                case "- Search  ":
                    clear()
                    search()
                case "- Schedule":
                    clear()
                    schedule()
                case "- Grab    ":
                    clear()
                    grab()
                case "- Update  ":
                    clear()
                    update()
                case "- Settings":
                    clear()
                    thesettings()
                # case '- Web (WIP/Not Working)':
                #    clear()
                #    web()
                case "- Exit    ":
                    clear()
                    sys.exit()

        menu()
    except KeyboardInterrupt:
        print("Are you sure you want to exit the terminal? (Y/N)")
        decision = readchar.readchar()
        match decision:
            case "y":
                sys.exit()
            case "n":
                continue1()


if __name__ == "__main__":
    clear()
    cursor.hide()

    if ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.kernel32.SetConsoleTitleW("animdl-tui - Administrator")
    else:
        ctypes.windll.kernel32.SetConsoleTitleW("animdl-tui")

    checkifexists("animdl_config.yml", "x", ANIMDL_DEFAULT)
    checkifexists("config.yml", "x", CONFIG_DEFAULT)

    if ctypes.windll.shell32.IsUserAnAdmin() and os.path.isfile("animdl.txt"):
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

    if ctypes.windll.shell32.IsUserAnAdmin() and os.path.isfile("pypresence.txt"):
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

    if ctypes.windll.shell32.IsUserAnAdmin() and os.path.isfile("update.txt"):
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
            print(
                "Seems like you encountered a bug. Please report it to me on github.com"
            )
        else:
            with open("animdl.txt", "a", encoding="utf-8") as animdl_signal:
                animdl_signal.write("animdl installus")
                print("animdl will try to install on next startup of animdl-tui")
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )

            sys.exit()

    if (
        doespackageexist("pypresence") is True
        and ismoduleon("animdl_config.yml", "discord_presence") is True
    ):
        pass

    elif (
        doespackageexist("pypresence") is False
        and ismoduleon("animdl_config.yml", "discord_presence") is True
    ):
        print("Whoops, doesn't look like you have pypresence installed.")
        print("Please install it manually or by pressing enter. Thanks")
        continue1()
        if os.path.isfile("pypresence.txt") is True:
            print(
                "Seems like you encountered a bug. Please report it to me on github.com"
            )
        else:
            with open("pypresence.txt", "a", encoding="utf-8") as pypresence_signal:
                pypresence_signal.write("pypresence installus")
                print("pypresence will try to install on next startup of animdl-tui")
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(sys.argv), None, 1
            )
            sys.exit()
    else:
        pass
    clear()
    main()

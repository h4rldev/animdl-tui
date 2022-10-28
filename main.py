import sys, platform, os, ctypes, cursor
from colored import fg, attr
from bullet import Bullet, colors
from msvcrt import getch as getkey
from click import clear
from configparser import ConfigParser
global config
global file
file = "animdl-tui\\config.ini"
config = ConfigParser()
config.read(file)

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
    cursor.hide();
    def leave():
        os.system("exit");

    def special():
        print(-1)

    def range():
        print(-1)

    def quality():
        print(-1)

    def player():
        print(-1)

    def provider():
        print(-1)

    def toggle():
        clear();
        file = "animdl-tui\\config.ini"
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
        print("%s%s%s\n%s\n%s\n%s\n%s\n%s" % (bold, cyan, animdl1, animdl2, animdl3, animdl4, animdl5, reset));

        print("           +-----------------------+")
        print("           | PROVIDER      =", providerstatuscolor, "\b{:5}".format(config['toggles']['provider']), reset, "\b|")
        print("           | QUALITY       =", qualitystatuscolor, "\b{:5}".format(config['toggles']['quality']), reset, "\b|")
        print("           | RANGE         =", rangestatuscolor, "\b{:5}".format(config['toggles']['range']), reset, "\b|")
        print("           | SPECIAL RANGE =", specialstatuscolor, "\b{:5}".format(config['toggles']['special']), reset, "\b|")
        print("           +-----------------------+")
        modules = Bullet(
            prompt = "%s                 Enable modules: %s \n" % (bold, reset),
            choices = [
                "Provider",
                "Quality",
                "Range",
                "Special",
                "Exit"
            ],
            bullet = "",
            margin = 0,
            align = 20,
            word_on_switch=colors.foreground["white"],
            background_on_switch=colors.background["cyan"]
        )
        result = modules.launch()
        print("                    +------+")
        match result:
            case "Provider":
                if config['toggles']['provider'] == 'True':
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
            case "Quality":
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
            case "Range":
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
            case "Special":
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
            case "Exit":
                return 0;

    def settings():
        clear();
        print("%s%s%s\n%s\n%s\n%s\n%s\n%s" % (bold, cyan, animdl1, animdl2, animdl3, animdl4, animdl5, reset));
        settings = Bullet(
            prompt = "%s                     Settings:  %s \n" % (bold, reset),
            choices = [
                '- Toggle   -',
                '- Provider -',
                '- Player   -',
                '- Quality  -',
                '- Range    -',
                '- Special  -',
                '- Exit     -'
            ],
            bullet = "",
            margin = 0,
            align = 20,
            word_on_switch=colors.foreground["white"],
            background_on_switch=colors.background["cyan"]
        )
        result = settings.launch()
        match result:
            case '- Toggle   -':
                clear();
                toggle();
            case '- Provider -':
                clear();
                stream();
            case '- Player   -':
                clear();
                search();
            case '- Quality  -':
                clear();
                schedule();
            case '- Range    -':
                clear();
                grab();
            case "- Special  -":
                clear();
                update();
            case "- Exit     -":
                clear();
                menu();

    def update():
        match platform.system:
            case 'Windows':
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

            case 'Linux':
                print("I can't test this with linux rn.",
                "Run \'sudo animdl update to update.\'")
                exit();

            case 'Darwin':
                print("If you really use mac you have to contribute, I don't own a mac because I don't suck")
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
        cursor.hide();
        print("%s%s%s\n%s\n%s\n%s\n%s\n%s" % (bold, cyan, animdl1, animdl2, animdl3, animdl4, animdl5, reset));
        menu = Bullet(
            prompt = "%s                     Main Menu:  %s \n" % (bold, reset),
            choices = [
                '- Download -',
                '- Stream   -',
                '- Search   -',
                '- Schedule -',
                '- Grab     -',
                '- Update   -',
                '- Settings -',
                '- Exit     -'
            ],
            bullet = "",
            margin = 0,
            align = 20,
            word_on_switch=colors.foreground["white"],
            background_on_switch=colors.background["cyan"]
        )

        result = menu.launch()
        match result:
            case '- Download -':
                clear();
                download();
            case '- Stream   -':
                clear();
                stream();
            case '- Search   -':
                clear();
                search();
            case '- Schedule -':
                clear();
                schedule();
            case '- Grab     -':
                clear();
                grab();
            case "- Update   -":
                clear();
                update();
            case "- Settings -":
                clear();
                settings();
            case "- Exit     -":
                clear();
                leave();
    menu();

def is_admin():
    if platform.system == 'Windows':
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False
    else:
        return False

if is_admin():
    os.system("animdl update");
    os.system("pause");
    exit();

if __name__ == '__main__':
    clear();
    main();
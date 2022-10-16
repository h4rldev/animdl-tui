import sys, platform, os, ctypes, cursor
from colored import fg, attr
from bullet import Bullet, colors, Check
from msvcrt import getch as getkey
from click import clear

cyan = fg("cyan")
reset = attr("reset")
bold = attr("bold")

animdl1 = " ___  _ _  _  _  _   __   _"
animdl2 = "| . || \ || ||  \ \ | . \| |"
animdl3 = "|   ||   || ||     || | || |_"
animdl4 = "|_|_||_\_||_||_|_|_||___/|___|"
animdl5 = "=============================="

def continue1():
    print("\n Press any key to continue");
    getkey();

def main():
    cursor.hide();
    def leave():
        os.system("exit");

    def toggle():
        Check(checked=True)

    def settings():
        print("%s%s%s\n%s\n%s\n%s\n%s\n%s" % (bold, cyan, animdl1, animdl2, animdl3, animdl4, animdl5, reset));
        settings = Bullet(
            prompt = "%s        -Settings:- %s \n" % (bold, reset),
            choices = [
                '- Toggle   -'
                '- Provider -'
                '- Player   -'
                '- Quality  -'
                '- Range    -'
                '- Special  -'
                '- Exit     -'
            ],
            bullet = "",
            margin = 0,
            align = 8,
            word_on_switch=colors.foreground["white"],
            background_on_switch=colors.background["cyan"]
        )
        result = settings.launch()
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
            case "6. Update":
                clear();
                update();
            case "7. Settings":
                clear();
                settings();
            case "8. Exit":
                clear();
                leave();

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
            prompt = "%s        -Main Menu:- %s \n" % (bold, reset),
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
            align = 8,
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
            case "6. Update":
                clear();
                update();
            case "7. Settings":
                clear();
                settings();
            case "8. Exit":
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
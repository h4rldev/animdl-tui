import ctypes, sys, platform, os
from colored import fg, attr
from bullet import Bullet, Check, YesNo, Input, Date, CheckDependencies, Password, ScrollBar
from msvcrt import getch as getkey
from click import clear

blue = fg("blue")
reset = attr("reset")

animdl1 = " ___  _ _  _  __ _        __   _"
animdl2 = "| . || \ || ||  \ \  ___ | . \| |"
animdl3 = "|   ||   || ||     ||___|| | || |_"
animdl4 = "|_|_||_\_||_||_|_|_|     |___/|___|"

def continue1():
    print("\n Press any key to continue");
    getkey();

def main():
    def leave():
        os.system("exit");

    def settings():
        print("yes")

    def update():
        match platform.system:
            case 'Windows':
                if is_admin():
                    os.system("animdl update")

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
        print(blue, animdl1, reset)
        print(blue, animdl2, reset)
        print(blue, animdl3, reset)
        print(blue, animdl4, reset, "\n")
        menu = Bullet(
            bullet = ">> ",
            prompt = "Choose Action:",
            choices = [
                '1. Download',
                '2. Grab',
                '3. Schedule',
                '4. Search',
                '5. Stream',
                '6. Update',
                '7. Settings',
                '8. Exit'
            ])

        result = menu.launch()
        match result:
            case "1. Download":
                clear();
                download();
            case "2. Grab":
                clear();
                grab();
            case "3. Schedule":
                clear();
                schedule();
            case "4. Search":
                clear();
                search();
            case "5. Stream":
                clear();
                stream();
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
    exit();

if __name__ == '__main__':
    clear();
    main();
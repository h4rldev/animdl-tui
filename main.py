import ctypes, sys, os
from bullet import Bullet, Check, YesNo, Input, Date, CheckDependencies, Password, ScrollBar
from msvcrt import getch as getkey
from click import clear, prompt

if os.name == 'nt':
    os.system('color')


def continue1():
    print("\n Press any key to continue");
    getkey();

def leave():
    os.system("exit");

def settings():
    print("yes")

def update():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if os.name == 'nt':
        if is_admin():
            os.system("animdl update")
        else:
            # Re-run the program with admin rights
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            os.system("powershell.exe %s" % (__file__))
    else:
        print("I can't test this with linux rn. Run \'sudo animdl update to update.\'")
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
    cli = Bullet(bullet = ">> ", prompt = " Choose Action:", choices = ['1. Download', '2. Grab', '3. Schedule', '4. Search', '5. Stream', '6. Update', '7. Settings', '8. Exit'])
    result = cli.launch()
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

def is_admin():
    if os.name == 'nt':
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
    menu();
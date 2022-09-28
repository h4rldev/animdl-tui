import pick, ctypes, sys, os#, webbrowser 
from msvcrt import getch as getkey

def leave():
    exit();

def settings():
    getkey();

def update():
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        os.system("animdl update")
        getkey();
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

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
    title = 'What do you want to do?: '
    options = ['Download', 'Grab', 'Schedule', 'Search', 'Stream', 'Update', 'Settings', 'Exit']
    indicator = '•'
    option, index = pick.pick(options, title, indicator)
    amogus = index

    if amogus == 0:
        download();
    elif amogus == 1:
        grab();
    elif amogus == 2:
        schedule();
    elif amogus == 3:
        search();
    elif amogus == 4:
        stream();
    elif amogus == 5:
        update();
    elif amogus == 6:
        settings();
    else:
        leave();



def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
        title = 'Do you want to update?: '
        options = ['Yes', 'No']
        indicator = '•'
        pick.pick(options)
        option, index = pick.pick(options, title, indicator)
        amogus = index

        if amogus == 0:
            update();
        else:
            menu();

menu();
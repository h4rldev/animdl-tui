import pick, ctypes, sys, os
from msvcrt import getch as getkey
from termcolor import colored
from click import clear

os.system('color')

def leave():
    exit();

def settings():
    def provider():
        global provider
        title = 'Choose Provider: '
        options = ['animixplay', 'haho (NSFW)', 'gogoanime', 'tenshi', 'animepahe','allanime', 'Exit']
        indicator = 'Provider -> •'
        option, index = pick.pick(options, title, indicator)
        amogus = index

        if amogus == 0:
            provider = 'animixplay'
            print("The provider has been set to", provider)
            getkey();
        elif amogus == 1:
            provider = 'haho'
            print("The provider has been set to", provider)
            getkey();
        elif amogus == 2:
            provider = 'gogoanime'
            print("The provider has been set to", provider)
            getkey();
        elif amogus == 3:
            provider = 'tenshi'
            print("The provider has been set to", provider)
            getkey();
        elif amogus == 4:
            provider = 'animepahe'
            print("The provider has been set to", provider)
            getkey();
        elif amogus == 5:
            provider = 'allanime'
            print("The provider has been set to\""+provider+"\"")
            getkey();
        else:
            settings();
        getkey();
    def quality():
        getkey();
    def range():
        getkey();
    def directory():
        getkey();
    def leave():
        menu();
    title = 'Settings: '
    options = ['Provider', 'Quality', 'Range', 'Directory', 'Exit']
    indicator = '•'
    option, index = pick.pick(options, title, indicator)
    amogus = index

    if amogus == 0:
        provider();
    elif amogus == 1:
        quality();
    elif amogus == 2:
        range();
    elif amogus == 3:
        directory();
    else:
        leave();

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
    options = ['[1.] Download', '[2.] Grab', '[3.] Schedule', '[4.] Search', '[5.] Stream', '[6.] Update', '[7.]Settings', '[8.] Exit']
    indicator = 'Main Menu -> •'
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

if __name__ == '__main__':
    menu();
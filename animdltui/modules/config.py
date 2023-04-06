import yaml
import sys
import os

from pathlib import Path

if "win32" in sys.version:
    default_config_path = (
        Path(os.getenv("LOCALAPPDATA", "."))
        / ".config"
        / "animdl-tui"
        / "tui_config.yml"
    )

else:
    config_path = (
        Path(os.getenv("HOME", ".")) / ".config" / "animdl-tui" / "tui_config.yml"
    )


ANIMDL_DEFAULT: dict = {
    "default_player": "mpv",
    "discord_presence": False,
    "players":{
        "mpv": {
            "executable": "mpv",
            "opts": []
        }
    }
}

TUI_DEFAULT: dict = {
    "skip_main_menu": False,
    "debug": False,
    # "idm": "status": False,

    "directory": {
        "status": False,
        "value": ""
    },

    "range": {
        "status": False,
        "value": ""
    },
    
    "quality": {
        "status": False,
        "value": ""
    },
    
    "special": {
        "status": False,
        "value": ""
    },
    
    "default_index": {
        "status": False,
        "value": ""
    }

}


def todo():
    """Todo"""
    pass

def main():
    todo()
    
def config():
    print("Config")
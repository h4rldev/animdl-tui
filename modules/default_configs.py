"""default configs for animdl and animdl-tui"""
ANIMDL_DEFAULT: dict = {
    "default_player": "mpv",
    "players": {"mpv": {"executable": "mpv", "opts": []}},
    "discord_presence": False,
}

CONFIG_DEFAULT: dict = {
    "modifiers": {
        "dir": "",
        "provider": "animixplay",
        "quality": "",
        "range": "",
        "special": "",
    },
    "toggles": {
        "dir": False,
        "quality": True,
        "range": False,
        "special": False,
    },
}

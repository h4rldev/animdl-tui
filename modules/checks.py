"""Checks for things (may deprecate soon)"""

import os

from colors import cyan, red, reset
import yaml as y

def doespackageexist(package):
    """Checks if a package exists"""
    is_present = os.system(f"pip show {package}")
    if is_present == 1:
        return False
    return True

def ismoduleon(config_file, module: str):
    """Checks if pypresence is enabled or not"""
    with open(config_file, "r", encoding="utf-8") as module_io:
        module_check = y.safe_load(module_io)

        if module_check[module] is True:
            return module_check[module]
        return False


def checkifexists(file, mode, default_data):
    """Checks if a file exists, if it doesn't it, it creates it and writes default data to it"""
    if os.path.isfile(file) is False:
        with open(file, mode, encoding="utf-8") as make_config_file:
            y.dump(default_data, make_config_file)
    else:
        pass


def checkiffalse(config, modifier: str):
    """Checks if a modifier is false"""
    with open("config.yml", "r", encoding="utf-8") as configfile_read:
        tui_config = y.safe_load(configfile_read)
    with open("animdl_config.yml", "r", encoding="utf-8") as animdl_config_read:
        animdl_config = y.safe_load(animdl_config_read)

    if config == animdl_config:
        modifier_value = config[modifier]
    else:
        modifier_value = config["modifiers"][modifier]
    if modifier != "provider" and config != animdl_config:
        modifier_status = config["toggles"][modifier]

    if modifier == "special":
        modifier_name = "Special Range"
    elif modifier == "default_player":
        modifier_name = "Player"
    else:
        modifier_name = modifier.capitalize()

    if config == tui_config:
        if modifier == "provider":
            return f" {modifier_name} is {cyan}{modifier_value}{reset}"
        if config["toggles"][modifier] is False:
            return f" {modifier_name} is {red}{modifier_status}{reset}"
        return f" {modifier_name} is {cyan}{modifier_value}{reset}"
    return f" {modifier_name} is {cyan}{modifier_value}{reset}"

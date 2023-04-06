from colored import fg, bg, attr
from colorama import just_fix_windows_console

# fg colors
FG_RED = fg("#FF0000")
FG_ORANGE = fg("#FFA500")
FG_YELLOW = fg("#FFFF00")
FG_GREEN = fg("#00FF00")
FG_BLUE = fg("#0000FF")
FG_INDIGO = fg("#4B0082")
FG_VIOLET = fg("#8F00FF")
FG_CYAN = fg("#00FFFF")

# bg colors
BG_RED = bg("#FF0000")
BG_ORANGE = bg("#FFA500")
BG_YELLOW = bg("#FFFF00")
BG_GREEN = bg("#00FF00")
BG_BLUE = bg("#0000FF")
BG_INDIGO = bg("#4B0082")
BG_VIOLET = bg("#8F00FF")
BG_CYAN = bg("#00FFFF")
# attr
RESET = attr("reset")
BOLD = attr("bold")
UNDERLINED = attr("underlined")
BLINK = attr("blink")

just_fix_windows_console()

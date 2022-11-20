# animdl-tui

[![License](https://img.shields.io/github/license/h4rldev/animdl-tui?style=flat-square)](https://github.com/H4rldev/animdl-tui/blob/main/LICENSE)

A Terminal User Interface for [animdl](https://github.com/justfoolingaround/animdl)

(_heck, I had to fork a library and make it better for this_)

(__I WON'T ADD FUZZYFINDER FOR THIS BECAUSE TWIST.MOE IS RANCID__)

## News

First working release!! (expect bugs)

How to run:

```shell
git clone https://github.com/H4rldev/animdl-tui
cd animdl-tui
main.py
```

Please report bugs in [issues](https://github.com/h4rldev/animdl-tui/issues)

## Todo

- Web frontent for it
- Code Cleanup
- Less skill issues.

## Installation

1. Download from the [releases](https://github.com/h4rldev/animdl-tui/releases) (currently empty due to it not even having a working release atm due to me not even implementing it yet)
2. Put the executable in a directory.
3. Put the directory in path.
4. Execute the name of the executable in your terminal.
5. Profit???

## Build/running latest

From the command line

Run in the cloned repository:

Run it directly or:
`python main.py`

Build in the cloned repository:

`pyinstaller --onefile --hidden-import animdl --hidden-import pypresence  --icon logo.ico main.py`

## Requirements (building)

- Python 3.10
- Windows (as of right now)
- [animdl](https://github.com/justfoolingaround/animdl)
- [colored](https://pypi.org/project/colored/)
- [click](https://pypi.org/project/click/)
- [rebullet](https://pypi.org/project/rebullet) and dependencies.
- [pyinstaller](https://pyinstaller.org/en/stable/) (if you want to build from source)

## Requirements (running)

- Python 3.10 (probably)
- Windows (as of right now)
- [animdl](https://github.com/justfoolingaround/animdl)
- [mpv](https://mpv.io/)
- other deps i can't find out atm

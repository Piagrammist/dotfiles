import re

from libqtile.lazy import lazy


def parse_window_name(name):
    if not name:
        return name
    # remove the HTML title from chrome window name
    return re.sub(r".+ - (.+)$", "\\1", name)


@lazy.function
def toggle_minimize_all(qtile):
    for win in qtile.current_group.windows:
        if hasattr(win, "toggle_minimize"):
            win.toggle_minimize()

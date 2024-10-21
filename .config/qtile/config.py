from libqtile.config import Screen

import bar
from bar import widget_defaults, extension_defaults
from color import palette
from group import groups, keys
from hook import *
from keybinding import mod, mouse
from layout import floating_layout, layouts

screens = [
    Screen(top=bar.default),
]

wmname = "LG3D"
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = True
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

wl_input_rules = None
wl_xcursor_theme = None
wl_xcursor_size = 24

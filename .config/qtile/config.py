import bar
import color
from group import groups, keys
from hook import client_new
from keybinding import mod, mouse
from layout import floating_layout, layouts
from libqtile.config import Screen

palette = color.DoomOne

widget_defaults = dict(
    font="Mona Sans Bold Italic", fontsize=12, padding=0, background=palette[0]
)
extension_defaults = widget_defaults.copy()

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

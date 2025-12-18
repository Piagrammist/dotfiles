from libqtile import qtile
from libqtile.config import Drag, Key, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = 'mod4'
browser = 'chrome'
terminal = guess_terminal('alacritty')


keys = [
    # General
    Key([mod],            'Return', lazy.spawn(terminal),          desc="Launch terminal"),
    Key([mod, 'shift'],   'w',      lazy.spawn(browser),           desc="Launch browser"),
    Key([mod, 'shift'],   'Return', lazy.spawn("rofi -show drun"), desc="Run launcher"),
    Key([mod],            'r',      lazy.spawncmd(),               desc="Show Qbar's launcher"),
    Key([mod, 'control'], 'r',      lazy.reload_config(),          desc="Reload the Qtile config"),
    Key([mod, 'control'], 'q',      lazy.shutdown(),               desc="Shutdown Qtile"),

    # Window - General
    Key([mod], 'w',     lazy.window.kill(),              desc="Kill focused window"),
    Key([mod], 'n',     lazy.layout.normalize(),         desc="Reset all window sizes"),
    Key([mod], 'space', lazy.layout.next(),              desc="Move window focus to the next"),
    Key([mod], 'Tab',   lazy.next_layout(),              desc="Toggle between layouts"),
    Key([mod], 't',     lazy.window.toggle_floating(),   desc="Toggle floating on the focused window"),
    Key([mod], 'f',     lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "m",     lazy.window.toggle_maximize(),   desc="Toggle maximize"),

    # Window - Focus
    Key([mod], 'h', lazy.layout.left(),  desc="Move focus to left"),
    Key([mod], 'l', lazy.layout.right(), desc="Move focus to right"),
    Key([mod], 'j', lazy.layout.down(),  desc="Move focus down"),
    Key([mod], 'k', lazy.layout.up(),    desc="Move focus up"),

    # Window - Move
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left(),  desc="Move window to the left"),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down(),  desc="Move window down"),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up(),    desc="Move window up"),

    # Window - Grow
    Key([mod, 'control'], 'h', lazy.layout.grow_left(),  desc="Grow window to the left"),
    Key([mod, 'control'], 'l', lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, 'control'], 'j', lazy.layout.grow_down(),  desc="Grow window down"),
    Key([mod, 'control'], 'k', lazy.layout.grow_up(),    desc="Grow window up"),

    # Dmenu Scripts
    KeyChord([mod], 'd', [
        Key([], 'p', lazy.spawn("dm-power"),   desc="Run power dmenu"),
        Key([], 'c', lazy.spawn("dm-configs"), desc="Run configs list dmenu"),
    ]),
]


# Keys to switch VTs in Wayland.
for vt in range(1, 8):
    keys.append(
        Key(['control', 'mod1'], f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == 'wayland'),
            desc=f"Switch to VT{vt}"
        )
    )


mouse = [
    Drag([mod], 'Button1', lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], 'Button3', lazy.window.set_size_floating(),     start=lazy.window.get_size()),
]

from libqtile import bar, widget

from util import parse_window_name
from color import palette

widget_defaults = dict(
    padding=0,
    font="Roboto Slab",
    fontsize=13,
    background=palette[0],
    foreground=palette[1],
)
extension_defaults = widget_defaults.copy()

line = widget.TextBox(text='|', fontsize=14, padding=2)
spacer = widget.Spacer(length=10)

default = bar.Bar(
    size=32,
    margin=[6, 4, 0, 4],
    widgets=[
        spacer,
        widget.TextBox(
            '󰣇 ',
            font="Symbols Nerd Fonts",
            fontsize=24,
            markup=False,
        ),
        widget.CurrentLayout(),
        spacer,
        line,
        widget.GroupBox(
            spacing=0,
            padding=4,
            toggle=False,
            rounded=False,
            borderwidth=3,
            disable_drag=True,
            active=palette[8],
            inactive=palette[1],
            highlight_method='line',
            highlight_color=palette[2],
            this_current_screen_border=palette[7],
            this_screen_border=palette[4],
            other_current_screen_border=palette[7],
            other_screen_border=palette[4],
        ),
        line,
        spacer,
        widget.Prompt(),
        widget.WindowName(
            max_chars=40,
            foreground=palette[6],
            parse_text=parse_window_name,
        ),
        widget.Chord(
            chords_colors={'launch': ('#ff0000', '#ffffff')},
            name_transform=lambda name: name.upper(),
        ),
        widget.Clock(format="%m/%d  %H:%M"),
        widget.Spacer(length=bar.STRETCH),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Systray(),
        spacer,
    ],
)

from libqtile import bar, widget
from util import parse_window_name

default = bar.Bar(
    [
        widget.Spacer(length=10),
        widget.TextBox(
            "󰣇",
            font="Symblos Nerd Fonts",
            fontsize=24,
            markup=False,
        ),
        widget.Spacer(length=8),
        widget.CurrentLayout(),
        widget.Spacer(length=10),
        widget.GroupBox(
            disable_drag=True,
            highlight_method="line",
            highlight_color=["000000", "606060"],
            this_current_screen_border="f0f0f0",
            inactive="626262",
            toggle=False,
            spacing=0,
            padding=4,
        ),
        widget.Spacer(length=10),
        widget.Prompt(),
        widget.WindowName(parse_text=parse_window_name),
        widget.Chord(
            chords_colors={
                "launch": ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.Clock(format="%m/%d  %H:%M"),
        widget.Spacer(length=bar.STRETCH),
        # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
        # widget.StatusNotifier(),
        widget.Systray(),
        widget.Spacer(length=10),
    ],
    32,
    margin=[6, 4, 0, 4],
)

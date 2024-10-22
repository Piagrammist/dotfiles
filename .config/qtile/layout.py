from libqtile import layout
from libqtile.config import Match

from color import palette

layout_defaults = {
    'margin': 8,
    'border_width': 2,
    'border_focus':  palette[0],
    'border_normal': palette[7],
    'border_on_single': False,
}

layouts = [
    layout.Tile(**layout_defaults),
    layout.Columns(**layout_defaults),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,

        Match(wm_class='error'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='notification'),
        Match(wm_class='file_progress'),

        Match(wm_class='ssh-askpass'),
        Match(wm_class='qalculate-qt'),
        Match(wm_class='pavucontrol'),

        # gitk
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(title='branchdialog'),

        # GPG key password entry
        Match(title='pinentry'),
    ]
)

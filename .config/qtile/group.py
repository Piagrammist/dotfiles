from keybinding import keys, mod
from libqtile.config import Group, Key
from libqtile.lazy import lazy

groups_info = [
    {"label": "1"},
    {"label": "2", "layout": "Tile"},
    {"label": "3", "layout": "Tile"},
    {"label": "4"},
    {"label": "5"},
]

groups = []
for i in range(len(groups_info)):
    name = str(i + 1)
    info = groups_info[i]
    groups.append(
        Group(
            name=name,
            label=info.get("label", name),
            layout=info.get("layout", "Tile").lower(),
        )
    )
    keys.extend(
        [
            Key(
                [mod],
                name,
                lazy.group[name].toscreen(),
                desc=f"Switch to group {name}",
            ),
            Key(
                [mod, "shift"],
                name,
                lazy.window.togroup(name, switch_group=True),
                desc=f"Switch to & move focused window to group {name}",
            ),
        ]
    )

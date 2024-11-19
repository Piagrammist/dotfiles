[ -d "$HOME/.bin"           ] && PATH="$HOME/.bin:$PATH"
[ -d "$HOME/.local/bin"     ] && PATH="$HOME/.local/bin:$PATH"
[ -d "$HOME/.scripts"       ] && PATH="$PATH:$HOME/.scripts"
[ -d "$HOME/.scripts/dmenu" ] && PATH="$PATH:$HOME/.scripts/dmenu"
[ -d "$HOME/.cargo/bin"     ] && PATH="$PATH:$HOME/.cargo/bin"
export PATH

if [ -z "$DISPLAY" ] && [ $XDG_VTNR -eq 1 ]; then
    exec startx
fi

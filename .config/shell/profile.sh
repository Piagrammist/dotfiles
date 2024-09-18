[ -d "$HOME/.bin"       ] && PATH="$HOME/.bin:$PATH"
[ -d "$HOME/.local/bin" ] && PATH="$HOME/.local/bin:$PATH"
[ -d "$HOME/.scripts"   ] && PATH="$PATH:$HOME/.scripts"
export PATH

if [ -z "$DISPLAY" ] && [ $XDG_VTNR -eq 1 ]; then
    exec startx
fi

[[ -f ~/.zshrc ]] && . ~/.zshrc
if [[ -f ~/.config/shell/profile.sh ]]; then
    emulate sh
    . ~/.config/shell/profile.sh
    emulate zsh
fi

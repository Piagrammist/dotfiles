alias vim='nvim'
alias rg='rg -S'
alias du='du -sh'
alias free='free -h'
alias grep='grep --color=auto -i'

alias pacad='sudo pacman -S'
alias pacup='sudo pacman -Syu'
alias pacrm='sudo pacman -Rns'
alias pacls='pacman -Qqen'
alias aurls='pacman -Qqem'
alias aurup='paru -Syua'

alias psa='ps auxf'
alias psrg="ps aux | rg -v rg | rg -S"
alias cursorls='fd --type dir "cursors" /usr/share/icons ~/.local/share/icons ~/.icons 2>/dev/null'

alias s='git status'
alias commit='git commit -m'
alias pull='git pull'
alias push='git push'
alias diffu='git diff'
alias diffs='git diff --staged'

alias ..='cd ..'
alias .2='cd ../..'

__base_eza='eza --group-directories-first --color=always'
__base_ls="$__base_eza -lAhF"
alias ls="$__base_ls"
alias la="$__base_eza -A"
alias ll="$__base_eza -l"
alias lt="$__base_eza -At"
alias l.="$__base_ls .."
alias l..="$__base_ls ../.."
unset __base_eza __base_ls

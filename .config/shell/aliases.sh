# General
alias vim='nvim'
alias rg='rg -S'        # Smartcase
alias du='du -sh'       # Human-readable | No children listing
alias df='df -h'        # Human-readable
alias free='free -h'    # Human-readable
alias grep='grep --color=auto -i'

# Packages
alias pacad='sudo pacman -S'
alias pacup='sudo pacman -Syu'
alias pacrm='sudo pacman -Rns'
alias pacls='pacman -Qqen'
alias aurls='pacman -Qqem'
alias aurup='paru -Syua'

# Reflector
__base_reflector='sudo reflector --latest 20 --save /etc/pacman.d/mirrorlist'
alias  mirror="$__base_reflector"
alias mirrord="$__base_reflector --sort delay"
alias mirrors="$__base_reflector --sort score"
unset __base_reflector

# Processes
alias psa='ps auxf'
alias psrg='ps aux | rg -v rg | rg -S'

# Git
alias s='git status'
alias commit='git commit -m'
alias pull='git pull'
alias push='git push'
alias addup='git add -u'
alias diffu='git diff'
alias diffs='git diff --staged'

# Navigation / Listing
alias ..='cd ..'
alias .2='cd ../..'

__base_eza='eza --group-directories-first --color=always'
__base_ls="$__base_eza -lAhF"
alias ls="$__base_ls"
alias la="$__base_eza -A"
alias ll="$__base_eza -l"
alias lt="$__base_eza -AT"
alias l.="$__base_ls .."
alias l..="$__base_ls ../.."
unset __base_eza __base_ls

alias cursorls='fd --type dir "cursors" /usr/share/icons ~/.local/share/icons ~/.icons 2>/dev/null'

[[ $- != *i* ]] && return

bindkey -e
bindkey '^[[H'      beginning-of-line       # Home
bindkey '^[[F'      end-of-line             # End
bindkey '^[[3~'     delete-char             # Delete
bindkey '^[[1;5D'   backward-word           # Ctrl + ArrowLeft
bindkey '^[[1;5C'   forward-word            # Ctrl + ArrowRight
bindkey '^H'        backward-kill-word      # Ctrl + Backspace
bindkey '^[[3;5~'   kill-word               # Ctrl + Delete

__base_dir="$HOME/.config/shell"
[[ -f "$__base_dir/env.sh" ]] && . "$__base_dir/env.sh"
[[ -f "$__base_dir/aliases.sh" ]] && . "$__base_dir/aliases.sh"
unset __base_dir

eval "$(starship init zsh)"

__zsh_dir="/usr/share/zsh/plugins"
source "$__zsh_dir/zsh-autosuggestions/zsh-autosuggestions.plugin.zsh"
source "$__zsh_dir/zsh-syntax-highlighting/zsh-syntax-highlighting.plugin.zsh"
unset __zsh_dir

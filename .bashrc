[[ $- != *i* ]] && return

__base_dir="$HOME/.config/shell"
[[ -f "$__base_dir/env.sh" ]] && . "$__base_dir/env.sh"
[[ -f "$__base_dir/aliases.sh" ]] && . "$__base_dir/aliases.sh"
unset __base_dir

# PS1='[\u@\h \W]\$ '
eval "$(starship init bash)"

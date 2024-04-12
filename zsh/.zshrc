# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.config/zsh/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
#if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
#  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
#fi


autoload -U colors && colors
# autoload -U promptinit && promptinit
# promptinit; prompt gentoo
# PS1="%B%{$fg[red]%}[%{$fg[yellow]%}%n%{$fg[green]%}@%{$fg[blue]%}%M %{$fg[magenta]%}%~%{$fg[red]%}]%{$reset_color%}$%b "
# PS1="%{$fg[red]%}%n%{$reset_color%}@%{$fg[blue]%}%m %{$fg[yellow]%}%~ %{$reset_color%}%% "

# History in cache directory:
HISTSIZE=10000
SAVEHIST=10000
HISTFILE=~/.cache/zsh/history

# export ZSH_COMPDUMP=~/.cache/zsh/.zcompdump-$HOST

# Basic auto/tab complete:
autoload -U compinit promptinit
compinit -d ~/.cache/zsh/zcompdump-$ZSH_VERSION
promptinit; prompt gentoo #Enabling cache for the completions for zsh gentoo
 # zstyle menu select
zstyle ':completion:*' menu select matcher-list '' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=*' 'l:|=* r:|=*'
zstyle ':completion::complete:*' use-cache 1
zmodload zsh/complist

compinit
_comp_options+=(globdots)		# Include hidden files.

# vi mode
bindkey -v
export KEYTIMEOUT=1


# Use vim keys in tab complete menu:
# bindkey -M menuselect 'h' vi-backward-char
# bindkey -M menuselect 'k' vi-up-line-or-history
# bindkey -M menuselect 'l' vi-forward-char
# bindkey -M menuselect 'j' vi-down-line-or-history
# bindkey -v '^?' backward-delete-char


bindkey  "^[[H"   beginning-of-line
bindkey  "^[[F"   end-of-line
bindkey  "^[[3~"  delete-char




# source /usr/share/zsh-autosuggestions/zsh-autosuggestions.zsh 2>/dev/null
# source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh 2>/dev/null
# source /usr/share/zsh/plugins/zsh-history-substring-search/zsh-history-substring-search.zsh 2>/dev/null
# source /usr/share/zsh-theme-powerlevel10k/powerlevel10k.zsh-theme
source ~/.config/zsh/zsh-history-substring-search.zsh

#substring search
bindkey '^[[A' history-substring-search-up
bindkey '^[[B' history-substring-search-down
HISTORY_SUBSTRING_SEARCH_ENSURE_UNIQUE=1

#alias
# alias ls='ls --color=auto'
# alias l.='ls -d .* --color=auto'
# alias la='ls -la'
# alias i='sudo pacman -S'
# alias up='sudo pacman -Syu'
alias v='nvim'
alias sv='doas nvim'
alias sudo='doas'
alias i='doas emerge -a'
alias u='doas emerge -cav'
alias up='doas emerge -auDN @world'
source $ZDOTDIR/.aliases
#defaultapps
export EDITOR="nvim"
export SUDO_EDITOR="nvim"
export TERMINAL="kitty"
export BROWSER="firefox"
alias nvidia-settings --config="$XDG_CONFIG_HOME"/nvidia/settings # Alias nvidia-settings to use a custom configuration location: 
# export Term=xterm

#Environent variablees
export XDG_CONFIG_HOME="$HOME/.config"
export XDG_CACHE_HOME="$HOME/.cache"
export XDG_DATA_HOME="$HOME/.local/share"
export XDG_STATE_HOME="$HOME/.local/state"
# export GNUPGHOME="$XDG_DATA_HOME"/gnupg

export CUDA_CACHE_PATH="$XDG_CACHE_HOME"/nv
export GTK2_RC_FILES="$XDG_CONFIG_HOME"/gtk-2.0/gtkrc
export XCURSOR_PATH=/usr/share/icons:$XDG_DATA_HOME/icons

# export HOME=/home/ak


#Path
export PATH="/home/ok/.local/bin/:$PATH"

# umask 0077

#colored pass prompt
export SUDO_PROMPT="$(tput setaf 1 bold)Password:$(tput sgr0) "

# To customize prompt, run `p10k configure` or edit ~/.config/zsh/.p10k.zsh.
#[[ ! -f ~/.config/zsh/.p10k.zsh ]] || source ~/.config/zsh/.p10k.zsh
# cd
#
#
source /usr/share/zsh/site-functions/zsh-syntax-highlighting.zsh

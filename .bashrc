[[ $- == *i* ]] && source ~/opt/ble.sh/out/ble.sh --noattach
# /etc/skel/.bashrc
#
# This file is sourced by all *interactive* bash shells on startup,
# including some apparently interactive shells such as scp and rcp
# that can't tolerate any output.  So make sure this doesn't display
# anything or bad things will happen !


# Test for an interactive shell.  There is no need to set anything
# past this point for scp and rcp, and it's important to refrain from
# outputting anything in those cases.
if [[ $- != *i* ]] ; then
	# Shell is non-interactive.  Be done now!
	return
fi


# get current branch in git repo
function parse_git_branch() {
	BRANCH=`git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/\1/'`
	if [ ! "${BRANCH}" == "" ]
	then
		STAT=`parse_git_dirty`
		echo "  [${BRANCH}${STAT}]"
	else
		echo ""
	fi
}

# get current status of git repo
function parse_git_dirty {
	status=`git status 2>&1 | tee`
	dirty=`echo -n "${status}" 2> /dev/null | grep "modified:" &> /dev/null; echo "$?"`
	untracked=`echo -n "${status}" 2> /dev/null | grep "Untracked files" &> /dev/null; echo "$?"`
	ahead=`echo -n "${status}" 2> /dev/null | grep "Your branch is ahead of" &> /dev/null; echo "$?"`
	newfile=`echo -n "${status}" 2> /dev/null | grep "new file:" &> /dev/null; echo "$?"`
	renamed=`echo -n "${status}" 2> /dev/null | grep "renamed:" &> /dev/null; echo "$?"`
	deleted=`echo -n "${status}" 2> /dev/null | grep "deleted:" &> /dev/null; echo "$?"`
	bits=''
	if [ "${renamed}" == "0" ]; then
		bits=">${bits}"
	fi
	if [ "${ahead}" == "0" ]; then
		bits="*${bits}"
	fi
	if [ "${newfile}" == "0" ]; then
		bits="+${bits}"
	fi
	if [ "${untracked}" == "0" ]; then
		bits="?${bits}"
	fi
	if [ "${deleted}" == "0" ]; then
		bits="x${bits}"
	fi
	if [ "${dirty}" == "0" ]; then
		bits="!${bits}"
	fi
	if [ ! "${bits}" == "" ]; then
		echo " ${bits}"
	else
		echo ""
	fi
}

# Put your fun stuff here.
#Path
export PATH="$PATH:$HOME/.local/bin/:~/.config/emacs/bin"

PS1="\[\e[32m\][\[\e[m\]\[\e[31m\]\u\[\e[m\]\[\e[33m\]@\[\e[m\]\[\e[32m\]\h\[\e[m\]:\[\e[36m\]\W\[\e[m\]\[\e[32m\]]\[\e[m\]\[\e[35m\]\\$\[\e[m\]\[\e[36m\]\`parse_git_branch\`\[\e[m\] "

# bind 'set show-all-if-ambiguous on'
# bind 'TAB:menu-complete'
#
# #key binding to use vi line editing commands: 
# # set editing-mode vi
# # No double entries in the shell history.
# export HISTCONTROL="$HISTCONTROL erasedups:ignoreboth"
#
# bind '"\e[A": history-substring-search-backward'
# bind '"\e[B": history-substring-search-forward'
# # Wrap the following commands for interactive use to avoid accidental file overwrites.
# rm() { command rm -i "${@}"; }
# cp() { command cp -i "${@}"; }
# mv() { command mv -i "${@}"; }


# alias
# alias ls='ls --color=auto'
# alias l.='ls -d .* --color=auto'
# alias la='ls -la'
# alias i='sudo pacman -S'
# alias up='sudo pacman -Syu'
alias ls='lsd'
alias v='nvim'
alias sv='doas nvim'
#alias sudo='doas'
alias i='doas emerge -a'
alias u='doas emerge -cav'
alias up='doas emerge -auDN @world'
#defaultapps
export EDITOR="nvim"
export SUDO_EDITOR="nvim"
export TERMINAL="kitty"
export BROWSER="firefox"
[[ ${BLE_VERSION-} ]] && ble-attach

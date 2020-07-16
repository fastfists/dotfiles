#!/bin/sh
# Profile file. Runs on login.

# Adds `~/.scripts` and all subdirectories to $PATH
export PATH="$PATH:$(du "$HOME/.scripts/" | cut -f2 | tr '\n' ':' | sed 's/:*$//')"
export EDITOR="nvim"
export TERMINAL="st"
export BROWSER="firefox"
export READER="zathura"
export FILE="ranger"
export SUDO_ASKPASS="$HOME/.scripts/wmcmds/dmenupass"
export NOTMUCH_CONFIG="$HOME/.config/notmuch-config"
export GTK2_RC_FILES="$HOME/.config/gtk-2.0/gtkrc-2.0"
export XDG_SESSION_TYPE=x11
export GDK_BACKEND=x11

# less/man colors
export LESS=-R
export LESS_TERMCAP_mb="$(printf '%b' '[1;31m')"; a="${a%_}"
export LESS_TERMCAP_md="$(printf '%b' '[1;36m')"; a="${a%_}"
export LESS_TERMCAP_me="$(printf '%b' '[0m')"; a="${a%_}"
export LESS_TERMCAP_so="$(printf '%b' '[01;44;33m')"; a="${a%_}"
export LESS_TERMCAP_se="$(printf '%b' '[0m')"; a="${a%_}"
export LESS_TERMCAP_us="$(printf '%b' '[1;32m')"; a="${a%_}"
export LESS_TERMCAP_ue="$(printf '%b' '[0m')"; a="${a%_}"

# Config file
export ZDOTDIR="$HOME/.config/zsh"
export ANDROID_HOME="$HOME/.android/android-sdk" 
export ANDROID_SDK_ROOT="$HOME/.android/android-sdk"
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk

[ ! -f ~/.config/shortcutrc ] && shortcuts >/dev/null 2>&1

# Start graphical server if it not already running.
[ "$(tty)" = "/dev/tty1" ] && ! ps -e | grep -qw Xorg && exec startx

# Switch escape and caps if tty:
sudo -n loadkeys ~/.scripts/ttymaps.kmap 2>/dev/null

export PATH="$HOME/.cargo/bin:$PATH"
export PATH="$PATH:/opt/android-sdk/emulator"
export PATH="$PATH:/opt/android-sdk/platform-tools"
export PATH="$PATH:/opt/android-sdk/tools/bin"
export PATH="$PATH:$HOME/devel/flutter/bin"

source /home/fastfist/.config/broot/launcher/bash/br

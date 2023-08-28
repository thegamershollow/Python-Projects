#! /bin/sh
cd $HOME
mkdir brew && curl -L https://github.com/Homebrew/brew/tarball/master | tar xz --strip 1 -C brew
export PATH=$HOME/brew/bin:$PATH >> ~/.zshrc
exec $SHELL
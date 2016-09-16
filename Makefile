.PHONY: XXX all nvim zshrc git sig


XXX:
	$(error Missing target. Use 'make all' to install all targets)

all: nvim zshrc git signature

nvim:
	@make -C neovimrc/

zshrc:
	@make -C zshrc/

git:
	cp -f gitconfig ~/.gitconfig
	cp -f gitignore ~/.gitignore

sig:
	cp -f signature.html ~/.signature.html

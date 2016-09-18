.PHONY: XXX install nvim zshrc git sig


XXX:
	$(error Missing target. Use 'make install' to install all targets)

install: nvim zshrc git sig

nvim:
	@make -C neovimrc/ install

zshrc:
	@make -C zshrc/ install

git:
	cp -f gitconfig ~/.gitconfig
	cp -f gitignore ~/.gitignore

sig:
	cp -f signature.html ~/.signature.html

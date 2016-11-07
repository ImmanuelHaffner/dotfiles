.PHONY: XXX install nvim zshrc git sig cgdb


XXX:
	$(error Missing target. Use 'make install' to install all targets)

install: nvim zshrc git sig

nvim:
	@make -C neovimrc/ install

zshrc:
	@make -C zshrc/ install

git:
	cp -f gitconfig "${HOME}/.gitconfig"
	cp -f gitignore "${HOME}/.gitignore"

sig:
	cp -f signature.html "${HOME}/.signature.html"

cgdb:
	mkdir -p "${HOME}/.cgdb"
	cp -f cgdbrc "${HOME}/.cgdb/cgdbrc"

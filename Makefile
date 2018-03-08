.PHONY: XXX install nvim zshrc git sig cgdb


XXX:
	$(error Missing target. Use 'make install' to install all targets)

install: nvim zshrc git sig zathura qutebrowser

nvim:
	@make -C neovimrc/ install

zshrc:
	@make -C zshrc/ install

git:
	cp -f gitconfig "${HOME}/.gitconfig"
	cp -f gitignore "${HOME}/.gitignore"

sig:
	cp -f infosys.sig.html "${HOME}/.infosys.sig.html"
	cp -f private.sig.html "${HOME}/.private.sig.html"

cgdb:
	mkdir -p "${HOME}/.cgdb"
	cp -f cgdbrc "${HOME}/.cgdb/cgdbrc"

zathura:
	mkdir -p "${HOME}/.config/zathura"
	cp -f zathurarc "${HOME}/.config/zathura/zathurarc"

qutebrowser:
	mkdir -p "${HOME}/.config/qutebrowser"
	cp -f qutebrowser.py "${HOME}/.config/qutebrowser/config.py"

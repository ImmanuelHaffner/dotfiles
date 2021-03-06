.PHONY: XXX install nvim zshrc git sig cgdb ctags


XXX:
	$(error Missing target. Use 'make install' to install all targets)

install: nvim zshrc git sig cgdb zathura qutebrowser

nvim:
	@make -C neovimrc/ install

zshrc:
	@make -C zshrc/ install

git:
	cp -f gitconfig "${HOME}/.gitconfig"
	cp -f gitignore "${HOME}/.gitignore"
	git config --global user.signingkey $(shell gpg --list-secret-keys --keyid-format LONG "haffner.immanuel@gmail.com" | grep sec | cut --delimiter='/' -f 2 | cut --delimiter=' ' -f 1)

sig:
	cp -f bigdata.sig.html "${HOME}/.bigdata.sig.html"
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
	-xdg-settings set default-web-browser org.qutebrowser.qutebrowser.desktop
	-xdg-mime default org.qutebrowser.qutebrowser.desktop x-scheme-handler/http
	-xdg-mime default org.qutebrowser.qutebrowser.desktop x-scheme-handler/https

ctags:
	cp -f ctags ~/.ctags

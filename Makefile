.PHONY: XXX install nvim zshrc git sig cgdb zathura qutebrowser ctags screen latex xcompose matplotlib bin


XXX:
	$(error Missing target. Use 'make install' to install all configurations or 'make <APP>' to install the \
        configuration for a specific app)

install: nvim zshrc git sig cgdb zathura qutebrowser ctags screen latex xcompose matplotlib bin clangd wezterm

nvim:
	@make -C neovimrc/ install

zshrc:
	@make -C zshrc/ install

git:
	cp -f gitconfig "${HOME}/.gitconfig"
	cp -f gitignore "${HOME}/.gitignore"
	-git config --global user.signingkey $(shell gpg --list-secret-keys --keyid-format LONG "haffner.immanuel@gmail.com" | grep sec | cut --delimiter='/' -f 2 | cut --delimiter=' ' -f 1)

sig:
	cp -f bigdata.sig.html "${HOME}/.bigdata.sig.html"
	cp -f private.sig.html "${HOME}/.private.sig.html"

cgdb:
	mkdir -p "${HOME}/.cgdb"
	cp -f cgdbrc "${HOME}/.cgdb/cgdbrc"
	cp -f gdbinit "${HOME}/.gdbinit"

zathura:
	mkdir -p "${HOME}/.config/zathura"
	cp -f zathurarc "${HOME}/.config/zathura/zathurarc"

qutebrowser:
	mkdir -p "${HOME}/.config/qutebrowser"
	cp -f qutebrowser/qutebrowser.py "${HOME}/.config/qutebrowser/config.py"
	-xdg-settings set default-web-browser org.qutebrowser.qutebrowser.desktop
	-xdg-mime default org.qutebrowser.qutebrowser.desktop x-scheme-handler/http
	-xdg-mime default org.qutebrowser.qutebrowser.desktop x-scheme-handler/https
	cp -R qutebrowser/greasemonkey "${HOME}/.config/qutebrowser"

ctags:
	cp -f ctags "${HOME}/.ctags"

screen:
	cp -f screenrc "${HOME}/.screenrc"

latex:
	cp -f latexmkrc "${HOME}/.latexmkrc"

xcompose:
	cp -f XCompose "${HOME}/.XCompose"

matplotlib:
	cp -Rf matplotlib "${HOME}/.config/"

bin:
	cp -f uds-intranet "${HOME}/.local/bin/"

clangd:
	mkdir -p "${HOME}/.config/clangd"
	cp clangd.yaml "${HOME}/.config/clangd/config.yaml"

wezterm:
	cp wezterm.lua "${HOME}/.wezterm.lua"
	gsettings set org.cinnamon.desktop.default-applications.terminal exec wezterm # start Wezterm from Nemo

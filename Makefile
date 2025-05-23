.PHONY: XXX install bin cgdb ctags erdtreerc git gpg latex lazygit matplotlib nvim qutebrowser screen xcompose zathura zshrc


XXX:
	$(error Missing target. Use 'make install' to install all configurations or 'make <APP>' to install the \
        configuration for a specific app)

install: bin cgdb ctags erdtreerc git gpg htop latex lazygit matplotlib nvim qutebrowser screen wezterm xcompose zathura zshrc

nvim:
	@make -C neovimrc/ install

zshrc:
	@make -C zshrc/ install

git:
	cp -f gitconfig "${HOME}/.gitconfig"
	cp -f gitignore "${HOME}/.gitignore"
	-git config --global user.signingkey $(shell gpg --list-secret-keys --keyid-format LONG "haffner.immanuel@gmail.com" | grep sec | cut --delimiter='/' -f 2 | cut --delimiter=' ' -f 1)

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
	@>&2 echo "WARNING: Installing a user-wide clangd config currently breaks clangd support in mutable"
	@read -n1 -p "Install anyway? [y/N]" choice; \
        case $${choice} in \
            y|Y) \
                mkdir -p "${HOME}/.config/clangd"; \
                cp clangd.yaml "${HOME}/.config/clangd/config.yaml"; \
                ;; \
            *) ;; \
        esac

wezterm:
	cp wezterm.lua "${HOME}/.wezterm.lua"
	-gsettings set org.cinnamon.desktop.default-applications.terminal exec /usr/bin/wezterm  # start Wezterm from Nemo
	tempfile=$(mktemp) \
             && curl -o $tempfile https://raw.githubusercontent.com/wez/wezterm/master/termwiz/data/wezterm.terminfo \
             && tic -x -o ~/.terminfo $tempfile \
             && rm $tempfile


htop:
	mkdir -p "${HOME}/.config/htop/"
	cp -f htoprc "${HOME}/.config/htop/htoprc"

erdtree:
	cp erdtreerc "${HOME}/.erdtreerc"

lazygit:
	mkdir -p "${HOME}/.config/lazygit"
	cp -f lazygit.yml "${HOME}/.config/lazygit/config.yml"

gpg:
	mkdir -p "${HOME}/.gnupg"
	cp gpg/* "${HOME}/.gnupg/"

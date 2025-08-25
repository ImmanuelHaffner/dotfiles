.PHONY: XXX install
.PHONY: \
    bin \
    cgdb \
    ctags \
    erdtreerc \
    git \
    gpg \
    htop \
    latex \
    lazygit \
    matplotlib \
    nvim \
    qutebrowser \
    screen \
    vectorcode \
    wezterm \
    xcompose \
    zathura \
    zshrc

SHELL := /bin/bash

XXX:
	$(error Missing target. Use 'make install' to install all configurations or 'make <APP>' to install the \
        configuration for a specific app)

install: \
    bin \
    cgdb \
    ctags \
    erdtreerc \
    git \
    gpg \
    htop \
    latex \
    lazygit \
    matplotlib \
    nvim \
    qutebrowser \
    screen \
    vectorcode \
    wezterm \
    xcompose \
    zathura \
    zshrc

nvim:
	@make -C neovimrc/ install

zshrc:
	@make -C zshrc/ install

git:
	install -D gitconfig "${HOME}/.gitconfig"
	install -D gitignore "${HOME}/.gitignore"
	-git config --global user.signingkey $(shell gpg --list-secret-keys --keyid-format LONG "haffner.immanuel@gmail.com" | grep sec | cut --delimiter='/' -f 2 | cut --delimiter=' ' -f 1)

cgdb:
	install -D cgdbrc "${HOME}/.cgdb/cgdbrc"
	install -D gdbinit "${HOME}/.gdbinit"

zathura:
	install -D zathurarc "${HOME}/.config/zathura/zathurarc"

qutebrowser:
	install -D qutebrowser/qutebrowser.py "${HOME}/.config/qutebrowser/config.py"
	-xdg-settings set default-web-browser org.qutebrowser.qutebrowser.desktop
	-xdg-mime default org.qutebrowser.qutebrowser.desktop x-scheme-handler/http
	-xdg-mime default org.qutebrowser.qutebrowser.desktop x-scheme-handler/https
	install -D qutebrowser/greasemonkey/* "${HOME}/.config/qutebrowser/greasemonkey/"

ctags:
	install -D ctags "${HOME}/.ctags"

screen:
	install -D screenrc "${HOME}/.screenrc"

latex:
	install -D latexmkrc "${HOME}/.latexmkrc"

xcompose:
	install -D XCompose "${HOME}/.XCompose"

matplotlib:
	install -dD matplotlib "${HOME}/.config/"

bin:
	install -D bin/* "${HOME}/.local/bin/"

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
	install wezterm.lua "${HOME}/.wezterm.lua"
	-gsettings set org.cinnamon.desktop.default-applications.terminal exec /usr/bin/wezterm  # start Wezterm from Nemo
	tempfile=$(mktemp) \
             && curl -o $tempfile https://raw.githubusercontent.com/wez/wezterm/master/termwiz/data/wezterm.terminfo \
             && tic -x -o ~/.terminfo $tempfile \
             && rm $tempfile


htop:
	mkdir -p "${HOME}/.config/htop/"
	install -D htoprc "${HOME}/.config/htop/htoprc"

erdtree:
	install -D erdtreerc "${HOME}/.erdtreerc"

lazygit:
	mkdir -p "${HOME}/.config/lazygit"
	install -D lazygit.yml "${HOME}/.config/lazygit/config.yml"

gpg:
	mkdir -p "${HOME}/.gnupg"
	install -D gpg/* "${HOME}/.gnupg/"

vectorcode:
	install -T vectorcode-config.json5 "${HOME}/.config/vectorcode/config.json5"

# Dotfiles

Personal dotfiles and configuration for Linux and macOS, managed via `make`.

### Quick Start

```sh
# Install everything
make install

# Install a single component
make nvim
make zshrc
make git
```

### What's Included


| Component | Description |
|-----------|-------------|
| **bin** | Utility scripts — Arca cloud VM management, remote Neovide, Wake-on-LAN |
| **clangd** | User-wide clangd language server config |
| **ctags** | Ctags configuration |
| **erdtree** | Erdtree file-tree viewer config |
| **git** | Git aliases, delta pager, GPG signing, difftool/mergetool via Neovim |
| **gpg** | GnuPG agent and key configuration |
| **htop** | htop settings (separate configs for Linux and macOS) |
| **latex** | `latexmk` build configuration |
| **lazygit** | Lazygit TUI configuration |
| **matplotlib** | Custom matplotlib style (`acm.mplstyle`) |
| **[neovimrc]** ⚙ | Extensive Neovim config with custom statusline, LSP, Telescope, and more |
| **[qutebrowser](qutebrowser/)** | Qutebrowser config with Greasemonkey scripts |
| **screen** | GNU Screen configuration |
| **vectorcode** | VectorCode configuration |
| **[wezterm](wezterm.lua)** | WezTerm terminal emulator config (Night Owl theme, DPI-aware font sizing) |
| **XCompose** | Custom Compose key sequences (Linux only) |
| **zathura** | Zathura PDF viewer config (Linux only) |
| **[zshrc]** ⚙ | Zsh shell configuration and environment setup |

⚙ = Git submodule (separate repository)

[neovimrc]: https://github.com/ImmanuelHaffner/neovimrc
[zshrc]: https://github.com/ImmanuelHaffner/zsh-rc


### Platform Support

The top-level `Makefile` detects the OS and includes the appropriate platform-specific makefile (`Makefile-linux` or `Makefile-macos`). Each target installs its config files to the expected locations under `$HOME`.

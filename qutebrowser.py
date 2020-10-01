config.load_autoconfig()

# Zoom factor
# Enable Qt auto scaling by globally setting QT_AUTO_SCREEN_SCALE_FACTOR=1 (e.g. in /etc/profile)
c.zoom.default      = '75%'

# Fonts
c.fonts.completion.category = "bold 9pt monospace"
c.fonts.completion.entry    = "9pt monospace"
c.fonts.debug_console       = "9pt monospace"
c.fonts.downloads           = "9pt monospace"
c.fonts.hints               = "bold 9pt monospace"
c.fonts.keyhint             = "9pt sans-serif"
c.fonts.messages.error      = "9pt monospace"
c.fonts.messages.info       = "9pt monospace"
c.fonts.messages.warning    = "9pt monospace"
c.fonts.prompts             = "9pt sans-serif"
c.fonts.statusbar           = "10pt monospace"
c.fonts.tabs.selected       = "10pt monospace"
c.fonts.tabs.unselected     = "10pt monospace"

# User CSS
# c.content.user_stylesheets = ['css/solarized-dark-all-sites.css']

########################################################################################################################
# Colorscheme
########################################################################################################################
solarized = {
        'base03': '#002b36',
        'base02': '#073642',
        'base01': '#586e75',
        'base00': '#657b83',
        'base0': '#839496',
        'base1': '#93a1a1',
        'base2': '#eee8d5',
        'base3': '#fdf6e3',
        'yellow': '#b58900',
        'orange': '#cb4b16',
        'red': '#dc322f',
        'magenta': '#d33682',
        'violet': '#6c71c4',
        'blue': '#268bd2',
        'cyan': '#2aa198',
        'green': '#859900'
        }

## Background color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.bg = solarized['base03']

## Bottom border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.bottom = solarized['base03']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.category.border.top = solarized['base03']

## Foreground color of completion widget category headers.
## Type: QtColor
c.colors.completion.category.fg = solarized['base3']

## Background color of the completion widget for even rows.
## Type: QssColor
c.colors.completion.even.bg = solarized['base02']

## Text color of the completion widget.
## Type: QtColor
c.colors.completion.fg = solarized['base3']

## Background color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.bg = solarized['violet']

## Bottom border color of the selected completion item.
## Type: QssColor
c.colors.completion.item.selected.border.bottom = solarized['violet']

## Top border color of the completion widget category headers.
## Type: QssColor
c.colors.completion.item.selected.border.top = solarized['violet']

## Foreground color of the selected completion item.
## Type: QtColor
c.colors.completion.item.selected.fg = solarized['base3']

## Foreground color of the matched text in the completion.
## Type: QssColor
c.colors.completion.match.fg = solarized['base2']

## Background color of the completion widget for odd rows.
## Type: QssColor
c.colors.completion.odd.bg = solarized['base02']

## Color of the scrollbar in completion view
## Type: QssColor
c.colors.completion.scrollbar.bg = solarized['base0']

## Color of the scrollbar handle in completion view.
## Type: QssColor
c.colors.completion.scrollbar.fg = solarized['base2']

## Background color for the download bar.
## Type: QssColor
c.colors.downloads.bar.bg = solarized['base03']

## Background color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.bg = solarized['red']

## Foreground color for downloads with errors.
## Type: QtColor
c.colors.downloads.error.fg = solarized['base3']

## Color gradient start for download backgrounds.
## Type: QtColor
# c.colors.downloads.start.bg = '#0000aa'

## Color gradient start for download text.
## Type: QtColor
c.colors.downloads.start.fg = solarized['base3']

## Color gradient stop for download backgrounds.
## Type: QtColor
# c.colors.downloads.stop.bg = '#00aa00'

## Color gradient end for download text.
## Type: QtColor
# c.colors.downloads.stop.fg = solarized['base3']

## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.downloads.system.bg = 'rgb'

## Color gradient interpolation system for download text.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.downloads.system.fg = 'rgb'

## Background color for hints. Note that you can use a `rgba(...)` value
## for transparency.
## Type: QssColor
c.colors.hints.bg = solarized['violet']

## Font color for hints.
## Type: QssColor
c.colors.hints.fg = solarized['base3']

## Font color for the matched part of hints.
## Type: QssColor
c.colors.hints.match.fg = solarized['base2']

## Background color of the keyhint widget.
## Type: QssColor
# c.colors.keyhint.bg = 'rgba(0, 0, 0, 80%)'

## Text color for the keyhint widget.
## Type: QssColor
c.colors.keyhint.fg = solarized['base3']

## Highlight color for keys to complete the current keychain.
## Type: QssColor
c.colors.keyhint.suffix.fg = solarized['yellow']

## Background color of an error message.
## Type: QssColor
c.colors.messages.error.bg = solarized['red']

## Border color of an error message.
## Type: QssColor
c.colors.messages.error.border = solarized['red']

## Foreground color of an error message.
## Type: QssColor
c.colors.messages.error.fg = solarized['base3']

## Background color of an info message.
## Type: QssColor
c.colors.messages.info.bg = solarized['base03']

## Border color of an info message.
## Type: QssColor
c.colors.messages.info.border = solarized['base03']

## Foreground color an info message.
## Type: QssColor
c.colors.messages.info.fg = solarized['base3']

## Background color of a warning message.
## Type: QssColor
c.colors.messages.warning.bg = solarized['orange']

## Border color of a warning message.
## Type: QssColor
c.colors.messages.warning.border = solarized['orange']

## Foreground color a warning message.
## Type: QssColor
c.colors.messages.warning.fg = solarized['base3']

## Background color for prompts.
## Type: QssColor
c.colors.prompts.bg = solarized['base02']

## Border used around UI elements in prompts.
## Type: String
c.colors.prompts.border = '1px solid ' + solarized['base3']

## Foreground color for prompts.
## Type: QssColor
c.colors.prompts.fg = solarized['base3']

## Background color for the selected item in filename prompts.
## Type: QssColor
c.colors.prompts.selected.bg = solarized['base01']

## Background color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.bg = solarized['blue']

## Foreground color of the statusbar in caret mode.
## Type: QssColor
c.colors.statusbar.caret.fg = solarized['base3']

## Background color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.bg = solarized['violet']

## Foreground color of the statusbar in caret mode with a selection.
## Type: QssColor
c.colors.statusbar.caret.selection.fg = solarized['base3']

## Background color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.bg = solarized['base03']

## Foreground color of the statusbar in command mode.
## Type: QssColor
c.colors.statusbar.command.fg = solarized['base3']

## Background color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.bg = solarized['base01']

## Foreground color of the statusbar in private browsing + command mode.
## Type: QssColor
c.colors.statusbar.command.private.fg = solarized['base3']

## Background color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.bg = solarized['green']

## Foreground color of the statusbar in insert mode.
## Type: QssColor
c.colors.statusbar.insert.fg = solarized['base3']

## Background color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.bg = solarized['base03']

## Foreground color of the statusbar.
## Type: QssColor
c.colors.statusbar.normal.fg = solarized['base3']

## Background color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.bg = solarized['magenta']

## Foreground color of the statusbar in passthrough mode.
## Type: QssColor
c.colors.statusbar.passthrough.fg = solarized['base3']

## Background color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.bg = solarized['base01']

## Foreground color of the statusbar in private browsing mode.
## Type: QssColor
c.colors.statusbar.private.fg = solarized['base3']

## Background color of the progress bar.
## Type: QssColor
c.colors.statusbar.progress.bg = solarized['base3']

## Foreground color of the URL in the statusbar on error.
## Type: QssColor
c.colors.statusbar.url.error.fg = solarized['red']

## Default foreground color of the URL in the statusbar.
## Type: QssColor
c.colors.statusbar.url.fg = solarized['base3']

## Foreground color of the URL in the statusbar for hovered links.
## Type: QssColor
c.colors.statusbar.url.hover.fg = solarized['base2']

## Foreground color of the URL in the statusbar on successful load
## (http).
## Type: QssColor
c.colors.statusbar.url.success.http.fg = solarized['base3']

## Foreground color of the URL in the statusbar on successful load
## (https).
## Type: QssColor
c.colors.statusbar.url.success.https.fg = solarized['base3']

## Foreground color of the URL in the statusbar when there's a warning.
## Type: QssColor
c.colors.statusbar.url.warn.fg = solarized['yellow']

## Background color of the tab bar.
## Type: QtColor
# c.colors.tabs.bar.bg = '#555555'

## Background color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.bg = solarized['base01']

## Foreground color of unselected even tabs.
## Type: QtColor
c.colors.tabs.even.fg = solarized['base2']

## Color for the tab indicator on errors.
## Type: QtColor
c.colors.tabs.indicator.error = solarized['red']

## Color gradient start for the tab indicator.
## Type: QtColor
c.colors.tabs.indicator.start = solarized['violet']

## Color gradient end for the tab indicator.
## Type: QtColor
c.colors.tabs.indicator.stop = solarized['orange']

## Color gradient interpolation system for the tab indicator.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
# c.colors.tabs.indicator.system = 'rgb'

## Background color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.bg = solarized['base01']

## Foreground color of unselected odd tabs.
## Type: QtColor
c.colors.tabs.odd.fg = solarized['base2']

## Background color of selected even tabs.
## Type: QtColor
c.colors.tabs.selected.even.bg = solarized['base03']

## Foreground color of selected even tabs.
## Type: QtColor
c.colors.tabs.selected.even.fg = solarized['base3']

## Background color of selected odd tabs.
## Type: QtColor
c.colors.tabs.selected.odd.bg = solarized['base03']

## Foreground color of selected odd tabs.
## Type: QtColor
c.colors.tabs.selected.odd.fg = solarized['base3']

## Background color for webpages if unset (or empty to use the theme's
## color)
## Type: QtColor
# c.colors.webpage.bg = 'white'

# Search engines
c.url.searchengines.update({
    'DEFAULT':  'https://www.google.de/search?q={}',
    'gg':       'https://www.google.de/search?q={}',
    'duck':     'https://duckduckgo.com/?q={}&ia=web',
    'eco':      'https://www.ecosia.org/search?q={}',
    'map':      'https://www.google.com/maps/place/{}',
    'arch':     'https://wiki.archlinux.org/index.php?search={}',
    'clang':    'https://duckduckgo.com/?q=\\site:clang.llvm.org/doxygen+{}',
    'llvm':     'https://duckduckgo.com/?q=\\site:llvm.org/doxygen+{}',
    'aio':      'http://www.aiosearch.com/search/4/Torrents/{}/',
    'we':       'https://en.wikipedia.org/wiki/{}',
    'wd':       'https://de.wikipedia.org/wiki/{}',
    'cpp':      'http://en.cppreference.com/mwiki/index.php?search={}',
    'amazon':   'https://smile.amazon.de/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}',
    'dblp':     'https://dblp.uni-trier.de/search?q={}',
    'acm':      'https://dl.acm.org/results.cfm?query={}',
    'gs':       'https://scholar.google.de/scholar?q={}',
    'steamdb':  'https://steamdb.info/search/?a=app&q={}',
    'dict':     'https://www.dict.cc/?s={}',
    'leo':      'https://dict.leo.org/german-english/{}',
    'ling':     'https://www.linguee.com/english-german/search?source=auto&query={}',
    'yt':       'https://www.youtube.com/results?search_query={}',
    'wolfram':  'https://www.wolframalpha.com/input/?i={}',
    'py':       'https://docs.python.org/3/search.html?q={}&check_keywords=yes',
    'nzb':      'https://www.binsearch.info/?q={}&max=250&adv_age=1100&server=',
    'ghub':     'https://github.com/search?q={}',
    'hy':       'https://www.hyphenation24.com/word/{}/',
    'dhl':      'https://www.dhl.de/en/privatkunden/pakete-empfangen/verfolgen.html?piececode={}',
    'duden':    'https://www.duden.de/suchen/dudenonline/{}',
    'fa':       'https://fontawesome.com/icons?d=gallery&q={}',
    'intrin':   'https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text={}',
    'stock':    'https://www.finanzen.net/suchergebnis.asp?_search={}',
    })

# External Editor
c.editor.command = ['/usr/bin/sakura', '-e', '/usr/bin/nvim', '{}']

c.aliases = {
    'l': 'session-load',
    'w': 'session-save',
}
config.bind('<Ctrl-q>', 'session-save ;; quit')

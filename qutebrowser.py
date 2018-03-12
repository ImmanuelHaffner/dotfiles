config.load_autoconfig()

# Zoom
c.zoom.default      = '50%'

# Fonts
c.fonts.completion.category = "bold 6pt monospace"
c.fonts.completion.entry    = "6pt monospace"
c.fonts.debug_console       = "6pt monospace"
c.fonts.downloads           = "6pt monospace"
c.fonts.hints               = "bold 6pt monospace"
c.fonts.keyhint             = "6pt sans-serif"
c.fonts.messages.error      = "6pt monospace"
c.fonts.messages.info       = "6pt monospace"
c.fonts.messages.warning    = "6pt monospace"
c.fonts.prompts             = "6pt sans-serif"
c.fonts.statusbar           = "6pt monospace"
c.fonts.tabs                = "8pt monospace"

# Search engines
c.url.searchengines.update({
    'duck':     'https://duckduckgo.com/?q={}&ia=web',
    'gg':       'https://www.google.de/search?q={}',
    'arch':     'https://wiki.archlinux.org/index.php?search={}',
    'clang':    'https://duckduckgo.com/?q=\site:clang.llvm.org/doxygen+{}',
    'llvm':     'https://duckduckgo.com/?q=\site:llvm.org/doxygen+{}',
    'aio':      'http://www.aiosearch.com/search/4/Torrents/{}/',
    'we':       'https://en.wikipedia.org/wiki/{}',
    'cpp':      'http://en.cppreference.com/mwiki/index.php?search={}',
    'amazon':   'https://smile.amazon.de/s/ref=nb_sb_noss_2?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&url=search-alias%3Daps&field-keywords={}',
    'dblp':     'http://dblp.uni-trier.de/search?q={}',
    })

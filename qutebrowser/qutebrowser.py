import math
import re
import subprocess
import sys


def round_to_nearest_in_list(value, values_list):
    """
    Round a value to the nearest value in a given list.

    Args:
        value: The value to round
        values_list: List of values to round to

    Returns:
        The value from values_list that is closest to the input value
    """
    if not values_list:
        raise ValueError("values_list cannot be empty")

    # Find the value with minimum absolute difference
    return min(values_list, key=lambda x: abs(x - value))


def get_display_dpi():
    """
    Get the display DPI (dots per inch) from X resources.

    Uses xrdb to query the Xft.dpi value from X resources. This is used
    to determine appropriate scaling for UI elements and fonts.

    Returns:
        float: The detected DPI value, or 96 (default value) if detection fails
    """
    try:
        # Run `xrdb -query` to get X resources
        output = subprocess.check_output(['xrdb', '-query'], text=True)

        # Search for Xft.dpi value
        match = re.search(r'Xft.dpi:\s*(\d+)', output)
        if match:
            return float(match.group(1))
    except subprocess.CalledProcessError as e:
        print(sys.stderr, "Failed to run xrdb:", e)
    else:
        print(sys.stderr, "Falling back to default 96 DPI")
        return 96


def get_display_resolution():
    """
    Get the current display resolution.

    Returns:
        tuple: (width, height) in pixels, or `None` if detection fails
    """
    try:
        # Try xrandr first
        output = subprocess.check_output(['xrandr'], text=True)
        match = re.search(r' connected.* (\d+)x(\d+)', output)
        if match:
            return (int(match.group(1)), int(match.group(2)))

        # Fallback to xdpyinfo
        output = subprocess.check_output(['xdpyinfo'], text=True)
        match = re.search(r'dimensions:\s*(\d+)x(\d+)', output)
        if match:
            return (int(match.group(1)), int(match.group(2)))
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(sys.stderr, "Failed to detect display resolution:", e)

    return None


def compute_desired_zoom_factor(width, height, dpi):
    """
    Compute the optimal zoom factor based on display dimensions and DPI.

    The goal is to maintain consistent physical text size across different displays.
    This implementation considers:
    - Physical display size (calculated from resolution and DPI)
    - Viewing distance (estimated from display size)
    - Target physical text size for readability

    Args:
        width: Display width in pixels
        height: Display height in pixels
        dpi: Display DPI (dots per inch)

    Returns:
        Optimal zoom factor as a percentage (rounded to nearest preferred value)
    """
    # List of standard zoom factors supported by most browsers
    preferred_zoom_factors = [25, 33, 50, 67, 75, 90, 100, 110, 125, 150, 175, 200]

    # Calculate physical display dimensions in inches
    physical_width_inches = width / dpi
    physical_height_inches = height / dpi
    diagonal_inches = math.sqrt(physical_width_inches**2 + physical_height_inches**2)

    # Reference DPI (standard desktop DPI)
    reference_dpi = 96

    # Base zoom calculation: scale proportionally to DPI
    # This ensures that 1 CSS pixel maintains consistent physical size
    # NOTE: QT_AUTO_SCREEN_SCALE_FACTOR already normalizes for the DPI
    base_zoom = 100  # (dpi / reference_dpi) * 100

    # Apply display size adjustment factor
    # Smaller displays (laptops) typically need less zoom than larger displays (monitors)
    # because they're viewed from closer distances
    if diagonal_inches < 13:  # Small laptop
        size_factor = 0.75
    elif diagonal_inches < 15:  # Standard laptop
        size_factor = 0.80
    elif diagonal_inches < 20:  # Large laptop / small monitor
        size_factor = 0.85
    elif diagonal_inches < 24:  # Standard monitor
        size_factor = 1.0
    elif diagonal_inches < 27:  # Large monitor
        size_factor = 1.00
    else:  # Very large monitor
        size_factor = 1.10

    # Apply aspect ratio adjustment
    # Ultra-wide displays may benefit from slightly different scaling
    aspect_ratio = width / height
    if aspect_ratio > 2.0:  # Ultra-wide display
        aspect_factor = 1.05
    else:
        aspect_factor = 1.0

    # Calculate final zoom factor
    zoom_factor = base_zoom * size_factor * aspect_factor

    # Apply reasonable bounds
    zoom_factor = round_to_nearest_in_list(zoom_factor, preferred_zoom_factors)

    print(f'Display diagonal: {diagonal_inches:.1f}" | Base zoom: {base_zoom:.0f}% | '
          f'Size factor: {size_factor} | Final zoom: {zoom_factor:.0f}%\n')
    sys.stdout.flush()
    sys.stderr.flush()

    # Round to the nearest preferred zoom factor
    return zoom_factor


# Given the display \p dpi, computes and returns the default font size using a simple linear equation of the form
#
#   m * dpi + n
#
# Values *m* and *n* are determined by collecting desired font sizes for different display DPIs, building a set of
# *(dpi, pt)* points, and then fitting the model to these points.
#
# NOTE: The font size is relative to the zoom factor.  First, tune your zoom factor to your liking.  Only when you are
# satisfied with the zoom factor, start tuning the font size.
def compute_ui_font_size(width, height, dpi):
    # 169 dpi ⇒ 8 pt
    # 69 dpi ⇒ 13 pt
    return round(-.05 * dpi + 16.45)


def configure():
    global c, config

    width, height = get_display_resolution()
    dpi = get_display_dpi()
    print(f'Display of {width}x{height} has {dpi} DPI')
    default_font_size = compute_ui_font_size(width, height, dpi)
    # print(f'default font size: {default_font_size}')
    large_font_size = default_font_size + 1
    larger_font_size = default_font_size + 2

    ####################################################################################################################
    #
    # Config starts here
    #
    ####################################################################################################################
    config.load_autoconfig()

    config.set('qt.args', [
        'ignore-gpu-blocklist',
        'enable-gpu-rasterization',
        'enable-accelerated-video-decode',
        'enable-quic',
        'enable-zero-copy',
    ])

    # Set these variables to use NVIDIA GPU specifically
    c.qt.force_software_rendering = 'none'  # Don't force software rendering
    c.qt.chromium.process_model = 'process-per-site-instance'  # More efficient process model

    # Turn on QT HighDPI scaling.
    c.qt.highdpi = True

    c.statusbar.show = 'in-mode'  # use this setting once the weird "jump-to-top" behaviour is fixed
    # c.statusbar.show = 'always'
    c.tabs.show = 'multiple'

    c.tabs.pinned.frozen = False

    c.colors.webpage.preferred_color_scheme = 'dark'
    #  c.colors.wegpage.darkmode.policy.images = 'smart'

    # Zoom factor
    # Enable Qt auto scaling by globally setting QT_AUTO_SCREEN_SCALE_FACTOR=1 (e.g. in /etc/profile)
    preferred_zoom_factor = compute_desired_zoom_factor(width, height, dpi)
    c.zoom.default = f'{preferred_zoom_factor:.0f}%'

    # Fonts
    c.fonts.web.family.fixed        = 'Source Code Pro'
    c.fonts.web.family.serif        = 'Times New Roman'
    c.fonts.web.family.sans_serif   = 'Helvetica'
    c.fonts.web.family.standard     = 'Helvetica'
    c.fonts.web.size.default = 13  # default_font_size
    c.fonts.web.size.default_fixed = 13  # default_font_size
    c.fonts.web.size.minimum = 11  # int(.8 * default_font_size)

    c.fonts.completion.category = f'bold {large_font_size}pt Source Code Pro'
    c.fonts.completion.entry    = f'{default_font_size}pt Source Code Pro'
    c.fonts.debug_console       = f'{default_font_size}pt Source Code Pro'
    c.fonts.downloads           = f'{default_font_size}pt Helvetica'
    c.fonts.hints               = f'bold {large_font_size}pt Source Code Pro'
    c.fonts.keyhint             = f'{large_font_size}pt Helvetica'
    c.fonts.messages.error      = f'{default_font_size}pt Helvetica'
    c.fonts.messages.info       = f'{default_font_size}pt Helvetica'
    c.fonts.messages.warning    = f'{default_font_size}pt Helvetica'
    c.fonts.prompts             = f'{larger_font_size}pt Helvetica'
    c.fonts.statusbar           = f'{default_font_size}pt Source Code Pro'
    c.fonts.tabs.selected       = f'{default_font_size}pt Helvetica'
    c.fonts.tabs.unselected     = f'{default_font_size}pt Helvetica'

    c.tabs.padding              = dict(bottom = 1, top = 2, left = 5, right = 5)
    c.statusbar.padding         = dict(bottom = 1, top = 4, left = 5, right = 0)

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

    # SSL/TLS Certificate Error Handling
    c.content.tls.certificate_errors = 'ask-block-thirdparty' # ask for page loads with errors, automatically block resource loads

    config.bind(',b', 'config-cycle content.blocking.enabled true false')
    c.content.blocking.adblock.lists.extend([
        'https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters-2023.txt',
        'https://raw.githubusercontent.com/bogachenko/fuckfuckadblock/master/fuckfuckadblock.txt',
    ])

    # Notifications
    c.content.notifications.presenter = 'libnotify'

    # Request sites to reduce non-essential motions
    c.content.prefers_reduced_motion = True

    # No autoplay
    c.content.autoplay = False

    # Persist insert mode for each tab
    c.tabs.mode_on_change = 'restore'

    # Set hint characters for Colemak Mod-DH layout
    c.hints.chars = 'awftnuyorsei'

    # Search engines
    c.url.searchengines.update({
        'DEFAULT':  'https://www.google.de/search?q={}',
        # 'cpp':      'http://en.cppreference.com/mwiki/index.php?search={}',
        'acm':      'https://dl.acm.org/results.cfm?query={}',
        'aio':      'http://www.aiosearch.com/search/4/Torrents/{}/',
        'amazon':   'https://smile.amazon.de/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords={}',
        'arch':     'https://wiki.archlinux.org/index.php?search={}',
        'clang':    'https://duckduckgo.com/?q=\\site:clang.llvm.org/doxygen+{}',
        'cpp':      'https://duckduckgo.com/?q=\\site:en.cppreference.com+{}',
        'dblp':     'https://dblp.uni-trier.de/search?q={}',
        'dhl':      'https://www.dhl.de/en/privatkunden/pakete-empfangen/verfolgen.html?piececode={}',
        'dict':     'https://www.dict.cc/?s={}',
        'duck':     'https://duckduckgo.com/?q={}&ia=web',
        'duden':    'https://www.duden.de/suchen/dudenonline/{}',
        'eco':      'https://www.ecosia.org/search?q={}',
        'fa':       'https://fontawesome.com/search?q={}&o=r',
        'gg':       'https://www.google.de/search?q={}',
        'ghub':     'https://github.com/search?q={}',
        'gs':       'https://scholar.google.de/scholar?q={}',
        'guru':     'https://app.getguru.com/search?query={}',
        'hy':       'https://www.hyphenation24.com/word/{}/',
        'intrin':   'https://software.intel.com/sites/landingpage/IntrinsicsGuide/#text={}',
        'leo':      'https://dict.leo.org/german-english/{}',
        'ling':     'https://www.linguee.com/english-german/search?source=auto&query={}',
        'llvm':     'https://duckduckgo.com/?q=\\site:llvm.org/doxygen+{}',
        'map':      'https://www.google.com/maps/place/{}',
        'nzb':      'https://www.binsearch.info/?q={}&max=250&adv_age=1100&server=',
        'py':       'https://docs.python.org/3/search.html?q={}&check_keywords=yes',
        'steamdb':  'https://steamdb.info/search/?a=app&q={}',
        'stock':    'https://www.finanzen.net/suchergebnis.asp?_search={}',
        'tex':      'https://duckduckgo.com/?q=\\site:www.weinelt.de/latex/+{}',
        'wd':       'https://de.wikipedia.org/wiki/{}',
        'we':       'https://en.wikipedia.org/w/index.php?search={}&fulltext=1',
        'wolfram':  'https://www.wolframalpha.com/input/?i={}',
        'yt':       'https://www.youtube.com/results?search_query={}',
        })

    # External Editor
    c.editor.command = ['/usr/bin/neovide', '{}']

    c.aliases = {
        'l': 'session-load',
        'w': 'session-save',
    }
    config.bind('<Ctrl-q>', 'session-save ;; quit')

    # Temporarily grant JS access to the clipboard
    config.bind('<Space>sc', 'set -t content.javascript.clipboard access ;; message-warning "Clipboard enabled for 10 seconds" ;; cmd-later 10s set content.javascript.clipboard none ;; cmd-later 10s message-warning "Clipboard disabled"')

    # Tab-give
    config.bind('<Space>tgn', 'tab-give')       # new window
    config.bind('<Space>tg0', 'tab-give 0')     # window 0
    config.bind('<Space>tg1', 'tab-give 1')     # window 1

    # Toggle dark mode
    config.bind('<Space>d', 'config-cycle colors.webpage.darkmode.enabled true false')


    ########################################################################################################################
    ###     Per-website configs
    ###
    ### These changes are re-applied whenever the tab is revisited (not just when it's opened).
    ########################################################################################################################

    # Slack Web App
    config.set('input.mode_override', 'passthrough', 'app.slack.com')

    # Google Apps
    config.set('input.mode_override', 'passthrough', 'docs.google.com')
    config.set('input.mode_override', 'passthrough', 'meet.google.com')


configure()

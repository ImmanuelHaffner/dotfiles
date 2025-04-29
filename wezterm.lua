-- Pull in the wezterm API
local wezterm = require'wezterm'

function os.capture(cmd)
    local instream = assert(io.popen(cmd, 'r'))
    local outstream = assert(instream:read('*a'))
    instream:close()
    return outstream
end

local function compute_font_size(dpi)
    -- 169 dpi ⇒ 8 pt
    -- 69 dpi ⇒ 13 pt
    return math.floor(-.05 * dpi + 16.45 + .5)  -- +.5 to round
end

-- This table will hold the configuration.
local config = {}

local dpi = os.capture[[xrdb -query | grep Xft.dpi | awk '{print $2}']]

-- In newer versions of wezterm, use the config_builder which will
-- help provide clearer error messages
if wezterm.config_builder then
    config = wezterm.config_builder()
end

-- This is where you actually apply your config choices
config.font = wezterm.font("Source Code Pro", {weight="Regular", stretch="Normal", style="Normal"}) -- /usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf, FontConfig
config.font_size = compute_font_size(dpi)
config.warn_about_missing_glyphs = false

-- config.color_scheme = 'Solarized Dark (Gogh)'
-- config.color_scheme = 'Nightfly (Gogh)'
config.color_scheme = 'NightOwl (Gogh)'
config.colors = {  -- patch Solarized Dark (Gogh) theme: make character under cursor visible
    cursor_bg = '#2d3a4a',
}

-- Configure window padding.
config.window_padding = {
    left = 0,
    right = 0,
    top = 0,
    bottom = 0,
}

-- Configure tab bar. (Must come after setting color scheme and font.)
config.enable_tab_bar = false

-- Chainging the font size adjusts the rows/columns, not the window size.
config.adjust_window_size_when_changing_font_size = false

-- Configure hyperlinks
config.hyperlink_rules = wezterm.default_hyperlink_rules()

-- Configure bindings
config.mouse_bindings = {
    -- Disable copy on select
    {
        event = { Up = { streak = 1, button = 'Left' } },
        mods = 'NONE',
        action = wezterm.action.DisableDefaultAssignment,
    },

    -- Ctrl-click will open the link under the mouse cursor
    {
        event = { Up = { streak = 1, button = "Left" } },
        mods = "CTRL",
        action = wezterm.action.OpenLinkAtMouseCursor,
    },
    -- Disable the Ctrl-click down event to stop programs from seeing it when a URL is clicked
    {
        event = { Down = { streak = 1, button = "Left" } },
        mods = "CTRL",
        action = wezterm.action.Nop,
    },
}

-- and finally, return the configuration to wezterm
return config

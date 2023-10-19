-- Pull in the wezterm API
local wezterm = require 'wezterm'

-- This table will hold the configuration.
local config = {}

-- In newer versions of wezterm, use the config_builder which will
-- help provide clearer error messages
if wezterm.config_builder then
  config = wezterm.config_builder()
end

-- This is where you actually apply your config choices
config.font = wezterm.font("Source Code Pro", {weight="Regular", stretch="Normal", style="Normal"}) -- /usr/share/fonts/adobe-source-code-pro/SourceCodePro-Regular.otf, FontConfig
config.font_size = 10
config.warn_about_missing_glyphs = false

config.color_scheme = 'Solarized Dark (Gogh)'
config.colors = {  -- patch Solarized Dark (Gogh) theme: make character under cursor visible
    cursor_fg = '#002B36',
}
-- config.color_scheme = 'Solarized (dark) (terminal.sexy)'
-- config.color_scheme = 'Solarized Dark - Patched'
-- config.color_scheme = 'Solarized Dark Higher Contrast'

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

-- and finally, return the configuration to wezterm
return config

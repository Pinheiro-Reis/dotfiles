---@type ChadrcConfig
local M = {}

M.base46 = {
	theme = "pastelbeans",
  transparency = true,
	hl_override = {
		Comment = { italic = true },
		["@comment"] = { italic = true },
	},
}
M.term = { }
M.nvdash = { load_on_startup = true }
M.ui = {
    tabufline = {
         lazyload = false
    },
    cmp = {
      lspkind_text = true,
      style = "default", -- default/flat_light/flat_dark/atom/atom_colored
      format_colors = {
         tailwind = true,
      },
    },
}
M.colorify = { enabled = true }

return M

local g = vim.g
local o = vim.o
local opt = vim.opt

g.mapleader = " "
g.maplocalleader = "\\"

-- Transparency
--vim.cmd [[
--  highlight Normal guibg=none
--  highlight NonText guibg=none
--  highlight Normal ctermbg=none
--  highlight NonText ctermbg=none
--]]

o.termguicolors = true

-- No need to save when switching buffers
o.hidden = true

-- Decrease update time
o.timeoutlen = 500
o.updatetime = 200

-- Number of screen lines to keep above and below the cursor
o.scrolloff = 8

-- Better editor UI
o.number = true
o.numberwidth = 2
o.relativenumber = false
o.signcolumn = "yes"
o.cursorline = true

-- Better editing experience
o.expandtab = true
o.smarttab = true
o.cindent = true
o.autoindent = true
o.wrap = true
o.textwidth = 300
o.tabstop = 4
o.shiftwidth = 4
o.softtabstop = -1 -- If negative, shiftwidth value is used

-- Makes neovim and host OS clipboard play nicely with each other
o.clipboard = "unnamedplus"

-- Case insensitive searching UNLESS /C or capital in search
o.ignorecase = true
o.smartcase = true

-- Better buffer splitting
o.splitright = true
o.splitbelow = true

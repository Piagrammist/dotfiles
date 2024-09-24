return {
    {
        "tiagovla/tokyodark.nvim",
        priority = 1000,
        config = function()
            --require("tokyodark").setup()
            vim.cmd [[ colorscheme tokyodark ]]
        end,
    },
    {
        "nvim-telescope/telescope.nvim",
        dependencies = { "nvim-lua/plenary.nvim" },
        config = function()
            --require("telescope").setup()
            local telescope = require("telescope.builtin")
            vim.keymap.set("n", "<C-p>", telescope.find_files, {})
            vim.keymap.set("n", "<leader>fg", telescope.live_grep, {})
        end,
    },
    {
        "nvim-treesitter/nvim-treesitter",
        build = ":TSUpdate",
        config = function()
            require("nvim-treesitter.configs").setup({
                ensure_installed = {
                    "bash",
                    "c",
                    "comment",
                    "cpp",
                    "css",
                    "gitignore",
                    "html",
                    "javascript",
                    "json",
                    "lua",
                    "markdown",
                    "markdown_inline",
                    "php",
                    "printf",
                    "python",
                    "regex",
                    "rust",
                    "sql",
                    "typescript",
                    "vim",
                    "yaml",
                },
                auto_install = true,
                highlight = { enable = true },
                indent = { enable = true },
            })
        end,
    },
}

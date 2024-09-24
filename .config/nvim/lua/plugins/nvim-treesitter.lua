return {
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
}

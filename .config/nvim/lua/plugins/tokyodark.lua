return {
    "tiagovla/tokyodark.nvim",
    priority = 1000,
    opts = {
        transparent_background = true,
        styles = {
            comments = { italic = false },
            keywords = { italic = false },
            identifiers = { italic = false },
            functions = {},
            variables = {},
        },
    },
    config = function(_, opts)
        require("tokyodark").setup(opts)
        vim.cmd [[ colorscheme tokyodark ]]
    end,
}

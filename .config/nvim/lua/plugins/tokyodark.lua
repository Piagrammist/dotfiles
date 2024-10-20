return {
    "tiagovla/tokyodark.nvim",
    priority = 1000,
    opts = {
        transparent_background = true,
    },
    config = function(_, opts)
        require("tokyodark").setup(opts)
        vim.cmd [[ colorscheme tokyodark ]]
    end,
}

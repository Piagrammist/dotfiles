return {
    "tiagovla/tokyodark.nvim",
    priority = 1000,
    config = function()
        --require("tokyodark").setup()
        vim.cmd [[ colorscheme tokyodark ]]
    end,
}

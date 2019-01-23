if [ $(hostname) = "mdizg-pim" ] || [ $(hostname) = "Pims-MacBook-Pro.local" ] || [ $(hostname) = "mlres-pim" ]; then
    ZSH_DOTFILE_PATH="/Users/pbongaerts/Github/workflow/dotfiles/zsh"
elif [ $(hostname) = "deepcat1" ]; then
    ZSH_DOTFILE_PATH="/home/pbongaerts/workflow/dotfiles/zsh"
fi

# Environmental variables
echo "# ENVIRONMENTAL VARIABLES"
source $ZSH_DOTFILE_PATH/.env

# Oh My Zsh
echo "# OH MY ZSH"
source $ZSH/oh-my-zsh.sh

# Antigen
echo "# ANTIGEN"
source ~/.antigen/antigen.zsh
source $ZSH_DOTFILE_PATH/.antigen_settings

# Aliases
echo "# ALIASES"
source $ZSH_DOTFILE_PATH/.aliases

# Functions
echo "# FUNCTIONS"
source $ZSH_DOTFILE_PATH/.functions

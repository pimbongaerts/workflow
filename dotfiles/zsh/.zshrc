if [ $(hostname) = "mlizg-pim" ] || [ $(hostname) = "mlres-pim" ]; then
    ZSH_DOTFILE_PATH="/Users/pbongaerts/Github/workflow/dotfiles/zsh"
elif [ $(hostname) = "deepkat" ]; then
	ZSH_DOTFILE_PATH="/home/pbongaerts/Github/workflow/dotfiles/zsh"
elif [ $USERNAME = "deepcat" ]; then
    ZSH_DOTFILE_PATH="/home/deepcat/workflow/dotfiles/zsh"
elif [ $USERNAME = "pbongaerts" ]; then
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

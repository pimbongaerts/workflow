if [ $(hostname) = "mdizg-pim" ]; then
    ZSH_DOTFILE_PATH="/home/pbongaerts/Github/workflow/dotfiles/zsh"
elif [ $(hostname) = "deepcat1" ]; then
    ZSH_DOTFILE_PATH="/home/pbongaerts/workflow/dotfiles/zsh"
fi

# Environmental variables
source $ZSH_DOTFILE_PATH/.env

# General zsh settings
source $ZSH_DOTFILE_PATH/.zsh_settings

# Fonts
source ~/.fonts/*.sh

# Oh My Zsh
source $ZSH/oh-my-zsh.sh

# Antigen
source ~/.antigen/antigen.zsh
antigen use oh-my-zsh
source $ZSH_DOTFILE_PATH/.antigen_settings

# Aliases
source $ZSH_DOTFILE_PATH/.aliases

# Functions
source $ZSH_DOTFILE_PATH/.functions

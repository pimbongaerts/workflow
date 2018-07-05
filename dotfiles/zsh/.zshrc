ZSH_DOTFILE_PATH="/Users/pbongaerts/Github/workflow/dotfiles/zsh"

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

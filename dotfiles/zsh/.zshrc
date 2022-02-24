if [ $(hostname) = "mdizg-pim" ] || [ $(hostname) = "mlres-pim" ]; then
    ZSH_DOTFILE_PATH="/Users/pbongaerts/Github/workflow/dotfiles/zsh"
elif [ $USERNAME = "deepcat" ]; then
    ZSH_DOTFILE_PATH="/home/deepcat/workflow/dotfiles/zsh"
elif [ $(hostname) = "deepcat1" ] && [ $USERNAME = "pbongaerts" ]; then
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

if [ $(hostname) = "mdizg-pim" ] || [ $(hostname) = "mlres-pim" ]; then
	echo "# CONDA"
	# >>> conda initialize >>>
	# !! Contents within this block are managed by 'conda init' !!
	__conda_setup="$('/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
	if [ $? -eq 0 ]; then
	    eval "$__conda_setup"
	else
	    if [ -f "/miniconda3/etc/profile.d/conda.sh" ]; then
# . "/miniconda3/etc/profile.d/conda.sh"  # commented out by conda initialize
	    else
	        export PATH="/miniconda3/bin:$PATH"
	    fi
	fi
	unset __conda_setup
	# <<< conda initialize <<<
elif [ $USERNAME = "pbongaerts" ]; then
	# >>> conda initialize >>>
	# !! Contents within this block are managed by 'conda init' !!
	__conda_setup="$('/home/pbongaerts/CCG_installed_tools/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
	if [ $? -eq 0 ]; then
	    eval "$__conda_setup"
	else
	    if [ -f "/home/pbongaerts/CCG_installed_tools/anaconda3/etc/profile.d/conda.sh" ]; then
# . "/home/pbongaerts/CCG_installed_tools/anaconda3/etc/profile.d/conda.sh"  # commented out by conda initialize
	    else
# export PATH="/home/pbongaerts/CCG_installed_tools/anaconda3/bin:$PATH"  # commented out by conda initialize
	    fi
	fi
	unset __conda_setup
	# <<< conda initialize <<<
fi
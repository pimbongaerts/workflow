set laststatus=2	      " required for lightline
set nocompatible              " required for Vundle 
filetype off                  " required for Vundle 
set rtp+=~/.vim/bundle/Vundle.vim " required for Vundle 
set rtp+=~/.fzf
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'junegunn/fzf'
Plugin 'junegunn/fzf.vim'
Plugin 'itchyny/lightline.vim'
Plugin 'scrooloose/nerdtree'
Plugin 'editorconfig/editorconfig-vim'
call vundle#end()            " required
filetype plugin indent on    " required

map ; :Files<CR>
map <C-n> :NERDTreeToggle<CR>

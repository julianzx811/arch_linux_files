" Plugins will be downloaded under the specified directory.
call plug#begin(has('nvim') ? stdpath('data') . '/plugged' : '~/.vim/plugged')

" Declare the list of plugins.
Plug 'dracula/vim'
" List ends here. Plugins become visible to Vim after this call.
call plug#end()


colorscheme dracula

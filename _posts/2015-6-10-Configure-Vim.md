---
layout: post
title: Configure Vim
---

Basic vim setup

```
" For color schemes go to: https://github.com/flazz/vim-colorschemes

" Auto releading of .vimrc file
autocmd! bufwritepost .vimrc source %

" Syntax highlighting
filetype off
filetype plugin indent on
syntax on " Turn syntax highlighting on

" Showing line numbers and length
set number " show line numbers
set tw=79 " width of document
set nowrap " don't automatically wrap on Load
set fo-=t " don't automatically wrap text when typing
set colorcolumn=80
highlight ColorColumn ctermbg=DarkGrey guibg=grey

" Real programmers don't use tabs!! Use spaces!!!
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround
set expandtab

" Make search case insensitive
set hlsearch
set incsearch
set ignorecase
set smartcase

" Disable stupid backup and swap files - they trigger too many events
" for file system watchers
set nobackup
set nowritebackup
set noswapfile

" Setup Pathogen to manage your plugins
call pathogen#infect()
```

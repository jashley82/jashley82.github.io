---
layout: post
title: Powerline Vim And Tmux
---

Install powerline via pip.

```bash
sudo pip install powerline-status
```

Install font packages and regenerate font cache.

```bash
wget https://github.com/Lokaltog/powerline/raw/develop/font/PowerlineSymbols.otf 
wget https://github.com/Lokaltog/powerline/raw/develop/font/10-powerline-symbols.conf
sudo mv PowerlineSymbols.otf /usr/share/fonts/
sudo fc-cache -vf
sudo mv 10-powerline-symbols.conf /etc/fonts/conf.d/
```

Enable powerline in vim by updating ~/.vimrc.

```
set rtp+=/usr/local/lib/python2.7/dist-packages/powerline/bindings/vim/
set laststatus=2
set t_Co=256
```

Enable tmux by updating ~/.tmux.conf.

```
source /usr/local/lib/python2.7/dist-packages/powerline/bindings/tmux/powerline.conf
set-option -g default-terminal "screen-256color"
```

and in ~/.bashrc.

```
export TERM=xterm-256color

if [ -f /usr/local/lib/python2.7/dist-packages/powerline/bindings/bash/powerline.sh ]; then
    source /usr/local/lib/python2.7/dist-packages/powerline/bindings/bash/powerline.sh
fi  
```

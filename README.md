<!-- ```shell
dotfiles/
├── install.sh
├── config/
│   ├── nvim/
│   └── alacritty/
├── root/
│   └── .bashrc
├── efi/
│   └── custom-boot-entry.efi
``` -->
# Max's Dotfiles
Welcome to my Arch Linux configurations and styling. Below I will document the steps to repoduce these exact machine configurations on a clean install.

![Version](https://badgen.net/badge/color/0.1/orange?label=Version) 
![Dist](https://badgen.net/badge/color/Arch&nbsp;Linux/blue?label=Distribution)
![Dist](https://badgen.net/badge/color/Unstable/red?label=Stability)

## Table of Contents

1. [🐧TODO](#todo)
2. [💾 Installation](#installation)
1. [🍚 The Configs](#the-configs)

## 🐧 TODO
- [ ] Upgrade the file structure to [GNU Stow](https://www.gnu.org/software/stow/) for easier symlinks
- [ ] Finish dotfiles 

## 💾 Installation

**1**. Clone the repository

```shell
$ sudo git clone https://github.com/maxlair1/dotfiles.git ~/.dotfiles
```


## 🍚 The Configs

| PKG    | What do?       |
| ------ | -------------- |
| [bspwm](https://github.com/baskerville/bspwm)  | Tiling Window Manager|
| [sxhkd](https://wiki.archlinux.org/title/Sxhkd)| Keybind Manager      |
| [kitty](https://sw.kovidgoyal.net/kitty/)      | Terminal Emulator    |
| [neovim](https://neovim.io/), [nano](https://www.nano-editor.org/), [Zed](https://zed.dev/)| Code Editors (use based on scale)|
| [picom](https://github.com/yshui/picom)                                                           | [X ](https://wiki.archlinux.org/title/Xorg) based compositor (for shadows) |
| [ranger](https://github.com/ranger/ranger)                                                        | File manager                                                               |
| [polybar](https://github.com/polybar/polybar)                                                     | Status bar                                                                 |
| [dunst](https://github.com/dunst-project/dunst) [this fork](https://github.com/Barbaross93/dunst) | Notification [daemon](https://en.wikipedia.org/wiki/Daemon_(computing))    |
| [rofi](https://github.com/davatorium/rofi) & [dmenu](https://wiki.archlinux.org/title/Dmenu)      | Menus and application launchers |                                                    

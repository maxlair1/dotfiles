```
                             __      __      
   ____ ___  ____ __  ______/ /___  / /______
  / __ `__ \/ __ `/ |/_/ __  / __ \/ __/ ___/
 / / / / / / /_/ />  </ /_/ / /_/ / /_(__  ) 
/_/ /_/ /_/\__,_/_/|_|\__,_/\____/\__/____/                                              
```

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
- [ ] Setup Display server ([xorg](https://wiki.archlinux.org/title/Xorg))
- [x] Cool wallpaper (`feh`)
- [x] Picom [animations](https://gitlab.com/Zaney/picom)
- [ ] Fix Kitty [line wrap overwrite](https://github.com/kovidgoyal/kitty/issues/2023)
- [ ] T480 Configs
    - [x] Fingerprint Reader for Login
    - [x] Make trackpad feel and [work better](https://wiki.archlinux.org/title/Touchpad_Synaptics)
    - [ ] Natural Scrolling
    - [ ] Screen/display control (i.e. scale & brightness)
    - [ ] Keyboard backlight
- [ ] Upgrade the file structure to [GNU Stow](https://www.gnu.org/software/stow/) for [easier symlinks](https://www.jakewiesler.com/blog/managing-dotfiles)
- [ ] Finish dotfiles

## 💾 Installation
> [!CAUTION]
> These dotfiles are not yet configured.

**1**. Clone the repository
```shell
$ sudo git clone https://github.com/maxlair1/dotfiles.git ~/.dotfiles # name whatever you like
```

**2**. `cd` into cloned repository
```shell
$ cd ~/.dotfiles # change to whatever you named the folder
```

**?**. Run the `install` scripts to hook everything up
```shell
$ install-pacman.sh && install.sh

# Example of structure → symlinks
# dotfiles/
# ├── install.sh
# ├── install-pacman.sh
# ├── config/     → ~/.config/*
# ├── home/       → ~/.* like .zshrc, .gitconfig
# ├── efi/        → /boot/efi/*
# ├── packages/
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

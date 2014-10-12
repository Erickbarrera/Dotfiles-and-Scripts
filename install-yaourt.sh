#!/bin/bash

echo Updating repos...
sudo pacman -Syy
echo Installing dependencies fakeroot and base-devel...
sudo pacman --noconfirm base-devel fakeroot

echo Downloading package-query...
wget https://aur.archlinux.org/packages/pa/package-query-git/package-query-git.tar.gz
tar -xvf package-query-git.tar.gz
cd package-query-git
makepkg -s -f
sudo pacman -U --noconfirm package-query-git-*-*.pkg.tar.xz
cd ..
echo package-query installed...

wget https://aur.archlinux.org/packages/ya/yaourt-git/yaourt-git.tar.gz
tar -xvf yaourt-git.tar.gz
cd yaourt-git
makepkg -s -f
sudo pacman -U --noconfirm yaourt-git-*-*.pkg.tar.xz
cd ..
echo yaourt instaled...
echo Done.

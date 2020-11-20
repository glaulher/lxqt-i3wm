# Dotfiles
xbps-install -Suv
xbps-install -S dbus elogind 
xbps-install -Sy void-repo-nonfree void-repo-multilib
xbps-install xorg-minimal mesa-intel-dri xf86-video-intel xorg-input-drivers vulkan-loader mesa-vulkan-intel intel-video-accel
xbps-install setxkbmap ntfs-3g linux-firmware linux-firmware-intel  intel-ucode
xbps-reconfigure -f linux
ln -s /etc/sv/dbus /var/service
ln -s /etc/sv/elogind /var/service

xbps-install -S lxqt nano Adapta papirus-icon-theme breeze-cursors qt5-styleplugins picom font-firacode fonts-roboto-ttf font-awesome
xbps-install -S pulseaudio pavucontrol-qt alsa-plugins-pulseaudio alsa-utils squashfs-tools xrdb xkill gvfs 
xbps-install -S geany firefox-i18n-pt-BR ranger trash-cli mpv feh lrzip unzip zip p7zip-unrar p7zip wicd-gtk

***

# gpg

sudo xbps-install xtools (if you don't have it)

$ xlocate -S (this needs to be periodically, it'll tell you when)

$ xlocate bin/gpg

***

> add tray icon weather

> https://github.com/dglent/meteo-qt

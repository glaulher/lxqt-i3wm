vi .xinitrc
startx
sudo shutdown -h now
startx
ls -a
nano .xinitrc
ls /etc/sv
ls /var/service
sudo rm -rf /var/service/dhcpcd
sudo ln -s /etc/sv/wicd /var/service/
sudo ln -s /etc/sv/dbus /var/service/
sudo ln -s /etc/sv/elogind /var/service/
sudo reboot
startx
wicd
sudo wicd
wicd-curses
clear
sudo xbps-install -f xorg xinit lxqt
startx
sudo xbps-install lxdm
sudo reboot
ls /var/service/
ls /etc/sv
sudo ln -s /etc/sv/polkitd /var/service/
ls /var/service/
sudo ln -s /etc/sv/lxdm /var/service/
free -h
wicd-curses
free -h
sudo lxqt
sudo pcmanfm
sudo pcmanfm-qt
sudo pcmanfm-qt
sudo xbps-install lxqt-sudo
sudo pcmanfm-qt
sudo dbus-launch pcmanfm-qt
ls
nano lxqt-archiver.desktop
sudo xbps-install pavulcontrol pulseaudio alsa-plugins-pulseaudio alsa-utils
sudo xbps-install pavucontrol pulseaudio alsa-plugins-pulseaudio alsa-utils
sudo xbps-query 
notify-send oi
sudo xbps-install -Rs zip unzip rar 7zip
sudo xbps-install -Rs zip unzip 7zip
sudo xbps-install -Rs zip unzip 
sudo xbps-query -Rs awesome
sudo xbps-install -Rs font-awesome5
sudo xbps-query -Rs monaco
sudo xbps-install -Rs geany
startx
sudo xbps-install -Rs dbus-elogind
ls /etc/sv
free -h
free -h
startx
free -h
startx
sudo reboot
sudo ln -s /etc/sv/rtkit /var/service/
free -h
startx
sudo reboot
ls /var/service/
sudo rm -rf /var/service/lxdm
ls /var/service/
sudo ln -s /etc/sv/dbus /var/service/
sudo reboot
fc-cache -vf 
lxqt-config-monitor --help
sudo rm -rf /var/service/elogind
sudo rm -rf /var/service/dbus
sudo ln -s /etc/sv/dbus /var/service/
sudo ln -s /etc/sv/elogind /var/service/
sudo sv start dbus
sudo sv start elogind
startx
sudo reboot
sudo xbps-install -Rs dbus
sudo reboot
sudo xbps-install -Rs polkit
sudo xbps-query -Rs polkit
sudo xbps-query -Rs lxqt
sudo xbps-install -S polkit
sudo xbps-install -S -f polkit
sudo xbps-query -Rs lxqt
sudo xbps-install -S xf86-video-intel
sudo shutdown -h now

xrdb -load ~/.Xresources


#Sem beeps chatos
xset -b

#Iniciar o i3
#exec ck-launch-session dbus-launch --sh-syntax --exit-with-session i3
exec dbus-launch --sh-syntax --exit-with-session startlxqt

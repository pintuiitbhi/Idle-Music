# Idle-Music
A python script to play music when system is inactive for some minute (as time defined by the user). 
The script automatically starts when the screensaver of Ubuntu starts.The music is played in VLC.

### [Update.py](https://github.com/pintuiitbhi/Idle-Music/blob/master/playSong.py)
It is used to update the song list played by user in VLC. The songs name is saved in a text file and its frequency
is updated whenever it is played. If song is new then it is added.

### [playSong.py](https://github.com/pintuiitbhi/Idle-Music/blob/master/playSong.py)
This file is used to play the random song( song which is most liked by user) which is already saved in the text file when
system is inactive for some minutes.

Both file is made executable and their shortcut (**.desktop** file) is placed in the **autostart** folder of Ubuntu. This will
ensure that whenever system reboots it will automatically starts the script. 
**To make the files executable** :
  ```
  chmode +x update.py
  chmode +x playSong.py
  ```
  
### Create "playSong.desktop" file 
Include the following content in the file. Save the file with extension **.desktop**. This file will 
act as a shortcut to the python script file **"playSong.py"**
```
[Desktop Entry]
Name = IdlePlay
Version = 1.0
Comment = Song playing during screensaver
Encoding = UTF-8
Exec = python /home/pintu/IdleMusic/playSong.py
Icon = /home/pintu/IdleMusic/icon.png
Type = Application
```
**Caution:** The python script file "playSong.py" complete address should be written in **"Exec = "**. Here I have written according to my 
own address of the file *"/home/pintu/IdleMusic/playSong.py"* ( *I have saved the file in folder "IdleMusic"* ).

### Create "update.desktop" file
Include the following content in the file. Save the file with extension **.desktop**. This file will 
act as a shortcut to the python script file **"Update.py"**
```
[Desktop Entry]
Name = IdleMusic
Version = 1.0
Encoding = UTF-8
Comment = Idle Music
Exec = python /home/pintu/IdleMusic/update.py
Icon = /home/pintu/IdleMusic/icon.png
Terminal = false
Type = Application
```
**Caution:** Here also the python script file update.py complete address should be written in **"Exec = "**. Here I have written according to my 
own address of the file *"/home/pintu/IdleMusic/update.py"* ( *I have saved the file in folder "IdleMusic"*).

Make both of these files as executable also using the command
  ```chmod +x ```

Now after creating those **.desktop** files, move them to folder **"~/.config/autostart"**  like
  ```
  sudo mv idlemusic.desktop ~/.config/autostart
  ```
  
In order to check whether  script works. First reboot the system. Then active the screensaver to see the effect of script.
Use the following command in terminal:
```
gnome-screensaver-command -a
```
As the screensaver starts VLC will starts playing random music and stop after playing a song. Instead of songs you can play any
music. Just you have to save the path of music file in the list of songs text file.

  

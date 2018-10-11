#! /usr/bin/env python
import os,time
#return the path of song currently playing otherwise return 'None'
def song_path():
    try:
        pid=os.popen("pgrep -x vlc")  # finding the VLC process ID
    except ValueError:
        return ''
    q=pid.read()
    q=q.strip() # removing whitespaces from end of string
    process= os.popen("readlink /proc/"+str(q)+"/fd/*") # all file descriptors of vlc
    s=process.read()
    #print(s)
    extension=['.mp3','.aac','.wma','.wav']

    ''' if songs with type available in 'extension'
        is found playing the return its path
    '''
    for item in s.split("\n"):
        check = ".mp3" in item or ".aac" in item or ".wma" in item or ".wav" in item
        if check:
            song_path = item.strip() + '\n'
            return song_path
            #print(song_path)

def song_update():
    '''Saving the song path in a file'''

    file = open("/home/pintu/.song_list.txt",'r+') #opening the song file
    # if currently no song is playing then just close the file
    if song_path() != None:
        path = song_path().strip('\n') +"\n"
        data= file.readlines() # read the song file and return as list
#if song is already available in list then increase the frequency
        if path in data:
            file.seek(0) #pointer which points to the beginning of the file
            index = data.index(path) # index of song path in list
            freq= int(data[index-1].strip('\n')) + 1  # increase the frequency of song by 1
            data[index-1] = str(freq)+"\n"
            file.write(''.join(data))  #update the file
# if song is not present in file then write in the file
        else:
            file.write("1\n"+path.strip('\n')+"\n")

    file.close()


def main():
    processName = "vlc"
    while (True):
        song=''
        time.sleep(1)
        status = os.popen("pgrep -x vlc").read()
        current_song= song_path()
        #if vlc is running and a song is playing then 'while' will execute
        while (status !='' and current_song != None) :
            current_song= song_path()

            if song != current_song:
                song_update()
                song = current_song
            time.sleep(1)
            status = os.popen("pgrep -x vlc").read()


if __name__ == "__main__":
    main()

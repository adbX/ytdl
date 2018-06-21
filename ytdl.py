import os
import youtube_dl

#get links from text
results=[]
folders=[]

#note: '~' doesn't work, you'll need to use /home/.....
downloadpath="/home/adb/stuff/gdrive/ytdl/"
linkspath="/home/adb/stuff/projects/ytdl_links/links.txt"

with open(linkspath) as inputfile:
	for line in inputfile:
		head,sep,tail=line.partition('#')
		folders.append(tail.strip())
		results.append(head.strip()) 

ydl_opts = {
    'format': 'bestaudio',
    'extractaudio':True,
    'nooverwrites':True,
    'download_archive':'downloaded.txt',
    'outtmpl':'%(playlist_index)s-%(title)s.%(ext)s',
    'ignoreerrors':True,
    'postprocessors': [{
 	'key': 'FFmpegExtractAudio',
    'preferredcodec': 'best',
    'preferredquality': '192', 
    }],
}

j=0
os.chdir(downloadpath)
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	for folder in folders:

		if not os.path.exists(folder):
			os.makedirs(folder)

		os.chdir(folder)
		ydl.download([results[j]])
		os.chdir("../")
		j=j+1

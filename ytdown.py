from pytube import YouTube

url = 'Enter URL'
my_video = YouTube(url)

print("********************Download video*************************")
#get all the stream resolution for the 
for stream in my_video.streams:
    print(stream)

#set resolution to highest
my_video = my_video.streams.get_highest_resolution()


my_video.download('Specify Path to where you want to store downloaded video')

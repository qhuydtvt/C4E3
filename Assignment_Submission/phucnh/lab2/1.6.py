playlist=["chua bao gio","da em roi xa","tam su voi nguoi ta"]
print("My Playlist is:")
for i in range(0,3):
    print(str.format("{0} : {1}",i,playlist[i]))
    
song=input("Enter song name here: ");


if song.lower() in playlist:
    print("play")
else:
    print("no play")

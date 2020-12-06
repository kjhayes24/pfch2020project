import glob
import json
import random
#Create a new list for the lyrcis from the Lorde songs.
my_lyrics_list = []
for file in glob.glob('*.json'):
    data = json.load(open(file))

    print(data['lyrics'])
    split_list = (data['lyrics']).split("\n") 

    my_lyrics_list.append(split_list)

print(len(my_lyrics_list))
#Flatten the Lorde song and lyric data into one string.
flat_list = []
for song in my_lyrics_list:
    if type(song) is list:
            
        for line in song:
            flat_list.append(line)
    else:
        flat_list.append(song)

print(len(flat_list))
#Request random lines from new string of Lorde lyrics. Make sure range counts all lines.
for l in range(21): 
    print(flat_list[random.randrange(0,1268,1)])
#Create a new song from your custom arrangement of lyrics. 
generated_song = ""
for i in range (21):
    generated_song = generated_song + flat_list[random.randrange(0, 1268, 1)] + "\n"
#Save that custom song to a new text file. Make sure you add an additional _# to generated_song for each new song.
text_file = open("generated_song", "w")
text_file.write(generated_song)
text_file.close
    
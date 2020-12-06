import lyricsgenius
import json
#Make sure to get your API key from Genius before running the code.
genius = lyricsgenius.Genius("vZVuJZ30oA3QTaSwfqjhdn0ZzqPf76aET12v83bjIs2SUJkE4IU0E57BoSMsWNSx")
#Exclude which songs are pulled via exlcuding certain terms.
genius.excluded_terms = ["Remix", "Live"]

#So this project is essentially going to pull from Lorde lyrcis but you can choose any artist. Get their artist ID from Genius.
artist = genius.search_artist('36944', artist_id=36944, max_songs=20, per_page=5)
#Download lyrics into individual json files. You will extract lyrics from these files.
for song in artist.songs:
    data_json = song.to_json()
    data_dict = json.loads(data_json)
    filename =str(data_dict['id']) + '36944.json'

    with open(filename, 'w') as output:
        json.dump (data_dict, output, indent=2)

    #print(song.lyrics)
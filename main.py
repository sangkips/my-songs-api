from fastapi import FastAPI, status
from schema import Song, Artist
from typing import Optional, List
import models
from database import SessionLocal

app = FastAPI()

db = SessionLocal()

# Project root endpoint
@app.get('/')
async def root():
    return {'Message': 'Welcome to my Songs Library'}

##### Songs #####

# Retrieve all songs
@app.get('/songs', response_model=List[Song], status_code=status.HTTP_200_OK)
def get_songs():
    songs = db.query(models.Song).all()
    return songs

# Retrieve a single song
@app.get('/song/{song_id}', response_model=Song, status_code=status.HTTP_200_OK)
def get_one_song(song_id:int):
    song = db.query(models.Song).get(song_id)
    return song

# Create a song
@app.post('/create_song', response_model=Song, status_code=status.HTTP_201_CREATED)
def create_a_song(song:Song):
   new_song = models.Song(title=song.title, year=song.year, description=song.description, artist_id=song.artist_id)
   
   # add new song to the db using SessionLocal class
   db.add(new_song)

   # save the new song to the database
   db.commit()
   return new_song

# Update a song
@app.put('/update_song/song_id')
def update_a_song(song_id:int):
    pass


@app.delete('/song/{song_id}')
def delete_a_song(song_id:int):
    pass


##### Artist ######

# Retrieve all Artists
@app.get('/artists', response_model=List[Artist], status_code=200)
def get_all_artists():
    artists = db.query(models.Artist).all()
    return artists

# Retrieve a single Artist
@app.get('/artist/{artist_id}')
def get_one_artist(artist_id:int):
    pass

# Add an Artist
@app.post('/Add_artist', response_model=Artist, status_code=status.HTTP_201_CREATED)
def create_an_artist(artist:Artist):
   new_artist = models.Artist(name=artist.name)

   db.add(new_artist)
   db.commit()
   return new_artist 

# Update an Artist
@app.put('/update_artist/artist_id')
def update_an_artist(artist_id:int):
    pass

# Delete an Artist fro db
@app.delete('/artist/{artist_id}')
def delete_an_artist(artist_id:int):
    pass

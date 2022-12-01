from fastapi import FastAPI
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
@app.get('/songs', response_model=List[Song], status_code=200)
def get_songs():
    songs = db.query(models.Song).all()
    return songs

# Retrieve a single song
@app.get('/song/{song_id}')
def get_one_song(song_id:int):
    pass

# Create a song
@app.post('/create_song')
def create_a_song(): # pass the dictionary from the dummy data
   pass

# Update a song
@app.put('/update_song/song_id')
def update_a_song(song_id:int):
    pass


@app.delete('/song/{song_id}')
def delete_a_song(song_id:int):
    pass


##### Artist ######

# Retrieve all Artists
@app.get('/artists')
def get_all_artists():
    pass

# Retrieve a single Artist
@app.get('/artist/{artist_id}')
def get_one_artist(artist_id:int):
    pass

# Add an Artist
@app.post('/Add_artist')
def create_an_artist():
   pass

# Update an Artist
@app.put('/update_artist/artist_id')
def update_an_artist(artist_id:int):
    pass

# Delete an Artist fro db
@app.delete('/artist/{artist_id}')
def delete_an_artist(artist_id:int):
    pass

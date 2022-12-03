from fastapi import FastAPI, status, HTTPException
from schema import Song, Artist
from typing import Optional, List
import models
from database import SessionLocal

app = FastAPI()

db = SessionLocal()

# Project root endpoint


@app.get('/', tags=['Get'])
async def root():
    return {'Message': 'Welcome to my Songs Library'}

##### Songs #####

# Retrieve all songs


@app.get('/songs', tags=['Get'], response_model=List[Song], status_code=status.HTTP_200_OK)
def get_all_songs():
    songs = db.query(models.Song).all()
    return songs

# Retrieve a single song


@app.get('/song/{song_id}', tags=['Get'], response_model=Song, status_code=status.HTTP_200_OK)
def get_one_song(song_id: int):
    song = db.query(models.Song).filter(models.Song.id == song_id).first()
    return song

# Create a song


@app.post('/create_song', tags=['Post'], response_model=Song, status_code=status.HTTP_201_CREATED)
def create_a_song(song: Song):
    new_song = models.Song(title=song.title, year=song.year,
                           description=song.description, artist_id=song.artist_id)

    # add new song to the db using SessionLocal class
    db.add(new_song)

    # save the new song to the database
    db.commit()
    return new_song

# Update a song


@app.put('/update_song/song_id', tags=['Put'], response_model=Song, status_code=status.HTTP_200_OK)
def update_a_song(song_id: int, song: Song):
    song_to_be_updated = db.query(models.Song).filter(
        models.Song.id == song_id).first()
    song_to_be_updated.title = song.title  # for updating the title
    song_to_be_updated.year = song.year
    song_to_be_updated.description = song.description
    song_to_be_updated.artist_id = song.artist_id

    db.commit()  # save changes

    return song_to_be_updated

# delete a song from database


@app.delete('/song/{song_id}', tags=['Delete'],)
def delete_a_song(song_id: int):
    song_to_be_deleted = db.query(models.Song).filter(
        models.Song.id == song_id).first()
    if song_to_be_deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='That song is not found in the databse')
    db.delete(song_to_be_deleted)  # delete a song instance
    db.commit()  # save to the databse
    return {'message': 'The song has been deleted successfully'}


##### Artist ######

# Retrieve all Artists
@app.get('/artists', tags=['Get'], response_model=List[Artist], status_code=status.HTTP_200_OK)
def get_all_artists():
    artists = db.query(models.Artist).all()
    return artists

# Retrieve a single Artist


@app.get('/artist/{artist_id}', tags=['Get'], response_model=Artist, status_code=status.HTTP_200_OK)
def get_one_artist(artist_id: int):
    artist = db.query(models.Artist).filter(
        models.Artist.id == artist_id).first()
    return artist

# Add an Artist


@app.post('/Add_artist', tags=['Post'], response_model=Artist, status_code=status.HTTP_201_CREATED)
def create_an_artist(artist: Artist):
    new_artist = models.Artist(name=artist.name)

    db.add(new_artist)
    db.commit()
    return new_artist

# Update an Artist


@app.put('/update_artist/artist_id', tags=['Put'], response_model=Artist, status_code=status.HTTP_200_OK)
def update_an_artist(artist_id: int, artist: Artist):
    artist_to_be_updated = db.query(models.Artist).filter(
        models.Artist.id == artist_id).first()
    artist_to_be_updated.name = artist.name

    db.commit()
    return artist_to_be_updated

# Delete an Artist fro db


@app.delete('/artist/{artist_id}', tags=['Delete'],)
def delete_an_artist(artist_id: int):
    artist_to_be_deleted = db.query(models.Artist).filter(
        models.Artist.id == artist_id).first()

    if artist_to_be_deleted is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='The artist is not in the databse')

    db.delete(artist_to_be_deleted)
    db.commit()

    return {'Message': 'Artist has been successfully deleted'}

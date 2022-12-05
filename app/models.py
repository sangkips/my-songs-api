from app.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    songs = relationship('Song', back_populates='artist')


class Song(Base):
    __tablename__ = 'songs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer, index=True)
    description = Column(Text, index=True)

    artist_id = Column(Integer, ForeignKey('artists.id'))

    artist = relationship('Artist', back_populates='songs')

    # represent an object as a string

    def __repr__(self):
        return f'<Song title = {self.title} year={self.year}>'

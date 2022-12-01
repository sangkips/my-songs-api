from database import Base, engine
from models import Song, Artist

Base.metadata.create_all(engine)
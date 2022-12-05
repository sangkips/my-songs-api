from app.database import Base, engine
from app.models import Song, Artist

Base.metadata.create_all(engine)

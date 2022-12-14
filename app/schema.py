from pydantic import BaseModel


class Song(BaseModel):
    id: int
    title: str
    year: int
    description: str | None = None
    artist_id: int

    class Config:  # provides configuration to pydantic
        orm_mode = True


class Artist(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

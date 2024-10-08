from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

# executing the instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinok")

meta = MetaData()

# create variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Integer, primary_key=True),
    Column("Name", String)
)

# create variable for "Album" table
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))
)

# create variable for "Track" table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False),
    Column("GenreId", Integer, primary_key=False),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


with db.connect() as connection:

    # Query1 -select all records from the "Artist" table
     #select_query = artist_table.select()

     # Query 2 - select 
     select_query = artist_table.select().where(artist_table.c.Name == "Queen")
     # Query 3
     # select_query = artist_table.select().where(artist_table.c.Composer == "Queen")
     # Query 4
     select_query = track_table.select().where(track_table.c.Composer == "Queen")

     results = connection.execute(select_query)
     for result in results:
          print(result)
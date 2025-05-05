"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlists'
    
    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    
    # Relationship with songs (through playlist_songs)
    songs = db.relationship('Song', secondary='playlists_songs', back_populates='playlists')


class Song(db.Model):
    """Song."""
    __tablename__ = 'songs'
    
    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    
    # Relationship with playlists (through playlist_songs)
    playlists = db.relationship('Playlist', secondary='playlists_songs', back_populates='songs')
    
class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = 'playlists_songs'
    
    # Define columns
    id = db.Column(db.Integer, primary_key=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id', ondelete='CASCADE'), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey('songs.id', ondelete='CASCADE'), nullable=False)

    # Relationship between playlist and song
    playlist = db.relationship('Playlist', backref=db.backref('playlist_songs', cascade='all, delete-orphan'))
    song = db.relationship('Song', backref=db.backref('playlist_songs', cascade='all, delete-orphan'))

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

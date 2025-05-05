from app import app
from models import db, Playlist, Song, PlaylistSong

# Create all tables
with app.app_context():
    db.drop_all()
    db.create_all()

    # Create playlists
    p1 = Playlist(name="Chill Vibes", description="Relaxing music for the anytime")
    p2 = Playlist(name="Earth Mother", description="Songs that smell like patchouli and dirt.")

    # Create songs
    s1 = Song(title="Medicine", artist="Rising Appalachia")
    s2 = Song(title="Growing Things", artist="Shook Twins")
    s3 = Song(title="Everywhere, Everything", artist="Noah Kahan")
    s4 = Song(title="Swell Window", artist="Zee Avi")

    # Add to session
    db.session.add_all([p1, p2, s1, s2, s3, s4])
    db.session.commit()

    # Link songs to playlists
    ps1 = PlaylistSong(playlist_id=p1.id, song_id=s3.id)
    ps2 = PlaylistSong(playlist_id=p2.id, song_id=s2.id)
    ps3 = PlaylistSong(playlist_id=p2.id, song_id=s4.id)

    db.session.add_all([ps1, ps2, ps3])
    db.session.commit()

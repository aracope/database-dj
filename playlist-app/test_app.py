import unittest
from app import app, db
from models import Playlist, Song, PlaylistSong

class PlaylistAppTestCase(unittest.TestCase):
    """Test Flask app for Playlist."""

    def setUp(self):
        """Stuff to do before every test."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///test-playlist-app-db'
        app.config['WTF_CSRF_ENABLED'] = False # Disable CSRF for testing form submissions
        app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

        self.client = app.test_client()

        with app.app_context():
            # Recreate the database from scratch for a clean test environment
            db.drop_all()
            db.create_all()

            # Add sample playlist and song to test basic functionality
            self.playlist = Playlist(name="Test Playlist", description="Test Desc")
            self.song = Song(title="Test Song", artist="Test Artist")
            db.session.add_all([self.playlist, self.song])
            db.session.commit()

    def tearDown(self):
        """Clean up any fouled transaction."""
        with app.app_context():
            db.session.rollback()
            db.drop_all()

    def test_home_redirect(self):
        """Test that visiting '/' redirects to the /playlists route."""
        with self.client as client:
            resp = client.get("/", follow_redirects=False)
            self.assertEqual(resp.status_code, 302)
            self.assertIn("/playlists", resp.location)

    def test_show_playlists(self):
        """Test that the playlists page shows the seeded test playlist."""
        with self.client as client:
            resp = client.get("/playlists")
            html = resp.get_data(as_text=True)
            self.assertIn("Test Playlist", html)

    def test_add_playlist(self):
        """Test adding a new playlist through the form."""
        with self.client as client:
            resp = client.post("/playlists/add", data={
                "name": "New Playlist",
                "description": "New Desc"
            }, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertIn("New Playlist", html)

    def test_show_songs(self):
        """Test that the songs page shows the seeded test song."""
        with self.client as client:
            resp = client.get("/songs")
            html = resp.get_data(as_text=True)
            self.assertIn("Test Song", html)

    def test_add_song(self):
        """Test adding a new song through the form."""
        with self.client as client:
            resp = client.post("/songs/add", data={
                "title": "New Song",
                "artist": "New Artist"
            }, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertIn("New Song", html)

    def test_add_song_to_playlist(self):
        with app.app_context():
            """Test adding a song to an existing playlist."""
            # Add another song that isn't in the playlist
            another_song = Song(title="Another", artist="Artist")
            db.session.add(another_song)
            db.session.commit()

            # Re-fetch fresh instances to avoid DetachedInstanceError
            # This ensures the instances are bound to the current session
            playlist = Playlist.query.filter_by(name="Test Playlist").first()
            another_song = Song.query.filter_by(title="Another").first()

            # Store IDs before leaving the app context to avoid using detached instances
            playlist_id = playlist.id
            song_id = another_song.id

        with self.client as client:
            # Post to the add-song form for the playlist
            resp = client.post(f"/playlists/{playlist_id}/add-song", data={
            "song": song_id
            }, follow_redirects=True)
            html = resp.get_data(as_text=True)
            # Confirm the song appears on the playlist page after being added
            self.assertIn("Another", html)

if __name__ == '__main__':
    unittest.main()

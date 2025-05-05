from flask import Flask, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"
connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route("/")
def root():
    """Homepage: redirect to /playlists.
    
    This is the default route users will see. It redirects to the playlist page.
    """

    return redirect("/playlists")

##############################################################################
# Playlist routes

@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists.
    
    Query all playlists from the database and display them in the playlists.html template.
    """

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist.
    
    Retrieves a playlist by its ID and renders it in the playlist.html template.
    If the playlist is not found, a 404 error is triggered.
    """

    # Get playlist by ID or 404 if not found
    playlist = Playlist.query.get_or_404(playlist_id)
    return render_template("playlist.html", playlist=playlist)

@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    If the form is submitted and valid, a new playlist is added to the database.
    Otherwise, show the empty form to create a new playlist.
    """

    form = PlaylistForm()

    if form.validate_on_submit():
        new_playlist = Playlist(
            # Get name from form
            name=form.name.data,
            # Get description from form
            description=form.description.data,
        )
        # Add the new playlist to the session
        db.session.add(new_playlist)
        # Commit to the database
        db.session.commit()
        # Redirect to the playlists page
        return redirect("/playlists")
    
    # If the form is not valid or not submitted, render the form page
    return render_template("new_playlist.html", form=form)

##############################################################################
# Song routes

@app.route("/songs")
def show_all_songs():
    """Show list of songs.
    
    Fetch all songs from the database and display them in the songs.html template."""
    # Fetch all songs
    songs = Song.query.all()
    # Render the template with songs
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song
    
    Retrieves a song by its ID and displays it in the song.html template.
    """
    # Get song by ID or 404 if not found
    song = Song.query.get_or_404(song_id)
    return render_template("song.html", song=song)

@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    If the form is submitted and valid, a new song is added to the database.
    Otherwise, show the empty form to create a new song.
    """
    form = SongForm()

    if form.validate_on_submit():
        new_song = Song(
            # Get title from form
            title=form.title.data,
            # Get artist from form
            artist=form.artist.data,
        )
        # Add the new song to the session
        db.session.add(new_song)
        # Commit to the database
        db.session.commit()
        # Redirect to the songs page
        return redirect("/songs")
    
    # If the form is not valid or not submitted, render the form page
    return render_template("new_song.html", form=form)

@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a song to a playlist 
    
    Displays a form with available songs to add to a specific playlist. 
    If the form is valid, the song is linked to the playlist.
    """
    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()

    # Restrict form to fetch songs not already on this playlist
    curr_song_ids = [s.id for s in playlist.songs]
    # Get songs not on the playlist
    songs_not_in_playlist = Song.query.filter(~Song.id.in_(curr_song_ids)).all()
    # Set available song choices
    form.song.choices = [(s.id, f"{s.title} by {s.artist}") for s in songs_not_in_playlist]

    if form.validate_on_submit():
        # Get the selected song ID from form
        song_id = form.song.data
        # Create the link between song and playlist
        new_link = PlaylistSong(playlist_id=playlist.id, song_id=song_id)
         # Add the link to the session
        db.session.add(new_link)
        # Commit the transaction to the database
        db.session.commit()
        return redirect(f"/playlists/{playlist_id}")

    # If the form is not valid or not submitted, render the form page    
    return render_template("add_song_to_playlist.html", playlist=playlist, form=form)

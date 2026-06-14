class Song:
    """Represent a song and track library-wide song information."""

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    # Keep the assignment's plural spelling available while matching the tests.
    artists_count = artist_count

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        self.__class__.add_song_to_count()
        self.__class__.add_to_genres(genre)
        self.__class__.add_to_artists(artist)
        self.__class__.add_to_genre_count(genre)
        self.__class__.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        cls.sync_artist_count_names()

        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

        cls.artists_count = cls.artist_count

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.add_to_artists_count(artist)

    @classmethod
    def sync_artist_count_names(cls):
        if cls.artist_count is cls.artists_count:
            return

        if not cls.artist_count or not cls.artists_count:
            cls.artist_count = {}
        else:
            cls.artist_count.update(cls.artists_count)

        cls.artists_count = cls.artist_count

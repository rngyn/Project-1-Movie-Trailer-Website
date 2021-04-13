import webbrowser


class Movie():
    """Creates instances for movies including
    the movie title, movie poster source, and YouTube trailer URL.

    Also includes the show_trailer function to be able to
    open and play the trailer using the supplied YouTube URL.
    """
    def __init__(self, movie_title, poster_image, trailer_youtube):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

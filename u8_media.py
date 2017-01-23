import webbrowser

class Movie():
    """ This stores information about my first list of movie trailers"""
    VALID_RATINGS= ["G","PG","PG-13","R"]
    def __init__(self, movie_title, movie_storyline, movie_img_url, movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_img_url
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        webbrowser.open_new(self.trailer)
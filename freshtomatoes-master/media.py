import webbrowser


class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # init is a reserved function in python.All reserved functions have 2 underscores at start and at end.
        self.title = movie_title
        # It takes a few arguments one of them is self.
        self.storyline = movie_storyline
        # self means itself.
        self.poster_image_url = poster_image
        # using init function to initialise pieces of info like title,storyline etc
        self.trailer_youtube_url = trailer_youtube
        # The variables title,storyline etc are unique to an object and are called instance variables

    def show_trailer(self):
        # show_trailer is an instance method of class Movie and it takes one argument self.
        webbrowser.open(self.trailer_youtube_url)

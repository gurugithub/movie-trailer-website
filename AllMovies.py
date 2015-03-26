# This class is an object blueprint for all movie content. Inherits from Video
import webbrowser
from AllVideo import Video

class Movie(Video):
    """Movie class - Subclass of Video"""
#constructor
    def __init__(self, title, duration, rating, storyline, poster_image, youtube_trailer):
        print("movie cons called")
        Video.__init__(self, title, duration, rating)
        self.storyline = storyline
        self.poster_image = poster_image
        self.youtube_trailer = youtube_trailer

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)

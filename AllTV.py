# This class is an object blueprint for all TV content. Inherits from Video
from AllVideo inport Video

class TV(Video):
    """TV class - Subclass of Video"""
    def __init__(self, title, duration, rating, season, episode, tv_station):
#constructor
        Video.__init__(self, title, duration, rating)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station


# This class is an object blueprint for all video content

class Video():
    def __init__(self, title, duration, rating):
        """Video class - Normally subclassed"""
#constructor
        self.title = title
        self.duration = duration
        self.rating = rating
        

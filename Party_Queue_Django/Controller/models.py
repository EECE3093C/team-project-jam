# Class - Song
class Song:
    def __init__(self, QueueID, Song, Artist, URL, UserID, UserQueuePosition = 0):
        self.QueueID = QueueID
        self.Song = Song
        self.Artist = Artist
        self.URL = URL
        self.UserID = UserID
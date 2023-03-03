import json

from Controller.models import Song

# converts json file to Song data type
def convert_json_to_song(Json):
    dict = json.load(Json)
    song = Song(dict['QueueID'], dict['Song'], dict['Artist'], dict['URL'], dict['UserID'])
    return song

# converts Song data type to json file
def convert_song_to_json(song):
    dict = {}
    dict['QueueID'] = song.QueueID
    dict['Song'] = song.Song
    dict['Artist'] = song.Artist
    dict['URL'] = song.URL
    dict['UserID'] = song.UserID
    Json = json.dumps(dict)
    return Json

# Receives posted json file, converts to Song data type, adds to database
def post_next_song(postJson):
    postSong = convert_json_to_song(postJson)
    '''
    add postSong to queue database
    '''
    return "Song Received: \tQueueID: {0}\n\t\t\t\tName: {1}\n\t\t\t\tArtist: {2}\n\t\t\t\tURL: {3}\n\t\t\t\tUserID: {4}".format(postSong.QueueID, postSong.Song, postSong.Artist, postSong.URL, postSong.UserID)

# Returns next song in queue from database
def get_next_song():
    # Test Song
    getSong = Song('1', 'Free Bird', 'Lynard Skynard', 'https://spotify.com/Free_Bird', '1')
    getJson = convert_song_to_json(getSong)
    '''
    store next song in queue database to getSong and return getSong
    '''
    return getJson
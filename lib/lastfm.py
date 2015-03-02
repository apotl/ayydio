#!/usr/bin/python3
import requests
import json

key = open('lib/lfmkey').readline().rstrip('\n')
def getAlbumArt( artist, track ):
    
    artist = artist.replace(' ','%20')    
    track = track.replace(' ','%20')    

    urlargs = "http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=" + key + "&artist=" + artist + "&track=" + track + "&autocorrect=1&format=json"
    
    r = requests.get(urlargs)
    lfm_json = json.loads(r.text)
    
    return (lfm_json['track']['album']['image'][3]['#text'])


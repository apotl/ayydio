#!/usr/bin/python3
import requests
import json

try:
	key = open('lib/lfmkey').readline().rstrip('\n')
except IOError:
	key = ''

def getAlbumArt( artist, track ):
    
    artist = artist.replace(' ','%20')    
    track = track.replace(' ','%20')    

    urlargs = "http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key=" + key + "&artist=" + artist + "&track=" + track + "&autocorrect=1&format=json"
    
    r = requests.get(urlargs)
    lfm_json = json.loads(r.text)
    try:
        #if lfm_json['error'] == 10:
	    #    return 'ERROR: Could not grab album art.'
        #else: 
        return (lfm_json['track']['album']['image'][3]['#text'])
    except KeyError:
        print('lfm.py could not find album art')

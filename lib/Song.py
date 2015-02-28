class Song:
    

    def __init__( self, d_song ):
        
        self._album = d_song['album']
        self._artist = d_song['artist']
        self._date = d_song['date']
        self._file = d_song['file']
        self._genre = d_song['genre']
        self._time = d_song['time']
        self._title = d_song['title']
        

    def printInfo( self ):        
        
        print( self._album ) 
        print( self._artist )
        print( self._date )
        print( self._file )
        print( self._genre )
        print( self._time )
        print( self._title )


    def getInfo( self ):
    
        s = {}
        
        s["_album"] = self._album
        s["_artist"] = self._artist
        s["_date"] = self._date
        s["_file"] = self._file
        s["_genre"] = self._genre
        s["_time"] = self._time
        s["_title"] = self._title

        return s

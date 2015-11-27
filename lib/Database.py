#!/usr/bin/python3
from mpd import MPDClient
from lib import Song

def conToMpd():
	con = MPDClient()
	con.timeout = 10
	con.idletimeout = None
	con.connect( 'localhost', 6600 )
	return con

class Database:

	def __init__( self, music_root ):
		self._music_root = music_root
		self._con = MPDClient()
		self._con.timeout = 10
		self._con.idletimeout = None
		self._con.connect( 'localhost', 6600 )

	def addToDb( self, song_obj ):
		temp = song_obj.getInfo()['file']
		while self._con.find( 'file', temp) == []:
			try:
				temp = temp.split( '/', 1 )[1]
			except IndexError:
				print( 'ERROR: Could not add.  Please put the song (if it exists) under the mpd root.' )
				break
		if self._con.find( 'file', temp) != []:
			self._con.update( temp )
		
	def listDbDir( self, dir_loc ):
		listings = []
		for listing in self._con.lsinfo( dir_loc ):
			temp = Song.Song( self._music_root + listing['file'] )
			listings.append( temp )
		return listings
	
	def __del__( self ):
		self._con.close()

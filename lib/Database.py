#!/usr/bin/python3
from mpd import MPDClient

def conToMpd():
	con = MPDClient()
	con.timeout = 10
	con.idletimeout = None
	con.connect( "localhost", 6600 )
	return con

class Database:


	def __init__( self ):
		self._con = MPDClient()
		self._con.timeout = 10
		self._con.idletimeout = None
		self._con.connect( "localhost", 6600 )

	def addToDb( self, song_obj ):
		self._con.update( song_obj['file'] );
		
	def listDbDir( self, dir_loc ):
		listings = {}
		for listing in self._con.lsinfo( dir_loc ):
			temp = Song( listing['file'])
			listings.append( temp)
		return listings
	
	def __del__( self ):
		self._con.close()

from lib import lastfm
import stagger
from stagger.id3 import *


class SongError( Exception):

	def __init__( self, reason ):
		self.reason = 'ERROR in Song.py: ' + reason

class Song:

	def __init__( self, d_song ):
		try:
			if d_song == None:
				 self._ok = False
				 return
			self._album = stagger.read_tag( d_song ).album
			self._artist = stagger.read_tag( d_song ).artist
			self._date = stagger.read_tag( d_song ).date
			self._file = d_song
			self._genre = stagger.read_tag( d_song ).genre
			self._title = stagger.read_tag( d_song ).title
			self._track = stagger.read_tag( d_song ).track
			self._ttrack = stagger.read_tag( d_song ).track_total
			self._disc = stagger.read_tag( d_song ).disc
			self._tdisc = stagger.read_tag( d_song ).disc_total
			self._comment = stagger.read_tag( d_song ).comment
			self._aart = ''
#			self._aart = lastfm.getAlbumArt( self._artist, self._title )
			self._ok = True
		except IOError:
				raise SongError( 'File does not exist' )

	def printInfo( self ):
		if not self._ok:
			raise SongError( 'Song not instantiated correctly' )
		print( 'Album: ' + self._album ) 
		print( 'Artist: ' + self._artist )
		print( 'Date: ' + self._date )
		print( 'Filename: ' + self._file )
		print( 'Genre: ' + self._genre )
		print( 'Title: ' + self._title )
		print( 'Track ' + str( self._track ) + ' of ' + str( self._ttrack ) )
		print( 'Disc ' + str( self._disc ) + ' of ' + str( self._tdisc ) )
		print( 'Comment: ' + self._comment )
		print( 'Art: ' + self._aart )

	def getInfo( self ):
		if not self._ok:
			raise SongError( 'Song not instantiated correctly' )
		s = {}
		s['album'] = self._album
		s['artist'] = self._artist
		s['date'] = self._date
		s['file'] = self._file
		s['genre'] = self._genre
		s['title'] = self._title
		s['aart'] = self._aart
		s['track'] = self._track
		s['ttrack'] = self._ttrack
		s['disc'] = self._disc
		s['tdisc'] = self._tdisc
		s['comment'] = self._comment
		s['aart'] = self._aart
		return s



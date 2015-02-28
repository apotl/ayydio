from mpd import MPDClient
from lib.Song import Song

def conToMpd():
	con = MPDClient()
	con.timeout = 10
	con.idletimeout = None
	con.connect( "localhost", 6600)
	return con

checking = True
while checking == True:
	print( 'Give the file location of the song relative to mpd\'s root: '  )
	song_name = raw_input()
	client = conToMpd()
	for song_listing in client.lsinfo( song_name ):
		song_to_check = Song( song_listing)
		print( 'Album name: ' + song_to_check._album )
		print( 'Artist name: ' + song_to_check._artist )
		print( 'Date of song: ' + song_to_check._date )
		print( 'File name: ' + song_to_check._file )
		print( 'Song genre: ' + song_to_check._genre )
		print( 'Length: ' + song_to_check._time )
		print( 'Song title: ' + song_to_check._title + '\n' )
	client.close()
	print( 'Check another song? (type \'n\' to exit))' )
	test = raw_input()
	if test == 'n':
		checking = False

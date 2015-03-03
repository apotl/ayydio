#!/usr/bin/python3
from mpd import MPDClient
from lib.Song import Song

def conToMpd():
	con = MPDClient()
	con.timeout = 10
	con.idletimeout = None
	con.connect( "localhost", 6600 )
	return con

def makeChoice():
	print( 'Select a lib to check: ' )
	print( '   (1) Song.py' )
	choice = input()
	return choice

def checkSong_py():
	print( '\nGive the file location of the song: '  )
	song_loc = input()
	client = conToMpd()
		
	print( 'Testing instantiation...' )
	song_to_check = Song( song_loc )
	print( 'Album name: ' + song_to_check._album )
	print( 'Artist name: ' + song_to_check._artist )
	print( 'Date of song: ' + song_to_check._date )
	print( 'File name: ' + song_to_check._file )
	print( 'Song genre: ' + song_to_check._genre )
	print( 'Length: ' + song_to_check._time )
	print( 'Song title: ' + song_to_check._title )
	print( 'Album art link: ' + song_to_check._aart + '\n' )
	print( 'Instantiation OK.' )

	print( 'Testing getInfo()...' )
	song_info_dict = song_to_check.getInfo()
	for tag in song_info_dict:
		print( song_info_dict[tag] )
	print( 'getInfo() OK.' )

	print( 'Testing printInfo()...' )
	song_to_check.printInfo()
	print( 'printInfo() OK.' )

	client.close()

checking = True
while checking == True:
	choice = makeChoice()
	if choice == '1':
		checkSong_py()
	else:
		print( '\nERROR: Given option invalid')
	print( 'Test another lib? (type \'n\' to exit))' )
	test = input()
	if test == 'n':
		checking = False

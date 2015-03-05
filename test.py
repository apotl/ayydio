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
	print( '   (e) Exit test.py' )
	choice = input()
	return choice

def checkSong_py():
	print( '\nGive the file location of the song: '  )
	song_loc = input()
	client = conToMpd()
		
	print( 'Testing instantiation...', end = '' )
	song_to_check = Song( song_loc )
	print( 'Instantiation OK.' )

	print( 'Testing getInfo()...', end = '' )
	song_to_check.getInfo()
	print( 'getInfo() OK.' )

	print( 'Testing printInfo()...', end = '' )
	song_to_check.printInfo()
	print( 'printInfo() OK.' )

	client.close()

checking = True
while checking == True:
	choice = makeChoice()
	if choice == '1':
		checkSong_py()
	elif choice == 'e':
		checking = False
	else:
		print( '\nERROR: Given option invalid')

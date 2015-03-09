#!/usr/bin/python3
from mpd import MPDClient
from lib.Song import Song
from lib.Database import Database

def conToMpd():
	con = MPDClient()
	con.timeout = 10
	con.idletimeout = None
	con.connect( "localhost", 6600 )
	return con

def makeChoice():
	print( '\nSelect a lib to check: ' )
	print( '   (1) Song.py' )
	print( '   (2) Database.py' )
	print( '   (e) Exit test.py' )
	choice = input()
	return choice

def askSongLoc():
	print( '\nGive the file location of the song: '  )
	song_loc = input()
	return song_loc

def checkSong_py():
	client = conToMpd()
	print( 'Testing instantiation...', end = '' )
	song_to_check = Song( askSongLoc() )
	print( 'Instantiation OK.' )

	print( 'Testing getInfo()...', end = '' )
	song_to_check.getInfo()
	print( 'getInfo() OK.' )

	print( 'Testing printInfo()...', end = '' )
	song_to_check.printInfo()
	print( 'printInfo() OK.' )

	client.close()

def checkDatabase_py():
	print( 'Testing instantiation...', end = '' )
	db_to_check = Database()
	print( 'Instantiation OK.' )

	print( 'Testing addToDb()...', end = '' )
	song_to_check = Song( askSongLoc() )
	db_to_check.addToDb( song_to_check )
	print( 'addToDb() OK.' )

	print( 'Testing destruction...', end = '' )
	del db_to_check
	print( 'Destruction OK.' )

checking = True
while checking == True:
	choice = makeChoice()
	if choice == '1':
		checkSong_py()
	elif choice == '2':
		checkDatabase_py()
	elif choice == 'e':
		checking = False
	else:
		print( 'ERROR: Given option invalid' )

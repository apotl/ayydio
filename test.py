#!/usr/bin/python3
import pprint
from mpd import MPDClient
from lib.Song import Song, SongError
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
	try:
		song_to_check = Song( askSongLoc() )
	except SongError as why:
		song_to_check = Song( None )
		print( why.reason )
	print( 'Instantiation OK.' )

	print( 'Testing getInfo()...', end = '' )
	try:
		song_to_check.getInfo()
	except SongError as why:
		print( why.reason )
	print( 'getInfo() OK.' )

	print( 'Testing printInfo()...', end = '' )
	try:
		song_to_check.printInfo()
	except SongError as why:
		print( why.reason )
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

	print( 'Testing listDbDir()...' )
	song_dir_to_check = song_to_check._file.rsplit( '/' )[-2]
	pprint.pprint( db_to_check.listDbDir( song_dir_to_check))
	print( 'listDbDir() OK.' )

	print( 'Testing destruction...', end = '' )
	del db_to_check
	print( 'Destruction OK.' )

def main():
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

if __name__ == "__main__":
    print("test.py is being run directly")
    main()
else:
    print("test.py is being imported into another module")

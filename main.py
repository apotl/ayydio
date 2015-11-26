#!/usr/bin/python3
from mpd import MPDClient
from lib.Song import Song

print('ayydioctrl micro')

c = MPDClient()
c.timeout = 10
c.idletimeout = None
c.connect("localhost",6600)
c.update()
def lsdb():
	#for each file/dir
	for f in c.lsinfo():
		try:
			print('\033[31m'+ f['directory'])
			for ff in c.lsinfo(f['directory']):
				try:
					print('\033[32m' + ff['file'])
				except KeyError:
					pass 
		except KeyError:
			print('\033[32m' + f['file'])
		print('\033[30m') 
def makeChoice():
	print('\033[34m') 
	print('(1) list all available files in db')
	print('(2) queue a song(s)')
	print('(3) play')
	print('(4) next song')
	print('(5) show current playlist')
	print('(6) search')
	print('(q) quit')
	choice = input('option: ')
	return choice 

def queueUri(uri):
	try:
		c.add(uri)
	except:
		pass

def searchdb(query):
	print()
	for result in c.search('file',str(query)):
		print(result['file'])	
	
while True:
	x = makeChoice()
	if x == '1':
		lsdb()
	elif x == '2':
		queueUri(input('Enter uri: '))
	elif x == '3':
		c.play( 0)
	elif x == '4':
		c.next() 
	elif x == '5':
		print('Current playlist:')
		for song in c.playlist():
			print (song)
	elif x == '6':
		query = input('Search string: ')
		searchdb(query)
	elif x == 'q':
		break
c.close()
c.disconnect()


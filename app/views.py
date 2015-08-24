from app import app
from flask import render_template, jsonify, request, redirect, url_for
from mpd import MPDClient
from lib import Song, Database
import random
from urllib.parse import quote, unquote
@app.route('/')
@app.route('/index')
def index():
	c = MPDClient()
	c.timeout = 10
	c.idletimeout = None
	c.connect("localhost",6600)
	try:
		s = Song.Song('/home/alec/Music/'+ c.currentsong()['file'])
	except:
		s = Song.Song( None)
	return render_template("index.html",
				   title='now playing',
				   c = c,
				   s = s)
@app.route('/api/skip')
def skip():
	c = MPDClient()
	c.timeout = 10
	c.idletimeout = None
	c.connect("localhost",6600)
	try:
		c.play(1)
	except:
		pass
	if c.status()['playlistlength'] == '0':
		return jsonify(status="failure")
	c.delete( 0)
	return jsonify(status="success")

@app.route('/api/queue/random')
def queue_random():
	c = MPDClient()
	c.timeout = 10
	c.idletimeout = None
	c.connect("localhost",6600)
	while True:
		try:
			randuri = random.choice(c.lsinfo(random.choice(c.lsinfo())['directory']))['file']
			break
		except IndexError:
			print('problems queuing a certain song, trying another')
		except KeyError:
			print('problem queuing a certain song, trying another')
	return redirect('/api/queue/'+quote(randuri))

@app.route('/api/queue/<path:uri>')
def queue(uri):
	c = MPDClient()
	c.timeout = 10
	c.idletimeout = None
	c.connect("localhost",6600)
	print(uri)
	c.add(unquote(uri))
	#c.add(quote(uri).encode('ascii', 'xmlcharrefreplace').decode())
	if c.status()['state'] != 'play':
		c.play(0)
	return jsonify(status="success")

@app.route('/queue')
def queue_numbers():
	c = MPDClient()
	c.timeout = 10
	c.idletimeout = None
	c.connect("localhost",6600)
	songs = ''
	for f in c.lsinfo():
		try:
			for ff in c.lsinfo(f['directory']):
				try:
					songs += '<tr onclick="$.getJSON(\'/api/queue/' + quote(ff['file']) + '\')">'
					songs += '<td>' + ff['artist'] + '</td>'
					songs += '<td>' + ff['album'] + '</td>'
					songs += '<td>' + ff['title'] + '</td>'
					songs += '</tr>'
				except KeyError:
					pass 
		except KeyError:
			songs += '<tr><td><a onclick="$.getJSON(\'/api/queue/' + f['file'] + '\')">' + f['file'] + '</a></td></tr>'
	return render_template("queue.html",
				title='queue song',
				songs = songs)


@app.route('/api/nowplaying.json')
def currsong():
	c = MPDClient()
	c.timeout = 10
	c.idletimeout = None
	c.connect("localhost",6600)
	c.update()   
	return jsonify(result=c.currentsong())

@app.route('/api/playlist.json')
def pljson():
	c = MPDClient()
	c.timeout = 10
	c.idletimeout = None
	c.connect("localhost",6600)
	c.update()   
	return jsonify(result= c.playlist())
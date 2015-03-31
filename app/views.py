from app import app
from flask import render_template, jsonify, request
from mpd import MPDClient
from lib import Song
@app.route('/')
@app.route('/index')
def index():
    c = MPDClient()
    c.timeout = 10
    c.idletimeout = None
    c.connect("localhost",6600)
    c.update()   
    s = Song.Song('/home/floby/muz/'+ c.currentsong()['file'])
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
    c.update()   
    c.next()
    return jsonify(status="success")
@app.route('/add')
def add_numbers():
    c = MPDClient()
    c.timeout = 10
    c.idletimeout = None
    c.connect("localhost",6600)
    c.next()
    return jsonify(True)
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

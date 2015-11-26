from flask import Flask
app = Flask(__name__)
from app import views
from mpd import MPDClient

c = MPDClient()
c.timeout = 10
c.idletimeout = None
c.connect("localhost",6600)
c.random(0)
c.repeat(0)
c.consume(1)
#c.setvol(100)
c.close()   

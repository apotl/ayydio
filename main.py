from mpd import MPDClient
import pprint
from lib.Song import Song

c = MPDClient()
c.timeout = 10
c.idletimeout = None
c.connect("localhost",6600)
c.update()

for i in c.lsinfo( 'contact' ):
    s = Song( i )
    s.printInfo()    

c.close()
c.disconnect()


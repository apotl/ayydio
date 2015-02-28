from mpd import MPDClient
from lib.Song import Song

c = MPDClient()
c.timeout = 10
c.idletimeout = None
c.connect("localhost",6600)
c.update()

for i in c.lsinfo( 'dir' ):
    s = Song( i )
    s.printInfo()    

c.close()
c.disconnect()


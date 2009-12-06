from wirechannel import *
import time
w = WaveChannel()
sid = open("sid.txt").read()
w.crid = int(open("rid.txt").read())
print "sid: "+sid, "crid: ",w.crid
print w.search(sid,"public@a.gwave.com",100,100)
time.sleep(1)

print w.search(sid,"public@a.gwave.com",0,100)

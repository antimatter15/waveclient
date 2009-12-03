from wirechannel import WaveChannel
w = WaveChannel()
sid = open("sid.txt").read()

print "sid: "+sid

print w.search(sid,"public@a.gwave.com")
#print w.process_stream(sid, None)
exit()

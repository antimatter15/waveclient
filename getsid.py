from wirechannel import WaveChannel
w = WaveChannel()
#print w.test_signal("MODE=init")
#print w.test_signal("TYPE=xmlhttp")
sid = w.get_sid()
print "sid: "+sid
open("sid.txt","w").write(sid)

#print w.retrieve(sid)
#exit()


from wirechannel import *
w = WaveChannel()
sid = w.get_sid()
print "sid: "+sid, "crid: ",w.crid
open("sid.txt","w").write(sid)
open("rid.txt","w").write(str(w.crid))

print w.process_stream(sid, None)

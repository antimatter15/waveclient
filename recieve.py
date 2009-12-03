from wirechannel import WaveChannel
w = WaveChannel()
#print w.test_signal("MODE=init")
#print w.test_signal("TYPE=xmlhttp")
sid = w.get_sid()
print "sid: "+sid
open("sid.txt","w").write(sid)


import wavehttp
import random

sid = open("sid.txt").read()

print "sid: "+sid
zx = "".join([chr(random.randint(97,122)) for i in xrange(0, 11)])
res = wavehttp.get("/wave/wfe/channel?VER=6&RID=rpc&SID="+sid+
                  "&CI=0&AID=0&TYPE=xmlhttp&zx="+zx+"&t=1")
buf = ""
default = 10 #i sure hope no section will be larger than a googol! <the previous doesnt actually make sense any more, the value used to be 100>
size = default #an initial top part to get the headersey ish things

while True: #woot Apple, Inc headquarters!
  sect = res.read(size)
  #print "{",sect,"}"
  if sect is '':
    break #this thing died!
  if len(buf) == 0:
    first = sect.splitlines()[0] #this is the length of the following stuff
    #print "FRSOT PSOT {{",first,"}}"
    buf = sect[len(first):] #pre-fill the buffer with all the crap after the length of the length
    #print "START BUF {{",buf,"}}"
    size = int(first) - len(buf) + 1  #length to read is the amount left (size - buffer) and newlines are poopy
  else:
    buf += sect
    print "-------------NEW DATA-------------"
    print buf
    print "-------------END DATA-------------"
    size = default
    buf = ""

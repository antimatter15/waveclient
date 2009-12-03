import wavehttp
import random
import urllib

sid = open("sid.txt").read()

print "sid: "+sid
zx = "".join([chr(random.randint(97,122)) for i in xrange(0, 11)])

get = {
  "AID": 0,
  "CI": 0,
  "RID": "rpc",
  "SID": sid,
  "TYPE": "xmlhttp",
  "VER": 6,
  "t": 1,
  "zx": zx 
}


res = wavehttp.get("/wave/wfe/channel?"+urllib.urlencode(get))
                  
                  

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
    if '<HTML>' in first:
      print "Error, failure",sect+res.read()
      break #EPOCH PHAYLE
    #print "FRSOT PSOT {{",first,"}}"
    buf = sect[len(first):] #pre-fill the buffer with all the crap after the length of the length
    #print "START BUF {{",buf,"}}"
    size = int(first) - len(buf) + 1  #length to read is the amount left (size - buffer) and newlines are poopy
  else:
    buf += sect
    print "-------------NEW DATA-------------"
    print buf #WHOOT, parse this json later
    print "-------------END DATA-------------"
    size = default
    buf = ""

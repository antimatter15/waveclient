import wavehttp
zx = "".join([chr(random.randint(97,122)) for i in xrange(0, 11)])
res = wavehttp.get("/wave/wfe/channel?VER=6&RID=rpc&SID="+sid+
                  "&CI=0&AID=0&TYPE=xmlhttp&zx="+zx+"&t=1")

initial = res.read(100) #an initial top part to get the headersey ish things
first = string.splitlines()[0] #this is the length of the following stuff
buf = first[len(first):] #pre-fill the buffer with all the crap after hte length of the length
size = int(first) - len(buf) #length to read is the amount left (size - buffer)


buf = ""
size = 100 #an initial top part to get the headersey ish things
#i sure hope no section will be larger than a googol!
while True: #woot Apple, Inc headquarters!
  sect = res.read(size)
  if sect is '':
    break #this thing died!
  if len(buf) == 0:
    first = sect.splitlines()[0] #this is the length of the following stuff
    buf = first[len(first):] #pre-fill the buffer with all the crap after the length of the length
    size = int(first) - len(buf) #length to read is the amount left (size - buffer)
  else:
    buf += sect
    print "-------------NEW DATA-------------"
    print buf
    print "-------------END DATA-------------"
    size = 100
    buf = ""

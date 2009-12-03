import wavehttp
zx = "".join([chr(random.randint(97,122)) for i in xrange(0, 11)])
res = wavehttp.get("/wave/wfe/channel?VER=6&RID=rpc&SID="+sid+
                  "&CI=0&AID=0&TYPE=xmlhttp&zx="+zx+"&t=1")
while True:
  sect = res.read(100) #should be enough to parse out important stuff

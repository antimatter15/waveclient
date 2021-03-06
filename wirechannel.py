#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright @ 2009, Waverz.com - BSD license - Information wants to be free!

# direct wave wire channel implementation:
# reads the public stream

import random
#from wireutils import webrequest
import wavehttp
import urllib
from waveapi import simplejson

class WaveChannel():
    """Wave channel reader"""
    
    crid = random.randint(0, 100000)
    client_version = 3
    channel_version = 6
    
    def zx(self):
      return "".join([chr(random.randint(97,122)) for i in xrange(0, 11)])
    
    #do a channel post request
    def req(self, sid = None, payload = []): #payload is optional
      self.crid += 1 #increment
      #isn't a perfect clone of how it actually works, but shorter and works :)
      #as for future implementers, any random string would work.
      post = {'count': len(payload)}
      get = {
        'VER': self.channel_version,
        'RID': self.crid,
        'CVER': self.client_version,
        'zx': self.zx(),
        't': 1 #TODO number of retries
      }
      if sid is not None:
        get['SID'] = sid
      for index, item in enumerate(payload):
        post["req"+str(index)+"_key"] = item #TODO do json encoding?
      print post
      print urllib.urlencode(get)
      resp = wavehttp.post("/wave/wfe/channel?"+urllib.urlencode(get),urllib.urlencode(post))
      return resp
      
      
      
    def parse_response(self, r):
        """returns a native python object from the JSON mess spit by wave"""
        data = ("".join(r.split("\n")[1:])).replace(",]","]")
        obj = simplejson.loads(data)
        return obj
        
    def test_signal(self, data = "MODE=init"):
        """sends a test request"""
        resdat = wavehttp.get("/wave/wfe/test?VER=6&"+data+"&zx="+self.zx()+"&t=1")
        return resdat
        
    def get_sid(self):
        """returns a wave-usable SID"""
        resdat = self.req().read() #phew, that was easy :)
        print resdat
        resdat = self.parse_response(resdat)
        if (resdat[0][1][0] != "c"):
            return None
        sid = resdat[0][1][1]
        return sid
        
    def search(self, sid, group):
        """returns search result for all group messages"""
        zx = "".join([chr(random.randint(97,122)) for i in xrange(0, 11)])
        resdat = self.req(sid, ['{"a":"kA-_jfrF","r":"0","t":2007,"p":{"1000":[0,0],"2":"kA-_jfrF0"}}',
                           '{"a":"kA-_jfrF","r":"1","t":2602,"p":{"1000":[0,0],"2":"kA-_jfrF2","3":"","4":{"2":25,"1":0},"6":"public@a.gwave.com"}}']).read()
        print "RESULT DATA",resdat
    
        
    def process_stream(self, sid, f):
        """process an incoming stream referenced from SID; calls back f(data)"""
        http_response = wavehttp.get("/wave/wfe/channel?VER=6&RID=rpc&SID="+sid+
                           "&CI=0&AID=0&TYPE=xmlhttp&zx="+self.zx()+"&t=1")
        http_data = http_response.read(120)
        print http_data
        exit()
        connection.close()
        
    def retrieve(self, sid):
        """fetch the currently seeked result"""
        zx = "".join([chr(random.randint(97,122)) for i in xrange(0, 11)])
        resdat = wavehttp.get("wave.google.com", 
                            "/wave/wfe/channel?VER=6&RID=rpc&SID="+sid+
                            "&CI=0&AID=0&TYPE=xmlhttp&zx="+zx+"&t=1").read()
        file("./tempdata","w+").write(resdat)
        print resdat

        
        
    def __init__(self):
        pass
    
#t = webrequest("GET", "wave.google.com",
#               "/wave/wfe/channel?VER=6&RID=rpc&SID=3E8CF847DD1CE8A6&CI=0&AID=0&TYPE=xmlhttp&zx=u5kkqba3qj1z&t=1",
#               {'Cookie': "WAVE=DQAAAI4AAADv5UPduZqKEiF4eInHebThSZJE3P0iX6NDWL4NFMvbuY5Jcw6cYLzivgmSfTp921fdgI5Yj2-OIRYSceu8lHrgPh553raYIJ_F82UulGKm2yazA2syXNoIia0M1goqBnGBKub7Bmd5CKgIvVMLJ5edE5On-8dABj3m6DDcZtxYTX141VlBhvO4gCcJSGxX2VQ; S=wave-dollhouse=jsl7loIsv6FVZ0tEEETcIQ"},
#               None)
#print t
#exit()0




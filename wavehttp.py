import httplib
import pickle
import urllib
import Cookie

conn = httplib.HTTPSConnection("wave.google.com") 
#conn.set_debuglevel(8)

statefile = "state.txt"
state = {}
session = ""
cookie = ""

def loadstate():
  global statefile, state, session, cookie
  state = pickle.load(open(statefile,"r"))
  session = state['session']
  cookie = state['cookie']

loadstate()

dollhouse = ""

def setcookie(val):
  cookie = val
  setstate()
  savestate()
  
def setstate():
  state = {
    "session": session,
    "cookie": cookie
  }

def savestate():
  global statefile
  pickle.dump(state, open(statefile,"w"))

def handlecookie(header):
  global cookie, dollhouse
  C2 = Cookie.SimpleCookie(header)
  if "WAVE" in C2:
    if C2["WAVE"].value != cookie:
      cookie = C2["WAVE"].value
      setstate()
      savestate()
      #print "Set New WAVE Cookie Value",C2["WAVE"].value
    if "S" in C2:
      if C2["S"] != dollhouse:
        dollhouse = C2["S"].value
        #print "Set new S Cookie value",dollhouse

def get(url):

  global cookie, dollhouse
  conn.close()
  conn.request("GET", url, "", {"Cookie":  make_cookie({
  "WAVE": cookie,
  "S": dollhouse
  })})
  resp = conn.getresponse()
  handlecookie(resp.getheader("Set-Cookie"))
  return resp


def make_cookie(obj):
  cooks = []
  for key in obj:
    if obj[key] not in [None, ""]:
      cooks.append(key+"="+obj[key])
  return "; ".join(cooks)


def post(url, body):
  global cookie, dollhouse
  conn.close()
  conn.request("POST", url, body, {
  "Cookie": make_cookie({
  "WAVE": cookie,
  "S": dollhouse
  }), 
  "Content-type": "	application/x-www-form-urlencoded; charset=UTF-8"})
  resp = conn.getresponse()
  handlecookie(resp.getheader("Set-Cookie"))
  return resp

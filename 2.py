import requests
import json

#### Searching
searchString = 'shewillbeloved'
url = 'https://secure.twangmusic.in/music/v2/unisearch?q=' + searchString + '&lang=en'
data = {'x-bsy-net':'2/-1/1',
 'x-bsy-cid':'fec1c40709bc297ce8df2139f0ce5785b868ce6b',
 'x-bsy-utkn':'6SMmO6yuIN1iaRiCq0:C7tFPgbbRXDDKtOO6f0M5g2zjHg=',
 'x-bsy-did':'71a9c5d4807e0533/Android/22/36/1.3.2.0',
 'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LMY48M)',
 'Host':'secure.twangmusic.in',
 'Connection':'Keep-Alive',
 'Accept-Encoding':'gzip'}
res = requests.get( url, data = data )
#print( res.text )

json_data = json.loads(res.text)
respo = json_data['items'][0]


##Downloading Song
#songID = 'srch_universalmusic_00602547571755-USUM71203514'
#searchURL = 'http://api.wynk.in/music/v1/cscgw/'+ songID + '.html?hlscapable=1&lang=en'


searchURL = 'http://api.wynk.in/music/v1/cscgw/srch_hungama_16042465.html?hlscapable=1&lang=en'
data = {'x-bsy-net':'2/-1/2',
 'x-bsy-cid':'fec1c40709bc297ce8df2139f0ce5785b868ce6b',
 'x-bsy-utkn':'6SMmO6yuIN1iaRiCq0:OZDa0PEjz94XD8vqva+hhrMxHUk=',
 'x-bsy-did':'71a9c5d4807e0533/Android/22/36/1.3.2.0',
 'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LMY48M)',
 'Host':'secure.twangmusic.in',
 'Connection':'Keep-Alive',
 'Accept-Encoding':'gzip'}

res = requests.get( searchURL, data = data )
json_data = json.loads(res.text)
respo = json_data['items'][0]






searchURL = 'https://secure.twangmusic.in/music/v2/featured?lang=en'
data = {'x-bsy-net':'2/-1/1',
 'x-bsy-cid':'fec1c40709bc297ce8df2139f0ce5785b868ce6b',
 'x-bsy-utkn':'6SMmO6yuIN1iaRiCq0:OZDa0PEjz94XD8vqva+hhrMxHUk=',
 'x-bsy-did':'71a9c5d4807e0533/Android/22/36/1.3.2.0',
 'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; Nexus 6 Build/LMY48M)',
 'Host':'secure.twangmusic.in',
 'Connection':'Keep-Alive',
 'Accept-Encoding':'gzip'}


res = requests.get( searchURL, data = data )


http://hls.wynk.in/i/srch_hungama/music/,128,64,32,320,/1441519680/srch_hungama_16042465.mp4.csmil/master.m3u8?hdnts=exp=1443892448~acl=
http://hls.wynk.in/i/srch_hungama/music/,128,64,32,320,/1441519680/srch_hungama_16042465.mp4.csmil/master.m3u8
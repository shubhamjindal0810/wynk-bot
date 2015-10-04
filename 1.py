import requests
from subprocess import call
import sys
import re

call(['mkdir', 'temp'])

#http://hls.wynk.in/i/srch_universalmusic/music/64/1427192621/srch_hungama_1715478.mp4/index_0_a.m3u8?null= 
#http://hls.wynk.in/i/srch_sonymusic/music/64/1426539872/srch_sonymusic_A10328E00071536862.mp4/segment6_0_a.ts?null= 
"""
typeOfMusic= raw_input('Choose First String\n1.Universal Music?\n2.Sony Music?\n3.Hungama?\n4.Timewarner?\n')
if(int(typeOfMusic) == 1 ):
	string1 = 'universalmusic'
if(int(typeOfMusic)==2):
	string1='sonymusic'
if(int(typeOfMusic)==3):	
	string1='hungama'
if(int(typeOfMusic)==4):	
	string1='timewarner'

typeOfMusic= raw_input('Choose Second String\n1.Universal Music?\n2.Sony Music?\n3.Hungama?\n4.Timewarner?\n')
if(int(typeOfMusic) == 1 ):
	string2 = 'universalmusic'
if(int(typeOfMusic)==2):
	string2='sonymusic'
if(int(typeOfMusic)==3):	
	string2='hungama'
if(int(typeOfMusic)==4):	
	string2='timewarner'	

typeOfBit=raw_input('Enter the Bitrate\n0.128,64,32.320\n')
if(int(typeOfBit)==0):
	bitrate=',128,64,32,320,'
if(typeOfBit!=0):
	bitrate=str(typeOfBit)

number = raw_input('Enter the number:\n')
number2= raw_input('Enter the second number:\n')
"""


print( "Please enter the log string" )

names = ''
while True:
    try:
        name = raw_input()
    except KeyboardInterrupt:
        break
    names = names + name

url =  re.search("(?P<url>https?://[^\s]+)", names).group("url")
print(url)
url = '/'.join(url.split('/')[0:-1])

flag = raw_input("\nDo you wish to continue?\n1.Yes\n2.No\n")
if( int(flag) == 2):
	sys.exit()
#url = raw_input("Enter thr url upto before segment\n")
number3 = raw_input('Enter the file name number\n')
#preURL= 'http://hls.wynk.in/i/srch_' + string1 + '/music/' + bitrate + '/' + str(number) + '/srch_' + string2 + '_' + number2 +'/segment'
preURL= url + '/segment'

print(preURL)

def download_file(url):
    local_filename = 'temp/' + url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                f.flush()
    return local_filename

fileName = 'concat:'
drc = 'temp/'
for i in range( 1, 36 ):
	download_file( preURL + str(i) + '_' + number3 +'_a.ts')
	fileName = fileName + drc + (preURL + str(i) + '_' + number3 + '_a.ts').split('/')[-1] + '|'

call(['avconv', '-i', fileName, '-c', 'copy', drc +'temp.mp4'])
output = raw_input('Enter output file name\n')
call(['avconv', '-i', drc+'temp.mp4', output])
call(['rm', '-rf', 'temp'])
print("Done.")





#1441519680
#Enter the second number:16042465

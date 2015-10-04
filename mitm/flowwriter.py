
from libmproxy.protocol.http import decoded
from libmproxy import filt
import httplib
def start(context, argv):
    if len(argv) != 2:
        raise ValueError('Usage: -s "flowriter.py filename"')
    #context.filter = filt.parse("twangmusic\.in")
def request(context, flow):
    #if flow.match(context.filter):
    with open("body.txt","a") as f:
        f.write( '\n URL \n' + str( flow.request.host) + '\n')
        f.write( '\n header \n' + str( flow.request.headers) + '\n')
        f.write('\n Request \n'+ flow.request.content + '\n')

def response(context, flow):
	#if flow.match(context.filter):
	with decoded(flow.response):
		with open("body.txt","a") as f:
			f.write( '\n header \n' + str( flow.response.headers) + '\n')
			f.write('\n Response \n'+flow.response.content + '\n')
			

"""
from libmproxy.flow import FlowWriter
from libmproxy.protocol.http import decoded


def start(context, argv):
    if len(argv) != 2:
        raise ValueError('Usage: -s "flowriter.py filename"')
    if argv[1] == "-":
        f = sys.stdout
    else:
        f = open(argv[1], "wb")
    #context.flow_writer = FlowWriter(f)


def response(context, flow):
    with decoded(flow.response):  # automatically decode gzipped responses.
            f.write(flow.response.content)
"""


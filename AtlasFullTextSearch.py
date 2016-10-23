import requests
import json

ATLAS_DOMAIN="server1" # the Atlas Metadata server
ATLAS_PORT="21000"

def atlasREST( restAPI ):
    url = "http://"+ATLAS_DOMAIN+":"+ATLAS_PORT+restAPI
    print "URL request = %s" % (url)
    r= requests.get(url, auth=("admin", "admin"))
    print json.dumps(json.loads(r.text), indent=4, sort_keys=True)
    return(json.loads(r.text));

atlasREST("/api/atlas/discovery/search/fulltext?query=sku")
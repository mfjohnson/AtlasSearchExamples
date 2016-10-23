import requests
import json


### Global Variables
## Please update for your specific instance before running this script
ATLAS_DOMAIN="server1" # the Atlas Metadata server
ATLAS_PORT="21000"
DATABASE_NAME='default'
TABLE_NAME='drivers'
CLUSTER_NAME='HDP'
QUERY_TAG= '%60TLC%60'

# Utility function to execute the rest query and print the results
def atlasREST( restAPI ):
    url = "http://"+ATLAS_DOMAIN+":"+ATLAS_PORT+restAPI
    print "URL request = %s" % (url)
    r= requests.get(url, auth=("admin", "admin"))
    print json.dumps(json.loads(r.text), indent=4, sort_keys=True)
    return(json.loads(r.text));

def atlasGET( restAPI ):
    url = "http://"+ATLAS_DOMAIN+":"+ATLAS_PORT+restAPI
    print "URL request = %s" % (url)
    r= requests.get(url, auth=("admin", "admin"))
    return(json.loads(r.text));


## Simple DSL Search example seeking only those entities with the specified table name.  Note: This search differs from
# the Qualified name search in that it will extract any entity of that table name from any database and any cluster.
print("SIMPLE DSL SEARCH BASED ON TABLENAME ONLY")
atlasREST("/api/atlas/discovery/search/dsl?query=hive_table+where+name='%s'" % (TABLE_NAME))


print("-----------------------------------------")
print("SIMPLE DSL SEARCH BASED ON TABLENAME ONLY")
atlasREST("/api/atlas/discovery/search/dsl?query=hive_table+where+name='%s' limit 3" % (TABLE_NAME))

print("-----------------------------------------")
print("DSL SEARCH BASED ON TABLENAME ONLY DEMONSTRATING DISPLAYING ONLY SELECT PROPERTIES")
atlasREST("/api/atlas/discovery/search/dsl?query=hive_table+where+name='drivers' select tableType,temporary,retention,qualifiedName,description,name,owner,comment,createTime limit 1 ")

print("-----------------------------------------")
print("DSL SEARCH FOR ENTITIES CONTAINING COLUMN NAME")
atlasREST("/api/atlas/discovery/search/dsl?query=hive_table%2C+columns+where+name%3D%27tweet_id%27")
atlasREST("/api/atlas/discovery/search/dsl?query=hive_table%2C+columns+select+name%2C+owner")
#atlasREST("/api/atlas/discovery/search/dsl?query=hive_column+where+name%3D%27tweet_id%27")

print("-----------------------------------------")
print("DSL SEARCH BASED ON TABLENAME ONLY DEMONSTRATING DISPLAYING ONLY SELECT PROPERTIES and arrays")
#atlasREST("/api/atlas/discovery/search/dsl?query=hive_table+where+name='drivers' select tableType,temporary,retention,qualifiedName,description,name,owner,comment,createTime,columns, select owner")






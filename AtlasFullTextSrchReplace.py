from ATLASAPI import *

srchStr = "atlashivetable1"
AssignTag = "GROUP1"

# Create a list of qualifying Entities...Note this will identify all entity types with the search string
qualifiyingTables = atlasREST("/api/atlas/discovery/search/fulltext?query=%s" % (srchStr))

groupTrait = {
    "jsonClass": "org.apache.atlas.typesystem.json.InstanceSerialization$_ Struct",
    "typeName": "%s" % (AssignTag), "values": {
    }
}


for src_entity in qualifiyingTables:
    replaceResult = atlasPOST("/api/atlas/entities/%s/traits", groupTrait);

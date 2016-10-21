from ATLASAPI import *

## Properties
tableFQDN="default.drivers@HDP"  # Your table's FQDN in the format of '{database name}.{tablename}@{Cluster Name}


print("FIND HIVE_TABLE ENTITY USING ENTITY REST API:")
hive_tables=atlasREST("/api/atlas/entities?type=hive_table&property=qualifiedName&value=%s" % (tableFQDN))
print json.dumps(hive_tables, indent=4, sort_keys=True)



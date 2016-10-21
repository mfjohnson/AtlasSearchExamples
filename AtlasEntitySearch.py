from ATLASAPI import *

print("FIND HIVE_TABLE ENTITY FOR MODIFICATION:")
hive_tables=atlasREST("/api/atlas/entities?type=hive_table")
print json.dumps(hive_tables, indent=4, sort_keys=True)
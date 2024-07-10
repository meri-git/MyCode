-- Select the latest snapshot information from the Iceberg table
SELECT 
    metadata_file_location,
    snapshot_id,
    parent_snapshot_id,
    timestamp_ms,
    manifest_list,
    summary
FROM 
    TABLE(SYSTEM$SNAPSHOTS('my_database.my_schema.my_iceberg_table'))
ORDER BY 
    timestamp_ms DESC;

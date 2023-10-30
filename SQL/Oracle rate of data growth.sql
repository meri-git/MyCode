SELECT
  table_name,
  TO_CHAR(end_snap.snap_time, 'DD-MON-YYYY HH24:MI:SS') AS end_time,
  TO_CHAR(start_snap.snap_time, 'DD-MON-YYYY HH24:MI:SS') AS start_time,
  (end_seg.size_mb - start_seg.size_mb) / (TO_NUMBER(TO_CHAR(end_snap.snap_time, 'J')) - TO_NUMBER(TO_CHAR(start_snap.snap_time, 'J'))) AS growth_rate_mb_per_day
FROM
  (SELECT table_name, SUM(bytes) / 1024 / 1024 AS size_mb
   FROM dba_segments
   WHERE owner = 'YourSchemaOwner' AND segment_type = 'TABLE'
   GROUP BY table_name) end_seg
JOIN
  (SELECT table_name, SUM(bytes) / 1024 / 1024 AS size_mb
   FROM dba_segments
   WHERE owner = 'YourSchemaOwner' AND segment_type = 'TABLE'
   GROUP BY table_name) start_seg
ON end_seg.table_name = start_seg.table_name
JOIN
  (SELECT snap_id, snap_time
   FROM dba_hist_snapshot
   WHERE TO_DATE(snap_time, 'DD-MON-YYYY HH24:MI:SS') >= TO_DATE('StartDateTime', 'DD-MON-YYYY HH24:MI:SS')
   AND TO_DATE(snap_time, 'DD-MON-YYYY HH24:MI:SS') <= TO_DATE('EndDateTime', 'DD-MON-YYYY HH24:MI:SS')) end_snap
ON 1 = 1
JOIN
  (SELECT snap_id, snap_time
   FROM dba_hist_snapshot
   WHERE TO_DATE(snap_time, 'DD-MON-YYYY HH24:MI:SS') >= TO_DATE('StartDateTime', 'DD-MON-YYYY HH24:MI:SS')
   AND TO_DATE(snap_time, 'DD-MON-YYYY HH24:MI:SS') <= TO_DATE('EndDateTime', 'DD-MON-YYYY HH24:MI:SS')) start_snap
ON 1 = 1
ORDER BY growth_rate_mb_per_day DESC;

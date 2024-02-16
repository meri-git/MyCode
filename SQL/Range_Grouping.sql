WITH TableRanges AS (
  SELECT
    table_name,
    rowcounts,
    CASE
      WHEN rowcounts <= 1000 THEN '0 - 1000'
      WHEN rowcounts <= 5000 THEN '1001 - 5000'
      WHEN rowcounts <= 10000 THEN '5001 - 10000'
      -- Add more ranges as needed
      ELSE 'Above 10000'
    END AS rowcount_range
  FROM your_database.your_schema.your_table -- Replace with your actual table reference
)

SELECT
  rowcount_range,
  COUNT(DISTINCT table_name) AS num_tables
FROM TableRanges
GROUP BY rowcount_range
ORDER BY rowcount_range;

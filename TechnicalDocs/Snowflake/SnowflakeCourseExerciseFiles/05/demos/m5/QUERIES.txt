// LIMIT or TOP CLAUSE
SELECT * 
FROM   reviews 
LIMIT  100; 

SELECT TOP 100 * 
FROM   reviews;

SELECT * 
FROM   reviews
OFFSET 0 FETCH 100;

// DATEBUCKET FILTER
SELECT business_id, 
       stars, 
       Max(review_date) 
FROM   reviews 
GROUP  BY :datebucket(review_date), 
          business_id, 
          stars 
LIMIT  100; 

// DATERANGE FILTER
SELECT TOP 100 * 
FROM   reviews 
WHERE  review_date = :daterange; 

//Subqueries
SELECT bus.name, 
       city, 
       state 
FROM   public.businesses bus 
WHERE  bus.business_id IN (SELECT revs.business_id 
                           FROM   public.reviews revs 
                           GROUP  BY revs.business_id 
                           ORDER  BY Avg(stars) DESC 
                           LIMIT  10);
                           


// Window functions
SELECT DISTINCT name, 
       city,
       state,
       rank()
           over (order by stars desc) as rank
    FROM businesses
    WHERE state='NV'
    ORDER BY name
    LIMIT 100;

// Variables and CTES
SET city='Windsor';

SELECT $city;

WITH businesses_place 
      (business_id, name, city, state) 
    AS 
      (
        SELECT business_id, name, city, state
            FROM businesses
          WHERE city = $city
      )
  SELECT name, city, state, avg(stars) avg_stars, sum(useful) sum_useful
  FROM businesses_place bp JOIN reviews rv ON bp.business_id=rv.business_id
  GROUP BY name,city,state
  ORDER BY avg_stars DESC
  ;

// Approximate functions and JSON
WITH approx_businesses AS (
  SELECT approx_top_k(business_id, 10) AS business_json
  FROM reviews
),
 flattened AS(
  SELECT value[0]::string AS business_id, value[1]::int AS frequency
FROM approx_businesses, lateral flatten(business_json))
SELECT DISTINCT name, frequency from flattened fl JOIN businesses bu WHERE fl.business_id=bu.business_id;


// Getting results back from the cache (accessible to executing user for 24 hours)
SELECT * FROM TABLE(result_scan('*********************************'));

// Querying ouput of commands
SHOW TABLES;

SELECT * FROM TABLE(result_scan('**********************************'))
AS x
WHERE x."rows">500000;

  

CREATE OR REPLACE PROCEDURE consume_api()
RETURNS VARIANT
LANGUAGE PYTHON
AS
$$
import requests
import json
import snowflake.connector

# Make API call and get response
response = requests.get('https://jsonplaceholder.typicode.com/todos')

# Convert JSON response to Python dictionary
data = json.loads(response.text)

# Flatten the JSON response
flattened_data = []
for item in data:
    flattened_item = {}
    for key in item.keys():
        if isinstance(item[key], dict):
            for sub_key in item[key].keys():
                flattened_item[key + "_" + sub_key] = item[key][sub_key]
        else:
            flattened_item[key] = item[key]
    flattened_data.append(flattened_item)

# Connect to Snowflake and insert flattened data
conn = snowflake.connector.connect(
    user='<YOUR_USERNAME>',
    password='<YOUR_PASSWORD>',
    account='<YOUR_ACCOUNT>',
    warehouse='<YOUR_WAREHOUSE>',
    database='<YOUR_DATABASE>',
    schema='<YOUR_SCHEMA>'
)

cur = conn.cursor()
cur.execute("CREATE OR REPLACE TABLE api_data (data VARIANT)")
cur.execute("INSERT INTO api_data SELECT parse_json(column1) FROM VALUES ('{}')".format(json.dumps(flattened_data)))
conn.commit()

return "API data successfully consumed and flattened."
$$;



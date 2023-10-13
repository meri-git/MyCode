import subprocess
import os

# Liquibase command and arguments
liquibase_command = "liquibase"
changeLogFile = "changelog.xml"  # ChangeLog XML file
snowflake_url = "jdbc:snowflake://<your_snowflake_url>?warehouse=<your_warehouse>&db=<your_database>&schema=<your_schema>&role=<your_role>"
snowflake_user = "<your_snowflake_username>"
snowflake_password = "<your_snowflake_password>"

# Define your view definition SQL
view_sql = """
CREATE OR REPLACE VIEW MY_VIEW AS
SELECT COLUMN1, COLUMN2
FROM MY_TABLE;
"""

# Write the SQL to a temporary file
with open("view.sql", "w") as sql_file:
    sql_file.write(view_sql)

# Create a Liquibase ChangeLog XML file
changelog_content = f"""
<?xml version="1.0" encoding="UTF-8"?>
<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.0.xsd">
    <changeSet author="yourname" id="create_view">
        <sqlFile path="view.sql" relativeToChangelogFile="true"/>
    </changeSet>
</databaseChangeLog>
"""

with open(changeLogFile, "w") as changelog_file:
    changelog_file.write(changelog_content)

# Run Liquibase to apply the change
try:
    subprocess.run([liquibase_command, "--changeLogFile=" + changeLogFile, "--url=" + snowflake_url, "--username=" + snowflake_user, "--password=" + snowflake_password, "update"], check=True)
    print("View created successfully in Snowflake.")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# Clean up temporary files
os.remove("view.sql")

# Optionally, you can clean up the ChangeLog file too
# os.remove(changeLogFile)

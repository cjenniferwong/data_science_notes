# you use SQA to write the sql statements and PG as the driver to interact with the database

import psycopg2
from sqlalchemy import create_engine
import json

with open ('config.json') as file:
    credentials = json.load(file)

connection_string = f"""postgres://{credentials['user']}:{credentials['password']}@{credentials['host']}/{credentials['database']}
"""

print(connection_string)

engine = create_engine(connection_string)
connection = engine.connect()
print('connected')

connection.close()

print('connection closed')


# establish a connection with the database
# connection = psycopg2.connect(
# host='localhost'
# , database='jennwong'
# , user='postgres'
# , password='postgres'
# )

# need to create a cursor that will enact the actions you want to do

# cursor = connection.cursor()

# pass a sql statement to query data

# sql_statement = '''
# SELECT * FROM TABLE_NAME
# '''

# cursor.execute(sql_statement)
# rows = cursor.fetchall() # returns a tuple with the data


print('connected')

# if you're making changes you have to make sure to commit the changes to the db
# connection.commit()

# its important to close your connect so you dont have a connection leak which drains resources
# cursor.close()
# connection.close()

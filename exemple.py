from redshift_connection import RedshiftConnector

conn = RedshiftConnector()

query = """
SELECT 'consegui criar um dataFrame de uma query!!!' as coluna;
"""

df= conn.create_dataframe(query)

df.head()
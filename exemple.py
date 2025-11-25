from pandas_redshift import PandasRedshift

conn = PandasRedshift()

query = """
SELECT 'consegui criar um dataFrame de uma query!!!' as coluna;
"""

df= conn.create_dataframe(query)

df.head()
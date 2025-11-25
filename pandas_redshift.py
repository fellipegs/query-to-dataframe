import redshift_connector
import pandas as pd
from typing import Optional
from dotenv import load_dotenv
import os

class PandasRedshift:
    def __init__(self):
        load_dotenv()

        self.__host = os.environ.get('REDSHIFT_HOST')
        self.__database = os.environ.get('REDSHIFT_DB')
        self.__user = os.environ.get('REDSHIFT_USER')
        self.__password = os.environ.get('REDSHIFT_PASSWORD')
        self.__port = os.environ.get('REDSHIFT_PORT') 

    def __get_connection(self):

        return redshift_connector.connect(
            host=self.__host,
            database=self.__database,
            port=self.__port,
            user=self.__user,
            password=self.__password
        )

    def create_dataframe(self, sql_query: str) -> Optional[pd.DataFrame]:
        connection = None
        try:
            connection = self.__get_connection()
            
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                return cursor.fetch_dataframe()

        except redshift_connector.Error as db_err:
            print(f"Erro de Conexão ou SQL no Redshift: {db_err}")
            return None
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
            return None
            
        finally:
            if connection:
                connection.close()

    def join_dataframes(self, df1, df2, keys, new_col, how="inner") -> Optional[pd.DataFrame]:
        return df1.merge(df2[keys + [new_col]], on=keys, how=how)

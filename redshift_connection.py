import redshift_connector
import pandas as pd
from typing import Optional
from dotenv import load_dotenv
import os

load_dotenv()

REDSHIFT_HOST = os.environ.get('REDSHIFT_HOST')
REDSHIFT_PORT = os.environ.get('REDSHIFT_PORT')
REDSHIFT_DB = os.environ.get('REDSHIFT_DB')
REDSHIFT_USER = os.environ.get('REDSHIFT_USER')
REDSHIFT_PASSWORD = os.environ.get('REDSHIFT_PASSWORD')


class RedshiftConnector:
    def __init__(self, host: str = REDSHIFT_HOST, database: str = REDSHIFT_DB, user: str = REDSHIFT_USER, password: str = REDSHIFT_PASSWORD, port: int = REDSHIFT_PORT):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = int(port)
        self.connection = None

    def create_dataframe(self, sql_query: str) -> Optional[pd.DataFrame]:
        print(f"Executando query")

        try:
            self.connection = redshift_connector.connect(
                host=self.host,
                database=self.database,
                port=self.port,
                user=self.user,
                password=self.password
            )

            with self.connection.cursor() as cursor:
                cursor.execute(sql_query)

                df = cursor.fetch_dataframe()

            print("DataFrame criado com sucesso!")
            return df

        except Exception as e:
            print(f"Ocorreu um erro ao conectar ou executar a query: {e}")
            return None

        finally:
            if self.connection:
                self.connection.close()
                self.connection = None
                print("Conexão com Redshift fechada.")

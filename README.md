# query-to-dataframe

A ideia é não precisar ficar extraindo csv para desenvolver com dataframes

## Instalação

* Python (usei 3.12.3) 
* lib os
* pip

Instale as libs do _requirements.txt_

``` bash 
pip install -r requirements.txt 
```

## Uso

Configure o .env com as envs

```
REDSHIFT_HOST = "seu_host.region.redshift.amazonaws.com"
REDSHIFT_PORT = 1234
REDSHIFT_DB = "seu_database"
REDSHIFT_USER = "seu_usuario"
REDSHIFT_PASSWORD = "sua_senha"
```

Exemplo de uso 

```
from pandas_redshift import PandasRedshift

conn = PandasRedshift()

query = """
SELECT 'consegui criar um dataFrame de uma query!!!' as coluna;
"""

df = conn.create_dataframe(query)

df.head()
```
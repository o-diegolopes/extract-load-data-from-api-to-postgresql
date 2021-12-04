from urllib.request import urlopen
from sqlalchemy import create_engine
from datetime import datetime
import json
import pandas as pd


class RequestJson:
    def __init__(self, url):
        self.__url = url

    def request_data(self):
        json_url = urlopen(self.__url)
        return json.loads(json_url.read())


class PostgreSQL:
    def __init__(self, username, password, database, dbschema):
        self.__engine = create_engine(
            f"postgresql://{username}:{password}@localhost:5432/{database}",
            connect_args={'options': '-csearch_path={}'.format(dbschema)}
        )

    def table_load(self, dataframe, table):
        dataframe.to_sql(table, self.__engine, if_exists='append')


class TransformData:

    @staticmethod
    def to_df(json):
        df = pd.DataFrame(json)
        df.fillna('', inplace=True)
        return df

    @staticmethod
    def get_current_date():
        return datetime.today().strftime('%Y-%m-%d')

    @staticmethod
    def csv_to_df(file_path):
        df = pd.read_csv(file_path)
        df.fillna('', inplace=True)
        return df
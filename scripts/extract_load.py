from utilities import RequestJson, TransformData, PostgreSQL
import json


class ExtractLoad:
    def __init__(self):
        self.__url_api = "https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/json/"
        self.__files_path = 'C:/Users/diegolopes/Desktop/PROJETOS/extract_load_data_from_api_to_postgresql'

        credential = ''
        with open(f"{self.__files_path}/files/credentials.json") as f:
            credential = json.load(f)
        self.__password = credential.get('PASSWORD')

        self.__conn = PostgreSQL(
            username="postgres",
            password=self.__password,
            database="dell_de_challenge",
            dbschema='challenge'
        )

    def extract(self):
        json_data = RequestJson(url=self.__url_api).request_data()
        df_data = TransformData.to_df(json_data)
        df_data['extraction_date'] = TransformData.get_current_date()
        countries = TransformData.csv_to_df(f'{self.__files_path}/data/countries_of_the_world.csv')

        payload = {
            'covid_cases_deaths': df_data,
            'countries': countries
        }

        return payload

    def load(self, payload):

        for table, data in payload.items():
            self.__conn.table_load(dataframe=data, table=table)


if __name__ == "__main__":
    el = ExtractLoad()
    el.load(payload=el.extract())

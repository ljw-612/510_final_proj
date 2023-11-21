import sqlite3
import csv
import pandas as pd

class DatabaseBuilder:
    """
    This class built a sqlite3 database from the csv files `embedded_groups.csv`, which contains the embedded
    results for all the duke resources.
    """
    @staticmethod
    def main(db_name, csv_files):
        DatabaseBuilder.create_data_base(db_name, csv_files)
        
    @staticmethod
    def create_data_base(db_name, csv_files):
        conn = sqlite3.connect(db_name)
        for csv_file in csv_files:
            table_name = csv_file.split('.')[0]
            print("table name: ", table_name)

            csv_file = 'output/' + csv_file
            df = pd.read_csv(csv_file)

            df.to_sql(table_name, conn, if_exists='replace', index=False)
        
        conn.close()

database_name = 'database/database.db'
csv_files_list = ['embedded_groups.csv']
DatabaseBuilder.main(database_name, csv_files_list)
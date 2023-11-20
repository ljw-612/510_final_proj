import sqlite3
import csv
import pandas as pd

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

create_data_base(database_name, csv_files_list)
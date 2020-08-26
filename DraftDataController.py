# Manipulates data from model and sends to view to be displayed
# Will have a database separate from the excel files created with scraped
# information.
# Database will most likely be created using SQLite python library
# WARNING THIS CODE IS NOT SECURE AND SUSCEPTIBLE TO SQL INJECTIONS

import pandas as pd
import sqlite3 as sq
import combined_soups as model_data

# Position lists for Model to be inserted to EXCEL
# HEADER_LIST = model_data.HEADER_LIST
# print(model_data.QB_LIST)
data_frameQB = pd.DataFrame(model_data.QB_LIST)
data_frameRB = pd.DataFrame(model_data.RB_LIST)
data_frameWR = pd.DataFrame(model_data.WR_LIST)
data_frameTE = pd.DataFrame(model_data.TE_LIST)
data_frameK = pd.DataFrame(model_data.K_LIST)
data_frameDEF = pd.DataFrame(model_data.D_LIST)

# print(data_frameWR)

with pd.ExcelWriter('model_data.xlsx') as writer:
    data_frameQB.to_excel(writer, sheet_name='QB')
    data_frameRB.to_excel(writer, sheet_name='RB')
    data_frameWR.to_excel(writer, sheet_name='WR')
    data_frameTE.to_excel(writer, sheet_name='TE')
    data_frameK.to_excel(writer, sheet_name='K')
    data_frameDEF.to_excel(writer, sheet_name='DEF')
    writer.save()

position_list = ['QB', 'RB', 'WR', 'TE', 'K', 'DEF']
DATA_FRAMES = []

# CREATES A LIST OF POSITIONAL DATA FRAMES GOING FROM EXCEL TO DATA FRAME STRUCTURE IN PANDAS
# DATA_FRAMES IN ORDER OF  position_list
for position in position_list:
    DATA_FRAMES.append(pd.read_excel('model_data.xlsx', sheet_name=position, header=1).drop(columns=0))

# Create an empty sqlite3 database named draft_data and a cursor to the data base to execute sql
# commands on the data base
db_conn = sq.connect('draft_data.db')
c = db_conn.cursor()

# Create tables for everything but DEFENSE
i = 0
for frames in DATA_FRAMES[0:5]:
    frames.to_sql(position_list[i], con=db_conn, if_exists='replace', index=True, index_label='None')
    i += 1

# Create DEF table
DATA_FRAMES[5].to_sql('DEF', con=db_conn, if_exists='replace', index=True, index_label='None')

# For now we are going to ignore the extra column that is added to the front of each table in the DB
# it gets an index name of None, I do not know why this gets added.

# Add two columns to each table in data base, injured and selected.
for table_name in position_list:
    c.execute('ALTER TABLE {} ADD {} VARCHAR'.format(table_name, 'Injured'))
    c.execute('ALTER TABLE {} ADD {} VARCHAR'.format(table_name, 'Selected'))

db_conn.commit()
db_conn.close()

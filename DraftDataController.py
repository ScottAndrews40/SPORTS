# Manipluates data from model and sends to view to be displayed
# Will have a database separate from the excel files created with scraped
# information.
# Database will most likely be created using SQLite python library

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

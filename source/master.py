""" This file is the master file to import and represent data """

import numpy as np
import pandas as pd

sap_data = pd.read_csv('../assets/saptrips.csv', sep=',')
di_data = pd.read_csv('../assets/didata.csv', sep=',')
daily_trip = pd.read_csv('../assets/dailytrip.csv', sep=',')


sap_data_final = sap_data[sap_data['Plant Consigner'] == 'Durg Plant']
sap_data_final = sap_data_final[sap_data_final['material'] != 'CLINKER']
sap_data_final = sap_data_final[sap_data_final['Is Mapped'] == 'No']


di_data['Delivery Number'] = [x.replace('="', "").replace('"', "") for x in di_data['Delivery Number']]

append_dataframe = ""

print(append_dataframe)


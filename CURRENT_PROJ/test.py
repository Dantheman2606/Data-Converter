import pandas as pd
from pathlib import Path
loc = "/Volumes/Data/Daniel/Data Converter/CURRENT_PROJ/test_csv.csv"
if ".csv" in str(loc):
       
            temp_table = pd.read_csv(str(loc))
            #sheet_n = (Path(loc).stem)
            #print(sheet_n)
            print(temp_table)
   
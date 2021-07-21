""" ------------------------------------------------------------------------
-------------- Take raw data from gov open data ----------------------------
----------------- get total cases for a day  -------------------------------
------------------------------------------------------------------------ """

import json
from datetime import datetime

data_list = []

""" ---------------- Get initial list with labels from json----------------- """
with open('0-casesByDayData.json') as json_file:
    data = json.load(json_file)
    for p in data:
        x = {"fecha": p[0],
             "casos": int(p[1])
             }
        data_list.append(x)


""" ---------------- Sort List By Day ----------------- """
data_list = sorted(data_list, key=lambda s: (datetime.strptime(s.get("fecha"), '%d/%m/%Y'), s.get("casos")))

f = open("1-formatedSortedCasesByDay.json", "w")
f.write(json.dumps(data_list, indent=4))
f.close()
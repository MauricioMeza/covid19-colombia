""" ------------------------------------------------------------------------
----------------- Take new Useful Data from data.gov.co --------------------
---------------- and make json by date for mun and cases -------------------
------------------------------------------------------------------------ """

import json
from datetime import datetime

data_list = []

""" ---------------- Get initial list with labels from json----------------- """
with open('1-initialData.json') as json_file:
    data = json.load(json_file)
    for p in data:
        x = {"mun_cod": int(p[0]),
             "casos": int(p[2]),
             "fecha": p[1]}
        data_list.append(x)


""" ---------------- Sort List By Day ----------------- """
data_list = sorted(data_list, key=lambda s: (datetime.strptime(s.get("fecha"), '%d/%m/%Y'), s.get("mun_cod")))


""" ----------------  Group all municipios cases by common day ----------------- """
date = ""
date_list = []
i = 0
for rex in data_list:
    if date != rex.get("fecha"):
        i += 1
        if(i != 1):
            date_list.append(y)

        date = rex.get("fecha")
        y = {"fecha": rex.get("fecha"),
             "mun": []}

    x = {"mun_cod": rex.get("mun_cod"),
         "casos": rex.get("casos")}

    y.get("mun").append(x)

f = open("2-FormatedSorted.json", "w")
f.write(json.dumps(date_list, indent=4))
f.close()



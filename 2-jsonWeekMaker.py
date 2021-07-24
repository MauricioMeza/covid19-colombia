""" ------------------------------------------------------------------------
------------------- Take daily data from jsonFormat.py ----------------------
---------------------- join daily data by week,  ----------------------------
------------------------------------------------------------------------ """

import json

data_week = []

with open('2-formatedSorted.json') as json_file:
    data = json.load(json_file)

    """-----Format Data for the first week of Covid-----"""
    initial = data[0]['fecha'].split("/")[0]
    mun = []
    x = {"fecha": initial + "-" + data[4].get('fecha'),
         'mun': []}

    full_days = 0
    week_days = 2
    for k in data:
        print(full_days)
        week_days += 1
        full_days += 1
        """-----Every 7 Days make a new Week group-----"""
        if week_days%7 == 0:
            initial = k['fecha'].split("/")[0]
            week_days = 0
            x['mun'] = mun
            data_week.append(x)
            mun = []
            if full_days+5 < len(data):
                x = {"fecha": initial + "-" + data[full_days+5].get('fecha'),
                     'mun': []}
            else:
                x = {"fecha": initial + "-" + data[len(data)-1].get('fecha'),
                     'mun': []}


        """-----Add all cases for that week and that municipio to put it into the week group-----"""
        for l in k.get('mun'):
            checker = False
            index = 0
            for m in mun:
                index += 1
                if l['mun_cod'] == m['mun_cod']:
                    checker = True
                    break

            if checker:
                mun[index-1]['casos'] += l.get('casos')
            else:
                mun.append(l)


f = open("3-FormatedSortedWeeks.json", "w")
f.write(json.dumps(data_week, indent=4))
f.close()

""" ------------------------------------------------------------------------
-------------- Take weekly organized data json -----------------------------
----- add extra 0s if municipio didnt have cases that week -----------------
------------------to improve visualization  --------------------------------
------------------------------------------------------------------------ """

import json

with open('3-FormatedSortedWeeks.json') as json_file:
    data = json.load(json_file)

    for i in range(0, len(data)):
        for munN in data[i].get("mun"):
            """---For all values except first---"""
            if i != 0:
                """Check data in previous week and find if there is a data for this municipio last week"""
                checker1 = True
                for munAn in data[i-1].get("mun"):
                    if munN.get("mun_cod") == munAn.get("mun_cod"):
                        checker1 = False
                        
                """If there is none, add 0 cases to this week"""
                if checker1:
                    munNew = {"mun_cod": munN.get("mun_cod"), "casos": 0}
                    data[i-1].get("mun").append(munNew)

            """---For all values except last---"""
            if i != len(data)-1:
                checker2 = True
                """Check data in next week and find if there is a data for this municipio next week"""
                for munDs in data[i+1].get("mun"):
                    if munN.get("mun_cod") == munDs.get("mun_cod"):
                        checker2 = False

                """If there is none, add 0 cases to this week"""
                if checker2:
                    munNew = {"mun_cod": munN.get("mun_cod"), "casos": 0}
                    data[i+1].get("mun").append(munNew)


f = open("4-FormatedSortedWeeks0sFinal.json", "w")
f.write(json.dumps(data, indent=4))
f.close()
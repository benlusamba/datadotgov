# Retrieving U.S. unenmployment data, using the BLS API (automated retrival)

import requests                                           # Import the relevant modules
import json
import prettytable
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['LNS14000000'],"startyear":"2009", "endyear":"2018"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
for series in json_data['Results']['series']:
    x=prettytable.PrettyTable(["series id","year","period","value"]) #add "footnotes"
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']
        #footnotes=""
        #for footnote in item['footnotes']:
        #    if footnote:
                #footnotes = footnotes + footnote['text'] + ','

        x.add_row([seriesId,year,period,value])

    output = open(seriesId + '.txt','w') #export as .csv or .txt file; switch as necessary
    output.write (x.get_string())
    output.close()
    print(x)

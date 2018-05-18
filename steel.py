#Post Tariff Steel Price Appreciation

import requests
import json
import prettytable
headers = {'Content-type': 'application/json'}
data = json.dumps({"seriesid": ['WPU1017'],"startyear":"2014", "endyear":"2018"})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
for series in json_data['Results']['series']:
    x=prettytable.PrettyTable(["series id","year","period","value"]) #add "footnotes"
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']

        x.add_row([seriesId,year,period,value])     

    output = open(seriesId + '.txt','w') #export as .csv or .txt file
    output.write (x.get_string())
    output.close()
    print(x)

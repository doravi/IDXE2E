import json
import requests
from Search import searchAllDatalows


def deleteDataflows():
    print ("Deleting Dataflows")
    dataflows = searchAllDatalows()
    try:
        for dataflow in dataflows['result']:
            url = 'https://idx.il1.gigya.com/idx.deleteDataflow'
            payload = {'apiKey': '3_hhzvJWz8K29RnV73k4xpcUPgI2PaKscZ3vnIOX90fd2qvzz6Ci1GXatDskbDjLCW', 'id': dataflow['id'], 'userKey': 'ANcs28dZbA+Q', 'secret': 'vC/8tyAY2le3YbXjMfQEkyr51L6Nm5on'}
            # GET
            #r = requests.get(url)

            # GET with params in URL
            r = requests.get(url, params=payload, verify=False)
            result = json.loads(r.text)
            print(result)
    except Exception as e:
        print(str(e) + ' there are no dataflows to delete')



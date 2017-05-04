import json
import requests
from Search import searchAllDatalows, searchAllScheduling


def deleteSchedulings():
    schedulings = searchAllScheduling()
    try:
        for scheduling in schedulings['result']:
            url = 'https://idx.il1.gigya.com/idx.deleteScheduling'
            payload = {'apiKey': '3_hhzvJWz8K29RnV73k4xpcUPgI2PaKscZ3vnIOX90fd2qvzz6Ci1GXatDskbDjLCW', 'id': scheduling['id'], 'userKey': 'ANcs28dZbA+Q', 'secret': 'vC/8tyAY2le3YbXjMfQEkyr51L6Nm5on'}
            # GET
            #r = requests.get(url)

            # GET with params in URL
            r = requests.get(url, params=payload, verify=False)
            result = json.loads(r.text)
    except Exception as e:
        print(str(e) + ' there are no Schedulings to delete')



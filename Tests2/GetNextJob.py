import json
import requests


def getNextJob():
    url = 'https://idx.il1.gigya.com/idx.getNextJob'
    payload = {'apiKey': '3_hhzvJWz8K29RnV73k4xpcUPgI2PaKscZ3vnIOX90fd2qvzz6Ci1GXatDskbDjLCW', 'userKey': 'ANcs28dZbA+Q', 'secret': 'vC/8tyAY2le3YbXjMfQEkyr51L6Nm5on'}
    # GET
    #r = requests.get(url)

    # GET with params in URL
    r = requests.get(url, params=payload, verify=False)
    result = json.loads(r.text)
    print(result)


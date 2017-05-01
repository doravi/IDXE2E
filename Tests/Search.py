import json
import requests
from IDX.DataflowGenerator import dataFlowGenerator



def searchAllDatalows():
    query = "SELECT * FROM dataflow"
    url = 'https://idx.il1.gigya.com/idx.search'
    payload = {'apiKey': '3_hhzvJWz8K29RnV73k4xpcUPgI2PaKscZ3vnIOX90fd2qvzz6Ci1GXatDskbDjLCW', 'query': query, 'userKey': 'ANcs28dZbA+Q', 'secret': 'vC/8tyAY2le3YbXjMfQEkyr51L6Nm5on'}
    # GET
    #r = requests.get(url)

    # GET with params in URL
    r = requests.get(url, params=payload, verify=False)
    result = json.loads(r.text)
    print(result)
    return (result)


def searchScheduling():
    query = "SELECT * FROM scheduling order By updateTime desc"
    url = 'https://idx.il1.gigya.com/idx.search'
    payload = {'apiKey': '3_hhzvJWz8K29RnV73k4xpcUPgI2PaKscZ3vnIOX90fd2qvzz6Ci1GXatDskbDjLCW', 'query': query, 'userKey': 'ANcs28dZbA+Q', 'secret': 'vC/8tyAY2le3YbXjMfQEkyr51L6Nm5on'}
    # GET
    #r = requests.get(url)

    # GET with params in URL
    r = requests.get(url, params=payload, verify=False)
    result = json.loads(r.text)
    print(result)
    return (result)


def searchJobStatus():
    query = "SELECT * FROM idx_job_status order By updateTime desc"
    url = 'https://idx.il1.gigya.com/idx.search'
    payload = {'apiKey': '3_hhzvJWz8K29RnV73k4xpcUPgI2PaKscZ3vnIOX90fd2qvzz6Ci1GXatDskbDjLCW', 'query': query, 'userKey': 'ANcs28dZbA+Q', 'secret': 'vC/8tyAY2le3YbXjMfQEkyr51L6Nm5on'}
    # GET
    #r = requests.get(url)

    # GET with params in URL
    r = requests.get(url, params=payload, verify=False)
    result = json.loads(r.text)
    print(result)
    return (result)



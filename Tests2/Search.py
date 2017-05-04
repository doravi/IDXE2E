import json
import requests
import time


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
    resultStatus = ""
    for x in xrange(0, 30):
        if resultStatus != u'succeeded':
            r = requests.get(url, params=payload, verify=False)
            result = json.loads(r.text)
            try:
                resultStatus = result[u'result'][0][u'schedulingStatus']
            except Exception as e:
                print(e)
            time.sleep(1)
            if x == 29:
                raise Exception("Job didnt start")
    print(resultStatus)
    return (resultStatus)


def searchJobStatus():
    query = "SELECT * FROM idx_job_status order By updateTime desc"
    url = 'https://idx.il1.gigya.com/idx.search'
    payload = {'apiKey': '3_hhzvJWz8K29RnV73k4xpcUPgI2PaKscZ3vnIOX90fd2qvzz6Ci1GXatDskbDjLCW', 'query': query, 'userKey': 'ANcs28dZbA+Q', 'secret': 'vC/8tyAY2le3YbXjMfQEkyr51L6Nm5on'}
    # GET
    #r = requests.get(url)

    # GET with params in URL
    r = requests.get(url, params=payload, verify=False)
    result = json.loads(r.text)
    resultStatus = result[u'result'][0][u'status']
    for x in xrange(0, 30):
        if resultStatus != u'succeeded':
            r = requests.get(url, params=payload, verify=False)
            result = json.loads(r.text)
            resultStatus = result[u'result'][0][u'status']
            if x == 29:
                raise Exception("Job not finished")

    fileName = result[u'result'][0][u'trace'][3]
    line, fileName = fileName.split("file ")
    fileName = str(fileName)
    return (fileName)


def searchAllScheduling():
    query = "SELECT * FROM scheduling order By updateTime desc "
    url = 'https://idx.il1.gigya.com/idx.search'
    payload = {'apiKey': '3_hhzvJWz8K29RnV73k4xpcUPgI2PaKscZ3vnIOX90fd2qvzz6Ci1GXatDskbDjLCW', 'query': query, 'userKey': 'ANcs28dZbA+Q', 'secret': 'vC/8tyAY2le3YbXjMfQEkyr51L6Nm5on'}
    # GET
    #r = requests.get(url)

    # GET with params in URL
    r = requests.get(url, params=payload, verify=False)
    result = json.loads(r.text)
    print(result)
    return (result)






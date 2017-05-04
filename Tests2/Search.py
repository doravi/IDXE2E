import sys
sys.path.append('/Tests2')

import json
import requests
import time
from GetNextJob import getNextJob


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
    print ("Searching schedualing status")
    query = "SELECT * FROM scheduling order By updateTime desc"
    url = 'https://idx.il1.gigya.com/idx.search'
    payload = {'apiKey': '3_hhzvJWz8K29RnV73k4xpcUPgI2PaKscZ3vnIOX90fd2qvzz6Ci1GXatDskbDjLCW', 'query': query, 'userKey': 'ANcs28dZbA+Q', 'secret': 'vC/8tyAY2le3YbXjMfQEkyr51L6Nm5on'}
    # GET
    #r = requests.get(url)

    # GET with params in URL
    resultStatus = ""
    for x in xrange(0, 5):
        if resultStatus == u'ready' or resultStatus == u'busy':
            r = requests.get(url, params=payload, verify=False)
            result = json.loads(r.text)
            try:
                resultStatus = result[u'result'][0][u'schedulingStatus']
                break
            except Exception as e:
                print(e)
            #getNextJob()
            time.sleep(3)
            if x == 4:
                raise Exception("Job didnt start")
    print(resultStatus)
    return (resultStatus)


def searchJobStatus():
    print ("Searching job status")
    query = "SELECT * FROM idx_job_status order By updateTime desc"
    url = 'https://idx.il1.gigya.com/idx.search'
    payload = {'apiKey': '3_hhzvJWz8K29RnV73k4xpcUPgI2PaKscZ3vnIOX90fd2qvzz6Ci1GXatDskbDjLCW', 'query': query, 'userKey': 'ANcs28dZbA+Q', 'secret': 'vC/8tyAY2le3YbXjMfQEkyr51L6Nm5on'}
    # GET
    #r = requests.get(url)

    # GET with params in URL
    r = requests.get(url, params=payload, verify=False)
    result = json.loads(r.text)
    resultStatus = result[u'result'][0][u'status']
    for x in xrange(0, 5):
        if resultStatus != u'succeeded':
            r = requests.get(url, params=payload, verify=False)
            result = json.loads(r.text)
            resultStatus = result[u'result'][0][u'status']
            if x == 4:
                raise Exception("Job not finished")

        else:
            break

        time.sleep(3)

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






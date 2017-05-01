import json
import requests
from IDX.DataflowGenerator import dataFlowGenerator



def createSchedulaing(dataFlowId):
    data = {"dataflowId":dataFlowId,"frequencyType":"once","name":"Export from Gigya to SFTP","fullExtract":True,"limit":10}
    url = 'https://idx.il1.gigya.com/idx.createScheduling'
    payload = {'apiKey': '3_hhzvJWz8K29RnV73k4xpcUPgI2PaKscZ3vnIOX90fd2qvzz6Ci1GXatDskbDjLCW', 'data': json.dumps(data), 'userKey': 'ANcs28dZbA+Q', 'secret': 'vC/8tyAY2le3YbXjMfQEkyr51L6Nm5on'}
    # GET
    #r = requests.get(url)

    # GET with params in URL
    r = requests.get(url, params=payload, verify=False)
    print (r.text)




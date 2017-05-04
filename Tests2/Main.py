import sys

sys.path.append('/Tests2')

from CreateDataFlow import createDataFlow
from CreateScheduling import createSchedulaing
from DeleteDataflows import deleteDataflows
from Search import searchScheduling, searchJobStatus
from ReadFromSFTP import readFileFromSFTP
from CompareOutputs import compareOutputs

try:
    dataFlowId = createDataFlow()
    createSchedulaing(dataFlowId)
    searchScheduling()
    fileName = searchJobStatus()
    readFileFromSFTP(fileName)
    compareOutputs()
except Exception as e:
    print(e)
finally:
    deleteDataflows()


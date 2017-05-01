import sys
sys.path.append('/Tests2')

from CreateDataFlow import createDataFlow
from CreateScheduling import createSchedulaing
from DeleteDataflows import deleteDataflows
from Search import searchScheduling, searchJobStatus


dataFlowId = createDataFlow()
createSchedulaing(dataFlowId)
searchScheduling()
searchJobStatus()
deleteDataflows()

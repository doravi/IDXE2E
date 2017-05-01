from IDX.DeleteDataflows import deleteDataflows

__author__ = 'dor.av'

from IDX.CreateDataFlow import createDataFlow
from IDX.CreateScheduling import createSchedulaing
from IDX.Search import searchScheduling, searchJobStatus


dataFlowId = createDataFlow()
createSchedulaing(dataFlowId)
searchScheduling()
searchJobStatus()
deleteDataflows()
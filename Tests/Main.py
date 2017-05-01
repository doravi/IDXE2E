from Tests.CreateDataFlow import createDataFlow
from Tests.CreateScheduling import createSchedulaing
from Tests.DeleteDataflows import deleteDataflows
from Tests.Search import searchScheduling, searchJobStatus


dataFlowId = createDataFlow()
createSchedulaing(dataFlowId)
searchScheduling()
searchJobStatus()
deleteDataflows()
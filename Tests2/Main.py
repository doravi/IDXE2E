from Tests2.CreateDataFlow import createDataFlow
from Tests2.CreateScheduling import createSchedulaing
from Tests2.DeleteDataflows import deleteDataflows
from Tests2.Search import searchScheduling, searchJobStatus

def main():
    dataFlowId = createDataFlow()
    createSchedulaing(dataFlowId)
    searchScheduling()
    searchJobStatus()
    deleteDataflows()

import request 
from enum import Enum

class StatusEnum(Enum): 
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

class ComponentEnum(Enum): 
    API_DOCS = "API_DOCS"
    HELP_CENTER = "HELP_CENTER"
    SDK_DOCS = "SDK_DOCS"
    OAS_FILE = "OAS_FILE"

class ConnectedTask:
    task_id: str
    title: str
    description: str
    status: StatusEnum

class Task:
    task_id: str
    title: str
    description: str
    status: StatusEnum
    component: ComponentEnum
    connected_tasks: list[ConnectedTask]

class TaskResponse:
    task_id: str

class TechnicalWriterTasks:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
    def tasks() -> list[Task]:
        response = requests.get('https://api.techwriter.xyz/tasks')
        print(response.status_code) 
    def upload(task: Task) -> TaskResponse:
        response = requests.post('https://api.techwriter.xyz/tasks')
        print(response.status_code)  




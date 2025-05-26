import requests 
from enum import Enum

'''
Rule of thumb: Python runs from top to bottom. 
Declare variables at the beginning
'''

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

class TaskInput:
    title: str
    description: str
    status: StatusEnum
    component: ComponentEnum
    connected_tasks: list[ConnectedTask]

class TaskResponse:
    task_id: str

class Error:
    description: str

class TechnicalWriterTasks:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key
    def tasks(status: StatusEnum, component: ComponentEnum, updatedAfter: str) -> list[Task]:
        headers = {'X-API-KEY': 'apiKey'}
        params = {'status': status, 'component': component, 'updatedAfter': updatedAfter}
        response = requests.get('https://api.techwriter.xyz/tasks', headers=headers, params=params)
        print(response.status_code) 

    def upload(task: Task) -> TaskResponse:
        headers = {'X-API-KEY': 'apiKey'}
        payload = {'task_id': task.task_id, 'title': task.title, 'description': task.description, 'status': task.status, 'component': task.component, 'connected_tasks': task.connected_tasks}
        response = requests.post('https://api.techwriter.xyz/task', headers=headers, payload=payload)
        print(response.status_code)  

TechnicalWriterTasks.tasks()
TechnicalWriterTasks.upload()

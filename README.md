<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="assets/style.css">
</head>

<html>

<div class="content">
<h1>Introduction</h1>
<p>The Technical Writer Tasks API is designed to track the progress and status of technical writers&#39; assignments.</p>

<h1>Product Overview</h1>
<p>The Technical Writer Tasks API offers two primary endpoints: a <code>GET</code> endpoint for retrieving all tasks and a <code>POST</code> endpoint for creating new tasks, which can be added as resources to the API.</p>

<h1>Authentication</h1>
<ul>
<li>Users are required to register for an account using a username and password.</li>
<li>Upon successful registration, users will be provided with a unique API key which is used to authenticate requests.</li>
<li>The client must include the API key in the X-API-KEY header to authenticate requests.</li>
</ul>

<h1>Resources</h1>

<h2>Technical Writer Tasks</h2>
<p>Retrieves an array of task properties assigned to the technical writers. </p>


<div><span>GET </span><code>https://api.techwriter.xyz/tasks</code></div>

<br>
<p><b>Parameters</b></p>
<table>
<tr>
<th>Name</th>
<th>Type</th>
<th>Required/ optional</th>
<th>Description</th>
<th>Location</th>
</tr>
<tr>
<td>Status</td>
<td>String</td>
<td>Optional</td>
<td>Filter tasks by status</td>
<td>Query</td>
</tr>
<tr>
<td>Component</td>
<td>String</td>
<td>Optional</td>
<td>Filter tasks by component</td>
<td>Query</td>
</tr>
<tr>
<td>updatedAfter</td>
<td>String</td>
<td>Optional</td>
<td>Filter tasks that have been modified after a specific date (format: YYYY-MM-DD)</td>
<td>Query</td>
</tr>
<tr>
<td>X-API-KEY</td>
<td>apiKey</td>
<td>Required</td>
<td>Authentication token</td>
<td>Header</td>
</tr>
</table>
<br>
<p><b>Example of cURL call</b></p>

```bash
curl -X 'GET' \
    'https://api.techwriter.xyz/tasks?status=IN_PROGRESS&component=API_DOCS&updatedAfter=2022-05-10' \
        -H 'accept: application/json' \
        -H 'X-API-KEY: eyJhbGciOiJ...POk6yJV_adQssw5c'
```
<br>
<p><b>Example of API response in JSON format</b></p>

```json
[
    {
        "task_id": "string",
        "title": "string",
        "description": "string",
        "status": "OPEN",
        "component": "API_DOCS",
        "connected_tasks": [
            {
                "task_id": "string",
                "title": "string",
                "description": "string",
                "status": "OPEN"
            }
        ]
    }
]
```

<p style="margin-top: 0%;"><i style="font-size: small;">A successful request returns an array of tasks.</i></p>

<br>

<p><b>Example of 401 error response</b></p>

```json
{
    "description": "Unauthorized, API key missing or invalid."
}
```
<p style="margin-top: 0%;"><i style="font-size: small;">The 401 error code response indicates that the request was not authorized due to invalid credentials or an invalid API key.</i></p>

<br>
     
<p><b>Fields in API response</b></p>
<p><b>task_id</b> <i>string</i></p>
<p>A unique ID specific to the task.</p>
<hr>
<p><b>title</b> <i>string</i></p>
<p>The title of the technical documentation for the specific task.</p>
<hr>
<p><b>description</b> <i>string</i></p>
<p>A summary of the technical documentation for the specific task.</p>
<hr>
<p><b>status</b> <i>string</i></p>
<p>The status object derives from StatusEnum enumeration, which include the following cases: OPEN, IN_PROGRESS, and COMPLETED.</p>
<hr>
<p><b>component</b> <i>string</i></p>
<p>The component object derives from ComponentEnum enumeration, which includes the following cases: API_DOCS,
HELP_CENTER, SDK_DOCS, OAS_FILE.</p>
<hr>
<p><b>connected_tasks</b> <i>array</i></p>
<p>The connected_tasks property is an array of ConnectedTask object. The ConnectedTask object includes the following fields: task_id, title, description, and status. The status field uses the StatusEnum enumeration, which
includes the following cases: OPEN, IN_PROGRESS, and COMPLETED.</p>
<hr>

<h2>New Technical Writer Task</h2>
<p>Creates a new technical writer task.</p>
<div><span>POST </span><code>https://api.techwriter.xyz/task</code></div>

<br>

<p><b>Parameters</b></p>
<table>
<tr>
<th>Name</th>
<th>Type</th>
<th>Required/ optional</th>
<th>Description</th>
<th>Location</th>
</tr>
<tr>
<td>X-API-KEY</td>
<td>apiKey</td>
<td>Required</td>
<td>Authentication token</td>
<td>Header</td>
</tr>
</table>

<br>

<p><b>Request body</b></p>

```json
{
    "task_id": "string",
    "title": "string",
    "description": "string",
    "status": "OPEN",
    "component": "API_DOCS",
    "connected_tasks": [
        {
        "task_id": "string",
        "title": "string",
        "description": "string",
        "status": "OPEN"
        }
    ]
}
```

<br>

<p><b>Example of POST request using Python</b></p>

```python
import requests

url = "https://api.techwriter.xyz/task"
headers = {'Content-Type': 'application/json', 'X-API-KEY': 'eyJhbGciOiJ...POk6yJV_adQssw5c'}
data = {    
    "task_id": "str"
    "title": "str"
    "description": "str"
    "status": "OPEN"
    "component": "API_DOCS"
    "connected_tasks": []
    }

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.status_code)
print(response.json())
```

<br>

<p><b>Example of API response in JSON format</b></p>

```json
{
    "task_id": "string"
} 
```
<p><i>A successful request returns the task ID of the new task that was uploaded.</i></p>

<br>

<p><b>Example of 400 error response</b></p>

```json
{
    "description": "Bad request, malformed data."
}  
```
<p style="margin-top: 1%;"><i style="font-size: small;">The 400 error code response indicates that the data sent contains data format issues or missing required fields.</i></p>

<br>

<p><b>Fields in API response</b></p>
<p><b>task_id</b> <i>string</i></p>
<p>A unique ID specific to the task.</p>
<hr>


<h1>HTTP Response Status Codes</h1>
<table>
<tr>
<th>Status Code</th>
<th>Description</th>
</tr>
<tr>
<td>200 OK</td>
<td>The request has succeeded.</td>
</tr>
<tr>
<td>400 Bad Request</td>
<td>The request was unacceptable, containing malformed data.</td>
</tr>
<tr>
<td>401 Unauthorized</td>
<td>The request contained invalid authentication credentials or, an expired or missing API key.</td>
</tr>
<tr>
<td>500 Server Error</td>
<td>An unexpected error on the server. (These are rare)</td>
</table>

<h1>Best Practices</h1>
<p><b>Handle Rate Limits</b></p>
<p>To safeguard overloading the API infrastructure, implement API processing limits to restrict the number of
endpoint transactions. These limitations will manage and regulate the number of transactions allowed for each
endpoint.</p>

<p><b>Manage Error Codes</b></p>
<ul>
<li>In the case of a 400 (Bad Request) error code, ensure the validity of the data format and that the required
fields are filled.</li>
<li>In the case of a 401 (Unauthorized) error code, ensure the API key is valid, and not expired or missing.
</li>
</ul>

<p><b>Safeguard API Key</b></p>
<ul>
<li>Regularly rotate API keys to limit their lifespan and reduce vulnerabilities.</li>
<li>To prevent your credentials from being compromised, do not include your API key in your source code.</li>
<li>Pass your token externally, such as using a .env file or other secrets manager.</li>
</ul>
</div>

</html>
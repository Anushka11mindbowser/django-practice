import json

import requests
import json

URL = "http://127.0.0.1:8000/per_create/"

data = {
    'name': 'Mary',
    'surname': 'Johnson',
    'city':'Greenwood',
    'state':'Indiana',
    'country':'USA'

}
json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
data = r.json
print(data)

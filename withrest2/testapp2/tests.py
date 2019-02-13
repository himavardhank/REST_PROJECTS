import requests
import json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
def get_resources(id=None):
    data={}
    if id is not None:
        data={
        'id':id
        }
    resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
    #print(resp.status_code)
    #print(resp.json())
#get_resources()
def create_resource():
	new_data={
	'eno': 222,
	'ename':'rana daggubati',
	'esal':50000,
	'eaddr':'film nagar',
	}
	r=requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))
	print(r.status_code)
	print(r.json)
#create_resource()
def update_resource(id):
    new_data={
    'id':id,
    'eno':222,
    'ename':'raju',
    'esal':5000,
    'eaddr':'hyd',
    }
    r=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_data))
    print(r.status_code)
    # print(r.text)
    print(r.json())
update_resource(3)

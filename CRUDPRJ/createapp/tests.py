import requests,json
BASE_URL='http://127.0.0.1:8000/'
END_POINT='api/'
def create_resource():
    new_emp={'eno':1000,'ename':'shiva','esal':147000,'eaddr':'bagya nagar',}
    r=requests.post(BASE_URL+END_POINT,data=json.dumps(new_emp))
    print(r.status_code)
    print(r.text)
    print(r.json())
create_resource()

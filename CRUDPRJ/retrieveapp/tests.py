#import requests
#BASE_URL='http://127.0.0.1:8000/'
#END_POINT='mixall/'
#n=input('enter emp id')
#r=requests.get(BASE_URL+END_POINT+'1/')
#if r.status_code in range(200,300):
#if r.status_code ==requests.codes.ok:
#    data=r.json()
#    print(data)
#else:
#    print('something wrong')
#    print('status code',r.status_code)
# Create your tests here.
import requests
import json
BASE_URL='http://127.0.0.1:8000/'
END_POINT='mixins/'
def create_resource():
    new_emp={
    'eno':1000,
    'ename':'shiva',
    'esal':147000,
    'eaddr':'bagya nagar',
    }
    r=requests.post(BASE_URL+END_POINT,data=json.dumps(new_emp))
    #print(r.status_code)
    #print(r.text)
    #print(r)
create_resource()

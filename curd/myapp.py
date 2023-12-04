import requests
import json
URL="http://127.0.0.1:8000/stuapi/"

def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)

    r=requests.get(url=URL,data=json_data)#jha bhejna hai
    data=r.json()
    print(data)


# get_data()#read function
def post_data():
    data={
        'name':'kashish',
        'st_id':18,
        'city':'kanpur'
    }
    json_data=json.dumps(data)
    r=requests.post(url=URL,data=json_data)#jha bhejna hai
    mydata=r.json()
    print(mydata)

# post_data()
def update_data():
    data={
        'id':3,
        'name':'kash',
        
        'city':'kanpur'

    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)#jha bhejna hai
    mydata=r.json()
    print(mydata)

# update_data()

def delete_data():
    data={
        'id':2,
    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)#jha bhejna hai
    mydata=r.json()
    print(mydata)
    
delete_data()





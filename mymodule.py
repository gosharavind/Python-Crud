import requests
import json

# @ To get all Todos data
# @ Type get
def getData(url):
   response = requests.get(url)
   return response.json()

# @ To get single Data data
# @ Type get
def getSingleData(url,json):
   response = requests.get(url,json)
   return response.json()

# @ To create single Data 
# @ Type POST
def createData(url,data):
    headers =  {"Content-Type":"application/json"}
    data = json.dumps(data)
    response = requests.post(url,data,headers=headers)
    return response.json()

# @ To get single Datas data
# @ Type PUT
def editData(url,json):
   response = requests.put(url,json)
   return response.json()

# @ To get single Datas data
# @ Type PATCH
def patchData(url,json):
   response = requests.patch(url,json)
   return response.json()

# @ To get single Datas data
# @ Type Delete
def deleteData(url,json):
   response = requests.delete(url)
   return response.json()




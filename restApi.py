import requests
import json

api_User_url = "https://jsonplaceholder.typicode.com/users"
my_api_url = "https://jsonplaceholder.typicode.com/todos"

# # @ To get all Todos data
# # @ Type GET
def getTodo(url):
   response = requests.get(url)
   return response.json()

# # @ To get single Todo data
# # @ Type GET/:id
def getSingleTodo(url,json):
   response = requests.get(url,json)
   return response.json()

# # @ To create single Todo 
# # @ Type POST
def createTodo(url,data):
    headers =  {"Content-Type":"application/json"}
    data = json.dumps(data)
    response = requests.post(url,data,headers=headers)
    return response.json()

# # @ To get single Todos data
# # @ Type PUT
def editTodo(url,json):
   response = requests.put(url,json)
   return response.json()

# # @ To get single Todos data
# # @ Type PATCH
def patchTodo(url,json):
   response = requests.patch(url,json)
   return response.json()

# # @ To get single Todos data
# # @ Type Delete
def deleteTodo(url,json):
   response = requests.delete(url)
   return response.json()

#print(getTodoDetails(api_Todo_url))
# print(getSingleTodo(my_api_url,{"id":2}))
#print(getSingleTodoDetails(api_Todo_url,{"address.zipcode": "92998-3874"}))

req = {
  "userId": 1,
  "id": 11,
  "title": "illo est ratione doloremque quia maiores aut",
  "completed": True
}

#  print(getTodo(url,json))

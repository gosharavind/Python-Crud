import requests
import datetime
import apimodule as ap


myURl = "https://jsonplaceholder.typicode.com/posts/1/comments"

getProducts = "http://localhost:4000/products"

getSingleProduct = "http://localhost:4000/products/:id"

userURl = "https://jsonplaceholder.typicode.com/users"

# result = requests.get(userURl)

# print(result.json())

# def getData(url):
#     result = requests.get(url)
#     return result.json()


# print(getData(userURl))

# x = datetime.datetime.now()
# print(x)

print(ap.getData(getProducts))
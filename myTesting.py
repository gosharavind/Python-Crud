import requests
import json
import mymodule

userSignUp = "http://localhost:4000/users/signup"
productsUrl = "http://localhost:4000/products/"
payload = {
  "email": "sam@gmail.com",
  "password": "abcd"
}
headers = {
  'Content-Type': 'application/json'
}

# response = requests.request("POST", url, headers=headers, data=payload)
# result = mymodule.createData(url,payload)
result = mymodule.getData(productsUrl)
print(result)



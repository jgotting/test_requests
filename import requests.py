import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos/2")
print(response.status_code)
res = (response.json()) #Transform JSON to a python dictionary
print(res)
print(type(res)) #Check the type
for l in res: #Iterate through the Dict
    print(l, " --> ", res[l])

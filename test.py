import requests

url = 'https://bayut.onrender.com/predict/riyadh'

data = {

    "Type_encoding": 0,
    "Price": 200,
    "Area_m2": 50,
}

response = requests.post(url, json=data)

print(response.json())
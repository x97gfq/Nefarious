import json
import requests

url = "http://192.168.1.99/phpAppExample/testpage.php"

def get_data():
    response = requests.get(url)
    
    if response.status_code == 200:
        return "{}: {}".format(response.status_code, response.content)
    else:
        return "{}: {}".format(response.status_code, "error")

for x in range(10):
    info = get_data()
    print(info)
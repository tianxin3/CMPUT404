import requests

print(requests.__version__)

google = requests.get("http://google.com")
print(google)


# raw url from github
var = requests.get("https://raw.githubusercontent.com/tianxin3/CMPUT404/master/lab1.py")

print(var.content)
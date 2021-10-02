import requests


with open("dataset_3378_2.txt") as file:
    url_link = file.read().split()
r = requests.get(url_link[0]).text.splitlines()
print(len(r))

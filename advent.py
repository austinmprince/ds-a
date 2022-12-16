import urllib.request

# specify the URL of the text file you want to download
url = "https://adventofcode.com/2022/day/1/input"

# download the file from the URL
import requests

# send the GET request to the API endpoint
response = requests.get(url)

# check the status code of the response to make sure the request was successful
if response.status_code == 200:
    # if the request was successful, process the response data
    data = response.json()
    print(data)
else:
    # if the request was not successful, print an error message
    print(response)


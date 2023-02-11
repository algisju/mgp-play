# import urllib library
from urllib.request import urlopen
  
# import json
import json
# store the URL in url as 
# parameter for urlopen
url = "https://www.motogp.com/en/json/live_timing/686"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
result_json = json.dumps(data_json,indent=1)
#printing the converted json object
print(result_json)
  
# print the json response
# print(data_json)
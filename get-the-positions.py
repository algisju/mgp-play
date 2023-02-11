##retrieve live timing motogp
#search index.html for table class="timing_table" data-trsid="xxx"

import urllib.request, json

url = "https://www.motogp.com/en/json/live_timing/685"

response = urllib.request.urlopen(url)

data = json.loads(response.read().decode())
print(data["lt"] ["head"] ["session_name"])

for x in range(1, 28):
	try:
		print(str(x)+" - "+data["lt"] ["rider"] [str(x)] ["rider_name"]+" "+data["lt"] ["rider"] [str(x)] ["rider_surname"] )
	except KeyError:
		break







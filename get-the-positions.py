##retrieve live timing motogp
#search index.html for table class="timing_table" data-trsid="xxx"

import urllib.request, json, os, time 

url = "https://www.motogp.com/en/json/live_timing/685"


response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())

while (data["lt"] ["head"] ["session_status_id"]) =="F":
	os.system("cls")
	print(data["lt"] ["head"] ["session_name"]+"\n")

	for x in range(1, 28):
		try:
			print(str(x)+" - "+data["lt"] ["rider"] [str(x)] ["rider_name"]+" "+data["lt"] ["rider"] [str(x)] ["rider_surname"] )
		except KeyError:
			break
	time.sleep(60)







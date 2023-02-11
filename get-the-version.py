import requests, re
url = "http://motogp.com/"
response = requests.get(url)
if response.status_code == 200:
    html = response.text
    match = re.search(r'data-trsid="(\d+)"', html)
    if match:
        ver = match.group(1)
    else:
        ver = None
    print(ver)
else:
    print("Failed to retrieve the HTML document. Response code:", response.status_code)
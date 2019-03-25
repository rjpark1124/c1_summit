import json
import requests
#
r = requests.get('https://images-api.nasa.gov/search', params = {'q':'space', 'media_type':'image'})
results = json.loads(r.text)
#print(json.dumps(results, indent=4))
list_of_results = results['collection']['items']
map = {}
for data in list_of_results:
    #print(data['links'][0]['href'])
    c = data['data'][0]['center']
    if c not in map:
        map[c] = c

print(map)

# r = requests.get('https://images-api.nasa.gov/search', params = {'nasa_id':'PIA14192'})
# results = json.loads(r.text)
# image = results['collection']['items'][0]['href']
# r1 = requests.get(image)
# results2 = json.loads(r1.text)
# print(results)

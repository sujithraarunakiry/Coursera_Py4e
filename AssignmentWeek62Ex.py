import urllib,json

# serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})

    print ('Retrieving ',url)
    url_handle = urllib.request.urlopen(url)
    data = url_handle.read()

    print ('Retrieved',len(data),'characters')
    json_data = json.loads(data)

    #print json.dumps(json_data['results'], indent=3)
    print ('Place id',json_data['results'][0]['place_id'])
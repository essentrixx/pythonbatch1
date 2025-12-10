import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

# Prompt for location
address = input("Enter location: ")
url = serviceurl + urllib.parse.urlencode({'q': address})
print("Retrieving", url)

# Read data from URL
data = urllib.request.urlopen(url).read()
print("Retrieved", len(data), "characters")

# Parse JSON
js = json.loads(data)

# Print the JSON structure to see what we're working with
print(json.dumps(js, indent=2))

# Extract the first plus_code
# The structure is features[0]['properties']['plus_code']
plus_code = js['features'][0]['properties']['plus_code']
print("Plus code", plus_code)
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Input for the actual assignment
url = 'http://py4e-data.dr-chuck.net/known_by_Thalia.html'
count = 7
position = 18

# Adjust position to zero-indexed
position = position - 1

for i in range(count + 1):
    print("Retrieving:", url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all anchor tags
    tags = soup('a')
    if i < count:  # Don't follow link on the last iteration
        url = tags[position].get('href', None)

# Extract the last name from the final URL
last_name = url.split("_")[-1].split(".")[0]
print("Last name in sequence:", last_name)
